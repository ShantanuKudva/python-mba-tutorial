// Pyodide + Monaco code editor (VSCode-style).
// Public API:
//   - enhanceCodeBlocks(rootEl): turn ```python blocks into runnable editors
//   - mountFullEditor(container, path, code): cell-based notebook for .py exercises

(function () {
  const PYODIDE_VERSION = "0.26.4";
  const PYODIDE_URL =
    "https://cdn.jsdelivr.net/pyodide/v" + PYODIDE_VERSION + "/full/";
  const MONACO_BASE = "https://cdn.jsdelivr.net/npm/monaco-editor@0.52.0/min/vs";

  let pyodideReadyPromise = null;
  let monacoReadyPromise = null;
  const editors = new Set(); // {editor, model, relint}

  function loadScript(src) {
    return new Promise((resolve, reject) => {
      const s = document.createElement("script");
      s.src = src;
      s.onload = resolve;
      s.onerror = () => reject(new Error("Failed: " + src));
      document.head.appendChild(s);
    });
  }

  function ensureMonaco() {
    if (monacoReadyPromise) return monacoReadyPromise;
    monacoReadyPromise = (async () => {
      await loadScript(MONACO_BASE + "/loader.min.js");
      window.require.config({ paths: { vs: MONACO_BASE } });
      window.MonacoEnvironment = {
        getWorkerUrl: function () {
          return (
            "data:text/javascript;charset=utf-8," +
            encodeURIComponent(`
              self.MonacoEnvironment = { baseUrl: '${MONACO_BASE}/' };
              importScripts('${MONACO_BASE}/base/worker/workerMain.js');
            `)
          );
        },
      };
      await new Promise((res) =>
        window.require(["vs/editor/editor.main"], res)
      );
      return window.monaco;
    })();
    return monacoReadyPromise;
  }

  async function ensurePyodide(statusEl) {
    if (pyodideReadyPromise) return pyodideReadyPromise;
    pyodideReadyPromise = (async () => {
      if (statusEl) statusEl.textContent = "Loading Python (~10MB, first time)…";
      await loadScript(PYODIDE_URL + "pyodide.js");
      const py = await window.loadPyodide({ indexURL: PYODIDE_URL });
      await py.loadPackage("micropip");
      // Expose JS prompt() to Python so input() works.
      py.globals.set("__js_prompt__", (msg) => {
        const r = window.prompt(msg || "Input:");
        return r === null ? "" : r;
      });
      py.runPython(`
import ast, builtins
def __lint(src):
    try:
        ast.parse(src)
        return None
    except SyntaxError as e:
        return (str(e.msg), int(e.lineno or 1), int(e.offset or 1))

# Browser-friendly input(): use JS prompt(). Echo to stdout for transcript.
def __browser_input(prompt=""):
    if prompt:
        print(prompt, end="")
    val = __js_prompt__(prompt)
    print(val)
    return val
builtins.input = __browser_input

# Per-session user namespace so cells share state.
__user_ns__ = {"__name__": "__main__", "input": __browser_input}
def __reset_ns():
    __user_ns__.clear()
    __user_ns__["__name__"] = "__main__"
    __user_ns__["input"] = __browser_input
`);
      editors.forEach((e) => e.relint());
      return py;
    })();
    return pyodideReadyPromise;
  }

  function detectMissingPackage(errText) {
    const m = errText.match(/No module named ['"]([^'"]+)['"]/);
    return m ? m[1] : null;
  }

  const PIP_NAMES = {
    cv2: "opencv-python",
    PIL: "pillow",
    sklearn: "scikit-learn",
    yaml: "pyyaml",
    bs4: "beautifulsoup4",
  };

  async function tryInstall(py, importName, statusEl) {
    const pipName = PIP_NAMES[importName] || importName;
    statusEl.textContent = "Installing " + pipName + "…";
    const micropip = py.pyimport("micropip");
    try {
      await micropip.install(pipName);
      statusEl.textContent = "Installed " + pipName + ". Click Run again.";
      return true;
    } catch (e) {
      statusEl.textContent = "Could not install " + pipName + ": " + e.message;
      return false;
    }
  }

  async function lintModel(monaco, model) {
    if (!pyodideReadyPromise) {
      monaco.editor.setModelMarkers(model, "pyodide", []);
      return;
    }
    try {
      const py = await pyodideReadyPromise;
      const result = py.globals.get("__lint")(model.getValue());
      if (result === undefined || result === null) {
        monaco.editor.setModelMarkers(model, "pyodide", []);
        return;
      }
      const arr = result.toJs ? result.toJs() : result;
      const [msg, line, col] = arr;
      const lineLen = model.getLineLength(line) || col;
      monaco.editor.setModelMarkers(model, "pyodide", [
        {
          severity: monaco.MarkerSeverity.Error,
          message: String(msg),
          startLineNumber: line,
          startColumn: Math.max(1, col),
          endLineNumber: line,
          endColumn: lineLen + 1,
        },
      ]);
    } catch {
      // ignore
    }
  }

  function getMonacoTheme() {
    const dark =
      document.documentElement.getAttribute("data-theme") === "dark";
    return dark ? "vs-dark" : "vs";
  }

  function commonOptions(readOnly) {
    return {
      language: "python",
      theme: getMonacoTheme(),
      fontSize: 13.5,
      fontFamily:
        'ui-monospace, "SF Mono", Menlo, Consolas, "DejaVu Sans Mono", monospace',
      minimap: { enabled: false },
      scrollBeyondLastLine: false,
      automaticLayout: true,
      tabSize: 4,
      insertSpaces: true,
      readOnly: !!readOnly,
      lineNumbers: "on",
      lineNumbersMinChars: 3,
      padding: { top: 8, bottom: 8 },
      bracketPairColorization: { enabled: true },
      renderLineHighlight: readOnly ? "none" : "line",
      scrollbar: { vertical: "auto", horizontal: "auto" },
    };
  }

  async function makeMonaco(host, code, opts) {
    opts = opts || {};
    const monaco = await ensureMonaco();
    const editor = monaco.editor.create(
      host,
      Object.assign(commonOptions(opts.readOnly), { value: code })
    );
    const model = editor.getModel();

    let lintTimer = null;
    const relint = () => {
      clearTimeout(lintTimer);
      lintTimer = setTimeout(() => lintModel(monaco, model), 350);
    };
    if (!opts.readOnly) {
      model.onDidChangeContent(relint);
      relint();
    }

    const handle = { editor, model, relint, monaco };
    editors.add(handle);
    return handle;
  }

  async function runPython(code, outEl, statusEl, installSlot, useUserNs) {
    outEl.textContent = "";
    installSlot.innerHTML = "";
    statusEl.textContent = "Loading runtime…";
    const py = await ensurePyodide(statusEl);
    statusEl.textContent = "Running…";

    let stdout = "";
    let stderr = "";
    py.setStdout({ batched: (s) => (stdout += s + "\n") });
    py.setStderr({ batched: (s) => (stderr += s + "\n") });

    try {
      if (useUserNs) {
        const ns = py.globals.get("__user_ns__");
        await py.runPythonAsync(code, { globals: ns });
      } else {
        await py.runPythonAsync(code);
      }
      outEl.textContent = stdout || "(no output)";
      if (stderr) outEl.textContent += "\n" + stderr;
      outEl.classList.remove("err");
      statusEl.textContent = "Done.";
    } catch (err) {
      const msg = err.message || String(err);
      outEl.textContent = (stdout ? stdout + "\n" : "") + msg;
      outEl.classList.add("err");
      const missing = detectMissingPackage(msg);
      if (missing) {
        statusEl.textContent = "Missing package: " + missing;
        const btn = document.createElement("button");
        btn.className = "play-install";
        btn.textContent = "Install " + (PIP_NAMES[missing] || missing);
        btn.addEventListener("click", async () => {
          btn.disabled = true;
          await tryInstall(py, missing, statusEl);
          btn.remove();
        });
        installSlot.appendChild(btn);
      } else {
        statusEl.textContent = "Error.";
      }
    }
  }

  // -------------------- Single ```python block widget --------------------

  async function makeBlockWidget(code) {
    const wrap = document.createElement("div");
    wrap.className = "play-wrap";

    const host = document.createElement("div");
    host.className = "play-monaco-host";
    const lines = Math.max(5, code.split("\n").length);
    host.style.height = Math.min(lines * 19 + 18, 460) + "px";
    wrap.appendChild(host);

    const toolbar = makeToolbar();
    wrap.appendChild(toolbar.bar);

    const out = document.createElement("pre");
    out.className = "play-output";
    out.textContent = "Output will appear here.";
    wrap.appendChild(out);

    const handle = await makeMonaco(host, code);
    const original = code;

    toolbar.runBtn.addEventListener("click", () => {
      toolbar.runBtn.disabled = true;
      runPython(handle.editor.getValue(), out, toolbar.status, toolbar.installSlot, false)
        .finally(() => (toolbar.runBtn.disabled = false));
    });
    toolbar.resetBtn.addEventListener("click", () => {
      if (!confirm("Discard your edits?")) return;
      handle.editor.setValue(original);
      out.textContent = "Output will appear here.";
      out.classList.remove("err");
      toolbar.status.textContent = "";
      toolbar.installSlot.innerHTML = "";
    });
    handle.editor.addCommand(
      window.monaco.KeyMod.CtrlCmd | window.monaco.KeyCode.Enter,
      () => toolbar.runBtn.click()
    );
    return wrap;
  }

  function makeToolbar() {
    const bar = document.createElement("div");
    bar.className = "play-toolbar";

    const runBtn = document.createElement("button");
    runBtn.className = "play-run";
    runBtn.innerHTML = '<span class="play-run-ic">▶</span> Run';

    const resetBtn = document.createElement("button");
    resetBtn.className = "play-reset";
    resetBtn.textContent = "Reset";

    const status = document.createElement("span");
    status.className = "play-status";

    const installSlot = document.createElement("span");
    installSlot.className = "play-install-slot";

    const kb = document.createElement("span");
    kb.className = "play-kbhint";
    kb.innerHTML = "<kbd>Ctrl</kbd>+<kbd>Enter</kbd>";

    bar.append(runBtn, resetBtn, kb, installSlot, status);
    return { bar, runBtn, resetBtn, status, installSlot };
  }

  // True if `code` looks like it touches the filesystem.
  function usesFileIO(code) {
    return /\bopen\s*\(|\bread_csv|\bread_excel|\bread_json|\bread_parquet|\bread_pickle|\bload\s*\(\s*["']|\bos\.path|pathlib/.test(
      code
    );
  }

  function buildFileToolbar() {
    const wrap = document.createElement("div");
    wrap.className = "play-file-toolbar";

    const note = document.createElement("div");
    note.className = "play-file-note";
    note.innerHTML =
      "<strong>📂 This page uses files.</strong> The browser doesn't see your computer's filesystem. " +
      "Click <strong>📎 Upload file</strong> below to load a file into Python's virtual disk, " +
      "then read it with <code>open(\"yourfile.csv\")</code> or <code>pd.read_csv(\"yourfile.csv\")</code> " +
      "(use just the filename — no path).";
    wrap.appendChild(note);

    const row = document.createElement("div");
    row.className = "play-top-toolbar";

    const uploadBtn = document.createElement("button");
    uploadBtn.className = "play-reset";
    uploadBtn.textContent = "📎 Upload file";
    const uploadInput = document.createElement("input");
    uploadInput.type = "file";
    uploadInput.multiple = true;
    uploadInput.style.display = "none";
    uploadBtn.addEventListener("click", () => uploadInput.click());

    const list = document.createElement("span");
    list.className = "play-upload-list";

    uploadInput.addEventListener("change", async (e) => {
      const py = await ensurePyodide(null);
      const cwd = "/home/pyodide";
      try { py.FS.mkdirTree(cwd); } catch {}
      for (const f of e.target.files) {
        const buf = new Uint8Array(await f.arrayBuffer());
        py.FS.writeFile(cwd + "/" + f.name, buf);
        const chip = document.createElement("span");
        chip.className = "play-upload-chip";
        chip.textContent = "📄 " + f.name;
        chip.title = 'Available as open("' + f.name + '")';
        list.appendChild(chip);
      }
      e.target.value = "";
    });

    row.appendChild(uploadBtn);
    row.appendChild(uploadInput);
    row.appendChild(list);
    wrap.appendChild(row);
    return wrap;
  }

  async function enhanceCodeBlocks(rootEl) {
    if (!rootEl) return;
    const pyCodes = rootEl.querySelectorAll("pre code.language-python");
    const sqlCodes = rootEl.querySelectorAll("pre code.language-sql");
    const sheetCodes = rootEl.querySelectorAll("pre code.language-sheet, pre code.language-excel");

    if (pyCodes.length > 0) {
      // If any python block does file I/O, inject a single file-toolbar before
      // the first python block on this page.
      let needsFiles = false;
      pyCodes.forEach((c) => {
        if (usesFileIO(c.textContent)) needsFiles = true;
      });
      if (needsFiles && !rootEl.querySelector(".play-file-toolbar")) {
        const firstPre = pyCodes[0].parentElement;
        if (firstPre && firstPre.parentNode) {
          firstPre.parentNode.insertBefore(buildFileToolbar(), firstPre);
        }
      }

      for (const codeEl of pyCodes) {
        const pre = codeEl.parentElement;
        if (!pre || pre.dataset.playEnhanced) continue;
        pre.dataset.playEnhanced = "1";
        const code = codeEl.textContent.replace(/\n$/, "");
        const placeholder = document.createElement("div");
        placeholder.className = "play-loading";
        placeholder.textContent = "Loading editor…";
        pre.replaceWith(placeholder);
        makeBlockWidget(code).then((wrap) => placeholder.replaceWith(wrap));
      }
    }

    if (sqlCodes.length > 0) {
      // Each page gets a fresh in-memory SQLite. Setup block (first sql block
      // whose first line is `-- 📦 SETUP`) is auto-run and read-only; all other
      // sql blocks share that DB.
      const pageDb = makePageDb();
      let setupSeen = false;
      for (const codeEl of sqlCodes) {
        const pre = codeEl.parentElement;
        if (!pre || pre.dataset.playEnhanced) continue;
        pre.dataset.playEnhanced = "1";
        const code = codeEl.textContent.replace(/\n$/, "");
        const isSetup = !setupSeen && /^\s*--\s*📦\s*SETUP/.test(code);
        if (isSetup) setupSeen = true;
        const placeholder = document.createElement("div");
        placeholder.className = "play-loading";
        placeholder.textContent = "Loading editor…";
        pre.replaceWith(placeholder);
        makeSqlBlockWidget(code, pageDb, { isSetup }).then((wrap) =>
          placeholder.replaceWith(wrap)
        );
      }
    }

    if (sheetCodes.length > 0) {
      for (const codeEl of sheetCodes) {
        const pre = codeEl.parentElement;
        if (!pre || pre.dataset.playEnhanced) continue;
        pre.dataset.playEnhanced = "1";
        const rawSpec = codeEl.textContent.replace(/\n$/, "");
        const placeholder = document.createElement("div");
        placeholder.className = "play-loading";
        placeholder.textContent = "Loading spreadsheet…";
        pre.replaceWith(placeholder);
        makeSheetBlockWidget(rawSpec).then(async (wrap) => {
          placeholder.replaceWith(wrap);
          // wrap is now in DOM; safe to mount x-spreadsheet (offsetWidth is real).
          if (typeof wrap.__mount === "function") await wrap.__mount();
        }).catch((err) => {
          placeholder.textContent = "Spreadsheet error: " + (err.message || err);
        });
      }
    }
  }

  // -------------------- Cell-based exercise UI --------------------

  // Parse a .py exercise into cells:
  //   { docstring, setup, cells: [{hint, code}], trailing }
  function parseExercise(src) {
    const lines = src.split("\n");
    let i = 0;

    // Capture leading triple-quoted docstring (if any) for header text.
    let docstring = "";
    if (
      lines[i] &&
      (lines[i].startsWith('"""') || lines[i].startsWith("'''"))
    ) {
      const quote = lines[i].slice(0, 3);
      const buf = [lines[i].slice(3)];
      i++;
      while (i < lines.length && !lines[i].includes(quote)) {
        buf.push(lines[i]);
        i++;
      }
      if (i < lines.length) {
        const idx = lines[i].indexOf(quote);
        buf.push(lines[i].slice(0, idx));
        i++;
      }
      docstring = buf.join("\n").trim();
    }

    // Skip blank lines after docstring.
    while (i < lines.length && lines[i].trim() === "") i++;

    // Read setup: everything up to first "# 🛠️" line.
    const setupLines = [];
    while (i < lines.length && !/^#\s*🛠️/.test(lines[i])) {
      setupLines.push(lines[i]);
      i++;
    }
    const setup = setupLines.join("\n").trim();

    // Read cells: each starts with "# 🛠️" (and trailing comment lines),
    // then (optional) blank/code lines until the next "# 🛠️".
    const cells = [];
    while (i < lines.length) {
      if (!/^#\s*🛠️/.test(lines[i])) {
        i++;
        continue;
      }
      // Hint = first "# 🛠️" line + following "#" comment lines until blank
      // line, code line, or another "# 🛠️" marker.
      const hintBuf = [];
      let first = true;
      while (i < lines.length && /^#/.test(lines[i])) {
        if (!first && /^#\s*🛠️/.test(lines[i])) break;
        hintBuf.push(lines[i].replace(/^#\s?/, ""));
        i++;
        first = false;
      }
      // Body = lines until next "# 🛠️" or EOF (trim trailing blanks).
      const bodyBuf = [];
      while (i < lines.length && !/^#\s*🛠️/.test(lines[i])) {
        bodyBuf.push(lines[i]);
        i++;
      }
      // Strip leading + trailing blank lines from body.
      while (bodyBuf.length && bodyBuf[0].trim() === "") bodyBuf.shift();
      while (bodyBuf.length && bodyBuf[bodyBuf.length - 1].trim() === "")
        bodyBuf.pop();
      cells.push({
        hint: hintBuf.join("\n").trim(),
        code: bodyBuf.join("\n"),
      });
    }
    return { docstring, setup, cells };
  }

  async function makeCellEditor(host, code) {
    const handle = await makeMonaco(host, code, { readOnly: false });
    return handle;
  }

  async function makeReadonlyEditor(host, code) {
    return await makeMonaco(host, code, { readOnly: true });
  }

  function autoSize(host, code, minLines) {
    const lines = Math.max(minLines || 3, code.split("\n").length);
    host.style.height = Math.min(lines * 19 + 18, 320) + "px";
  }

  function escapeHtml(s) {
    return String(s).replace(
      /[&<>"']/g,
      (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c])
    );
  }

  function renderHint(hintText) {
    // Hint is markdown-ish. Use marked if available.
    const div = document.createElement("div");
    div.className = "play-hint";
    if (window.marked) {
      div.innerHTML = window.marked.parse(hintText);
    } else {
      div.textContent = hintText;
    }
    return div;
  }

  // Convert "ex09_margin_table.py" -> "Exercise 9 — Margin Table".
  function humanizeFilename(filename) {
    let stem = filename.replace(/\.py$/, "");
    const m = stem.match(/^ex(\d+)_(.+)$/);
    if (m) {
      const n = parseInt(m[1], 10);
      const rest = m[2]
        .replace(/_/g, " ")
        .replace(/\b\w/g, (c) => c.toUpperCase());
      return "Exercise " + n + " — " + rest;
    }
    return stem.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
  }

  function isFilenameLine(s) {
    return /^ex\d+_.*\.py$/i.test(s.trim()) || /^[a-z0-9_-]+\.py$/i.test(s.trim());
  }

  function detectDifficulty(line) {
    // Match "Difficulty: Easy" or "🟢 Easy" / "🟡 Medium" / "🔴 Hard" (with optional surrounding text).
    const m1 = line.match(/^\s*Difficulty:\s*(Easy|Medium|Hard)\s*$/i);
    if (m1) return m1[1];
    const m2 = line.match(/^\s*(?:🟢|🟡|🔴)\s*(Easy|Medium|Hard)\s*$/i);
    if (m2) return m2[1];
    return null;
  }

  // Bold "Key:" lines and force paragraph break between them so the
  // Concepts / Lesson / Goal / Difficulty rows don't merge into one <p>.
  function formatDocstring(body) {
    const lines = body.split("\n");
    const out = [];
    let inFence = false;
    const KEY_RE = /^(\S[^:\n]{0,60}):(\s+.*)?$/;
    for (let i = 0; i < lines.length; i++) {
      const l = lines[i];
      if (/^\s*```/.test(l)) {
        inFence = !inFence;
        out.push(l);
        continue;
      }
      if (inFence) {
        out.push(l);
        continue;
      }
      const m = l.match(KEY_RE);
      const isUrl = /^[a-z][a-z0-9+.-]*:\/\//i.test(l);
      const isIndented = /^\s{2,}/.test(l);
      if (m && !isUrl && !isIndented) {
        // Force paragraph break before this line.
        if (out.length && out[out.length - 1].trim() !== "") out.push("");
        const key = m[1];
        const value = (m[2] || "").trim();
        let v = value;
        const md = value.match(/^([\w\-./]+\.md)\s*$/);
        if (md) v = "[" + md[1] + "](" + md[1] + ")";
        out.push("**" + key + ":** " + v);
      } else {
        out.push(l);
      }
    }
    return out.join("\n");
  }

  // Wrap "Expected output:" (and similar) tables in fenced code blocks so
  // monospace alignment is preserved through markdown.
  function fenceExpectedBlocks(body) {
    const lines = body.split("\n");
    const out = [];
    let i = 0;
    while (i < lines.length) {
      const l = lines[i];
      // Match "Expected output", "Expected final state", "Expected:", etc.
      // Header may end with optional "(...)" and a colon.
      if (/^Expected[^:]*:\s*$/i.test(l)) {
        out.push(l);
        i++;
        // Skip leading blank.
        while (i < lines.length && lines[i].trim() === "") {
          out.push(lines[i]);
          i++;
        }
        // Collect block: lines until two consecutive blanks or EOF.
        const blockLines = [];
        while (i < lines.length) {
          const cur = lines[i];
          const next = lines[i + 1];
          if (cur.trim() === "" && (next === undefined || next.trim() === "")) {
            break;
          }
          // Stop on a new section header.
          if (/^[A-Z][\w ]{0,30}:\s*$/.test(cur)) break;
          blockLines.push(cur);
          i++;
        }
        // Trim trailing blank lines from block.
        while (blockLines.length && blockLines[blockLines.length - 1].trim() === "")
          blockLines.pop();
        if (blockLines.length) {
          out.push("```");
          blockLines.forEach((b) => out.push(b));
          out.push("```");
        }
      } else {
        out.push(l);
        i++;
      }
    }
    return out.join("\n");
  }

  async function mountFullEditor(container, path, code) {
    container.innerHTML = "";

    const filename = path.split("/").pop();
    const parsed = parseExercise(code);

    // Walk docstring: pull title (first non-empty line that isn't a filename or
    // a difficulty marker) and pull difficulty if present.
    let title = humanizeFilename(filename);
    let difficulty = null;
    let titleFromDocstring = false;
    const bodyLines = [];

    if (parsed.docstring) {
      const lines = parsed.docstring.split("\n");
      let i = 0;
      while (i < lines.length && lines[i].trim() === "") i++;

      // Optionally consume the first line as title.
      while (i < lines.length) {
        const t = lines[i].trim();
        if (t === "") { i++; continue; }
        if (isFilenameLine(t)) { i++; continue; } // skip filename
        const d = detectDifficulty(t);
        if (d) { difficulty = d; i++; continue; } // skip difficulty marker
        if (!titleFromDocstring) {
          title = t.replace(/\.$/, "");
          titleFromDocstring = true;
          i++;
          continue;
        }
        break;
      }

      // Remaining lines = body, but still strip difficulty markers we missed.
      while (i < lines.length) {
        const d = detectDifficulty(lines[i]);
        if (d) { if (!difficulty) difficulty = d; }
        else bodyLines.push(lines[i]);
        i++;
      }
    }

    const body = formatDocstring(fenceExpectedBlocks(bodyLines.join("\n").trim()));

    const header = document.createElement("h1");
    header.textContent = title;
    header.style.marginTop = "0";
    header.style.marginBottom = "4px";
    container.appendChild(header);

    const subtitle = document.createElement("div");
    subtitle.className = "play-subtitle";
    let subHtml = '<code>' + filename + '</code>';
    if (difficulty) {
      const d = difficulty.toLowerCase();
      const emoji = d === "easy" ? "🟢" : d === "medium" ? "🟡" : "🔴";
      subHtml +=
        ' <span class="diff-pill ' + d + '">' + emoji + " " + difficulty + "</span>";
    }
    subtitle.innerHTML = subHtml;
    container.appendChild(subtitle);

    if (body) {
      const ds = document.createElement("div");
      ds.className = "play-docstring";
      if (window.marked) {
        ds.innerHTML = window.marked.parse(body, { breaks: true });
      } else {
        ds.textContent = body;
      }
      container.appendChild(ds);
    }

    const banner = document.createElement("div");
    banner.className = "play-banner";
    banner.innerHTML =
      "Each step has its own editor. Fill in the code, click <strong>▶ Run</strong> on that cell. " +
      "Cells share Python state — variables you set in one carry over. " +
      "Use <strong>Reset session</strong> to start fresh.";
    container.appendChild(banner);

    // File-handling note + upload button.
    const fileNote = document.createElement("div");
    fileNote.className = "play-file-note";
    fileNote.innerHTML =
      "<strong>📂 Working with files?</strong> The browser doesn't see your computer's filesystem. " +
      "If an exercise needs a CSV / xlsx, click <strong>📎 Upload file</strong> below — " +
      "it loads into Python's virtual disk and you can read it with " +
      "<code>open(\"yourfile.csv\")</code> or <code>pd.read_csv(\"yourfile.csv\")</code> " +
      "(use just the filename, no path). " +
      "Many exercises avoid files entirely by using an in-memory string with <code>io.StringIO</code> — " +
      "no upload needed.";
    container.appendChild(fileNote);

    // Top-level toolbar with reset-session + upload.
    const top = document.createElement("div");
    top.className = "play-top-toolbar";

    const resetSession = document.createElement("button");
    resetSession.className = "play-reset";
    resetSession.textContent = "↻ Reset session";
    resetSession.addEventListener("click", async () => {
      const py = await ensurePyodide(null);
      py.runPython("__reset_ns()");
      sharedOut.textContent = "Session reset — variables cleared.";
      sharedOut.classList.remove("err");
    });
    top.appendChild(resetSession);

    // Upload button.
    const uploadBtn = document.createElement("button");
    uploadBtn.className = "play-reset";
    uploadBtn.textContent = "📎 Upload file";
    const uploadInput = document.createElement("input");
    uploadInput.type = "file";
    uploadInput.multiple = true;
    uploadInput.style.display = "none";
    uploadBtn.addEventListener("click", () => uploadInput.click());

    const uploadList = document.createElement("span");
    uploadList.className = "play-upload-list";

    uploadInput.addEventListener("change", async (e) => {
      const py = await ensurePyodide(null);
      const cwd = "/home/pyodide";
      try { py.FS.mkdirTree(cwd); } catch {}
      for (const f of e.target.files) {
        const buf = new Uint8Array(await f.arrayBuffer());
        py.FS.writeFile(cwd + "/" + f.name, buf);
        const chip = document.createElement("span");
        chip.className = "play-upload-chip";
        chip.textContent = "📄 " + f.name;
        chip.title = "Available as open(\"" + f.name + "\")";
        uploadList.appendChild(chip);
      }
      e.target.value = "";
    });

    top.appendChild(uploadBtn);
    top.appendChild(uploadInput);
    top.appendChild(uploadList);

    // Reveal-solution button (gated).
    const solutionPath = "solutions/" + path;
    const hasSolution =
      window.FILES && Object.prototype.hasOwnProperty.call(window.FILES, solutionPath);
    const revealBtn = document.createElement("button");
    revealBtn.className = "play-reveal";
    revealBtn.textContent = hasSolution
      ? "👁 Reveal solution"
      : "👁 Solution not available yet";
    revealBtn.disabled = !hasSolution;
    if (!hasSolution) revealBtn.title = "No reference solution exists for this exercise.";
    top.appendChild(revealBtn);

    container.appendChild(top);

    // Solution panel (rendered after gated unlock).
    let solutionRevealed = false;
    revealBtn.addEventListener("click", async () => {
      if (solutionRevealed) return;
      const ok1 = confirm(
        "Reveal the solution?\n\n" +
        "Trying and failing teaches you more than reading. " +
        "If you're truly stuck, re-read the lesson, sketch the steps on paper, " +
        "or ask Claude for a hint first."
      );
      if (!ok1) return;
      // Friction: 5-second countdown.
      let n = 5;
      revealBtn.disabled = true;
      const tick = () => {
        if (n > 0) {
          revealBtn.textContent = "👁 Revealing in " + n + "…";
          n--;
          setTimeout(tick, 1000);
        } else {
          showSolution();
        }
      };
      tick();
    });

    async function showSolution() {
      solutionRevealed = true;
      revealBtn.style.display = "none";

      const wrap = document.createElement("div");
      wrap.className = "play-cell play-cell-solution";

      const label = document.createElement("div");
      label.className = "play-cell-label";
      label.textContent = "Reference solution (read-only)";
      wrap.appendChild(label);

      const host = document.createElement("div");
      host.className = "play-monaco-host";
      const code = window.FILES[solutionPath] || "";
      autoSize(host, code, 4);
      wrap.appendChild(host);

      // Insert above the shared output panel at the bottom.
      container.appendChild(wrap);
      makeReadonlyEditor(host, code);
    }

    // Setup cell (read-only).
    if (parsed.setup) {
      const setupBlock = document.createElement("div");
      setupBlock.className = "play-cell play-cell-setup";
      const label = document.createElement("div");
      label.className = "play-cell-label";
      label.textContent = "Setup (read-only)";
      setupBlock.appendChild(label);
      const host = document.createElement("div");
      host.className = "play-monaco-host";
      autoSize(host, parsed.setup, 2);
      setupBlock.appendChild(host);
      container.appendChild(setupBlock);
      makeReadonlyEditor(host, parsed.setup);

      // Auto-run setup once Pyodide ready.
      ensurePyodide(null).then(async (py) => {
        const ns = py.globals.get("__user_ns__");
        try {
          await py.runPythonAsync(parsed.setup, { globals: ns });
        } catch {}
      });
    }

    // Per-step cells.
    parsed.cells.forEach((cell, idx) => {
      const cellEl = document.createElement("div");
      cellEl.className = "play-cell";

      cellEl.appendChild(renderHint(cell.hint));

      const host = document.createElement("div");
      host.className = "play-monaco-host";
      const initial = cell.code || "# write your code here\n";
      autoSize(host, initial, 3);
      cellEl.appendChild(host);

      const tb = makeToolbar();
      tb.bar.classList.add("play-cell-toolbar");
      cellEl.appendChild(tb.bar);

      const out = document.createElement("pre");
      out.className = "play-output play-cell-output";
      out.textContent = "(not run yet)";
      cellEl.appendChild(out);

      container.appendChild(cellEl);

      makeCellEditor(host, initial).then((handle) => {
        tb.runBtn.addEventListener("click", () => {
          tb.runBtn.disabled = true;
          runPython(
            handle.editor.getValue(),
            out,
            tb.status,
            tb.installSlot,
            true
          ).finally(() => (tb.runBtn.disabled = false));
        });
        tb.resetBtn.addEventListener("click", () => {
          if (!confirm("Discard edits in this cell?")) return;
          handle.editor.setValue(initial);
          out.textContent = "(not run yet)";
          out.classList.remove("err");
          tb.status.textContent = "";
          tb.installSlot.innerHTML = "";
        });
        handle.editor.addCommand(
          window.monaco.KeyMod.CtrlCmd | window.monaco.KeyCode.Enter,
          () => tb.runBtn.click()
        );
      });
    });

    // Shared output panel at bottom (used by reset-session feedback).
    const sharedOut = document.createElement("pre");
    sharedOut.className = "play-output play-shared-output";
    sharedOut.style.display = "block";
    sharedOut.textContent = "";
    container.appendChild(sharedOut);

    // Pre-load Pyodide so squigglies + first run feel snappy.
    ensurePyodide(null).catch(() => {});
  }

  // -------------------- SQL runner (sql.js / SQLite WASM) --------------------

  const SQLJS_URL = "https://cdn.jsdelivr.net/npm/sql.js@1.10.3/dist/";
  let sqlReadyPromise = null;

  function ensureSqlJs() {
    if (sqlReadyPromise) return sqlReadyPromise;
    sqlReadyPromise = (async () => {
      await loadScript(SQLJS_URL + "sql-wasm.js");
      const SQL = await window.initSqlJs({
        locateFile: (f) => SQLJS_URL + f,
      });
      return SQL;
    })();
    return sqlReadyPromise;
  }

  // Each call returns a lazy handle that opens a fresh in-memory DB on first
  // use. We share the handle across all sql blocks on a single page so a
  // SETUP block in block 1 is visible to block 2.
  function makePageDb() {
    let dbPromise = null;
    return {
      get() {
        if (!dbPromise) {
          dbPromise = ensureSqlJs().then((SQL) => new SQL.Database());
        }
        return dbPromise;
      },
      async reset() {
        const SQL = await ensureSqlJs();
        const old = dbPromise ? await dbPromise : null;
        if (old) {
          try { old.close(); } catch {}
        }
        dbPromise = Promise.resolve(new SQL.Database());
        return dbPromise;
      },
    };
  }

  function commonSqlOptions(readOnly) {
    return Object.assign(commonOptions(readOnly), { language: "sql" });
  }

  async function makeMonacoSql(host, code, opts) {
    opts = opts || {};
    const monaco = await ensureMonaco();
    const editor = monaco.editor.create(
      host,
      Object.assign(commonSqlOptions(opts.readOnly), { value: code })
    );
    const model = editor.getModel();
    const handle = { editor, model, monaco, relint: () => {} };
    editors.add(handle);
    return handle;
  }

  function renderSqlResult(outEl, results, modified, elapsedMs) {
    outEl.innerHTML = "";
    outEl.classList.remove("err");
    if (!results || results.length === 0) {
      const note = document.createElement("div");
      note.className = "sql-empty";
      note.textContent =
        "OK — " +
        (modified > 0 ? modified + " row(s) affected" : "no rows returned") +
        " (" + elapsedMs.toFixed(1) + " ms)";
      outEl.appendChild(note);
      return;
    }
    // Render only the LAST result set (most useful when running setup + query).
    const last = results[results.length - 1];
    const cols = last.columns || [];
    const rows = last.values || [];

    const meta = document.createElement("div");
    meta.className = "sql-meta";
    const shown = Math.min(rows.length, 200);
    meta.textContent =
      rows.length + " row" + (rows.length === 1 ? "" : "s") +
      " · " + cols.length + " col" + (cols.length === 1 ? "" : "s") +
      " · " + elapsedMs.toFixed(1) + " ms" +
      (rows.length > shown ? " (showing first " + shown + ")" : "");
    outEl.appendChild(meta);

    const tableWrap = document.createElement("div");
    tableWrap.className = "sql-table-wrap";
    const table = document.createElement("table");
    table.className = "sql-table";
    const thead = document.createElement("thead");
    const htr = document.createElement("tr");
    cols.forEach((c) => {
      const th = document.createElement("th");
      th.textContent = c;
      htr.appendChild(th);
    });
    thead.appendChild(htr);
    table.appendChild(thead);
    const tbody = document.createElement("tbody");
    for (let i = 0; i < shown; i++) {
      const tr = document.createElement("tr");
      rows[i].forEach((v) => {
        const td = document.createElement("td");
        td.textContent = v === null ? "NULL" : String(v);
        if (v === null) td.classList.add("sql-null");
        else if (typeof v === "number") td.classList.add("sql-num");
        tr.appendChild(td);
      });
      tbody.appendChild(tr);
    }
    table.appendChild(tbody);
    tableWrap.appendChild(table);
    outEl.appendChild(tableWrap);
  }

  async function runSql(sql, pageDb, outEl, statusEl) {
    outEl.classList.remove("err");
    outEl.textContent = "";
    statusEl.textContent = "Loading SQLite…";
    try {
      const db = await pageDb.get();
      statusEl.textContent = "Running…";
      const t0 = performance.now();
      const results = db.exec(sql);
      const elapsed = performance.now() - t0;
      const modified = db.getRowsModified();
      renderSqlResult(outEl, results, modified, elapsed);
      statusEl.textContent = "Done.";
    } catch (err) {
      outEl.textContent = String(err.message || err);
      outEl.classList.add("err");
      statusEl.textContent = "Error.";
    }
  }

  function makeSqlToolbar(extra) {
    const bar = document.createElement("div");
    bar.className = "play-toolbar";

    const runBtn = document.createElement("button");
    runBtn.className = "play-run";
    runBtn.innerHTML = '<span class="play-run-ic">▶</span> Run';

    const resetBtn = document.createElement("button");
    resetBtn.className = "play-reset";
    resetBtn.textContent = "Reset";

    const status = document.createElement("span");
    status.className = "play-status";

    const kb = document.createElement("span");
    kb.className = "play-kbhint";
    kb.innerHTML = "<kbd>Ctrl</kbd>+<kbd>Enter</kbd>";

    bar.append(runBtn, resetBtn);
    if (extra && extra.length) extra.forEach((e) => bar.appendChild(e));
    bar.append(kb, status);
    return { bar, runBtn, resetBtn, status };
  }

  async function makeSqlBlockWidget(code, pageDb, opts) {
    opts = opts || {};
    const wrap = document.createElement("div");
    wrap.className = "play-wrap play-sql-wrap" + (opts.isSetup ? " play-sql-setup" : "");

    if (opts.isSetup) {
      const label = document.createElement("div");
      label.className = "play-cell-label";
      label.textContent = "📦 Setup (read-only, auto-run on first query)";
      wrap.appendChild(label);
    }

    const host = document.createElement("div");
    host.className = "play-monaco-host";
    const lines = Math.max(5, code.split("\n").length);
    host.style.height = Math.min(lines * 19 + 18, 460) + "px";
    wrap.appendChild(host);

    const toolbar = makeSqlToolbar();
    wrap.appendChild(toolbar.bar);

    const out = document.createElement("div");
    out.className = "play-output sql-output";
    out.textContent = opts.isSetup
      ? "Setup will run automatically the first time you run a query below."
      : "Output will appear here.";
    wrap.appendChild(out);

    const handle = await makeMonacoSql(host, code, { readOnly: !!opts.isSetup });
    const original = code;

    // For setup blocks: auto-run once, idempotent (DROP IF EXISTS handles re-runs).
    if (opts.isSetup) {
      runSql(code, pageDb, out, toolbar.status).catch(() => {});
      toolbar.runBtn.textContent = "▶ Re-run setup";
      toolbar.runBtn.addEventListener("click", async () => {
        toolbar.runBtn.disabled = true;
        await pageDb.reset();
        await runSql(code, pageDb, out, toolbar.status);
        toolbar.runBtn.disabled = false;
      });
      toolbar.resetBtn.style.display = "none";
    } else {
      toolbar.runBtn.addEventListener("click", () => {
        toolbar.runBtn.disabled = true;
        runSql(handle.editor.getValue(), pageDb, out, toolbar.status)
          .finally(() => (toolbar.runBtn.disabled = false));
      });
      toolbar.resetBtn.addEventListener("click", () => {
        if (!confirm("Discard your edits?")) return;
        handle.editor.setValue(original);
        out.textContent = "Output will appear here.";
        out.classList.remove("err");
        toolbar.status.textContent = "";
      });
      handle.editor.addCommand(
        window.monaco.KeyMod.CtrlCmd | window.monaco.KeyCode.Enter,
        () => toolbar.runBtn.click()
      );
    }
    return wrap;
  }

  // ---- .sql exercise parser & mount ----

  // SQL exercise format:
  //   /* docstring (title + Concepts/Lesson/Difficulty + Goal + Expected output) */
  //   -- 📦 SETUP   ← optional, until the first "-- 🛠️" marker
  //   <setup sql>
  //   -- 🛠️ Step 1: hint
  //   -- more hint lines starting with --
  //   <sql body>
  //   -- 🛠️ Step 2: ...
  function parseSqlExercise(src) {
    const lines = src.split("\n");
    let i = 0;

    // 1. Block-comment docstring at the very top.
    let docstring = "";
    while (i < lines.length && lines[i].trim() === "") i++;
    if (i < lines.length && lines[i].trim().startsWith("/*")) {
      const buf = [];
      // Strip leading /* on first line.
      buf.push(lines[i].replace(/^\s*\/\*\s?/, ""));
      i++;
      while (i < lines.length && !lines[i].includes("*/")) {
        buf.push(lines[i]);
        i++;
      }
      if (i < lines.length) {
        const idx = lines[i].indexOf("*/");
        buf.push(lines[i].slice(0, idx));
        i++;
      }
      docstring = buf.join("\n").trim();
    }
    while (i < lines.length && lines[i].trim() === "") i++;

    // 2. Setup: everything up to the first "-- 🛠️" line.
    const setupLines = [];
    while (i < lines.length && !/^\s*--\s*🛠️/.test(lines[i])) {
      setupLines.push(lines[i]);
      i++;
    }
    const setup = setupLines.join("\n").trim();

    // 3. Cells.
    const cells = [];
    while (i < lines.length) {
      if (!/^\s*--\s*🛠️/.test(lines[i])) {
        i++;
        continue;
      }
      const hintBuf = [];
      let first = true;
      while (i < lines.length && /^\s*--/.test(lines[i])) {
        if (!first && /^\s*--\s*🛠️/.test(lines[i])) break;
        hintBuf.push(lines[i].replace(/^\s*--\s?/, "").replace(/^🛠️\s*/, ""));
        i++;
        first = false;
      }
      const bodyBuf = [];
      while (i < lines.length && !/^\s*--\s*🛠️/.test(lines[i])) {
        bodyBuf.push(lines[i]);
        i++;
      }
      while (bodyBuf.length && bodyBuf[0].trim() === "") bodyBuf.shift();
      while (bodyBuf.length && bodyBuf[bodyBuf.length - 1].trim() === "")
        bodyBuf.pop();
      cells.push({
        hint: hintBuf.join("\n").trim(),
        code: bodyBuf.join("\n"),
      });
    }
    return { docstring, setup, cells };
  }

  async function mountFullSqlEditor(container, path, code) {
    container.innerHTML = "";
    const filename = path.split("/").pop();
    const parsed = parseSqlExercise(code);

    // Pull title + difficulty out of docstring (same shape as Python parser).
    let title = humanizeFilename(filename);
    let difficulty = null;
    let titleFromDoc = false;
    const bodyLines = [];

    if (parsed.docstring) {
      const lines = parsed.docstring.split("\n");
      let j = 0;
      while (j < lines.length && lines[j].trim() === "") j++;
      while (j < lines.length) {
        const t = lines[j].trim();
        if (t === "") { j++; continue; }
        if (isFilenameLine(t)) { j++; continue; }
        const d = detectDifficulty(t);
        if (d) { difficulty = d; j++; continue; }
        if (!titleFromDoc) {
          title = t.replace(/\.$/, "");
          titleFromDoc = true;
          j++;
          continue;
        }
        break;
      }
      while (j < lines.length) {
        const d = detectDifficulty(lines[j]);
        if (d) { if (!difficulty) difficulty = d; }
        else bodyLines.push(lines[j]);
        j++;
      }
    }
    const body = formatDocstring(fenceExpectedBlocks(bodyLines.join("\n").trim()));

    const header = document.createElement("h1");
    header.textContent = title;
    header.style.marginTop = "0";
    header.style.marginBottom = "4px";
    container.appendChild(header);

    const subtitle = document.createElement("div");
    subtitle.className = "play-subtitle";
    let subHtml = '<code>' + filename + '</code>';
    if (difficulty) {
      const d = difficulty.toLowerCase();
      const emoji = d === "easy" ? "🟢" : d === "medium" ? "🟡" : "🔴";
      subHtml += ' <span class="diff-pill ' + d + '">' + emoji + " " + difficulty + "</span>";
    }
    subtitle.innerHTML = subHtml;
    container.appendChild(subtitle);

    if (body) {
      const ds = document.createElement("div");
      ds.className = "play-docstring";
      if (window.marked) {
        ds.innerHTML = window.marked.parse(body, { breaks: true });
      } else {
        ds.textContent = body;
      }
      container.appendChild(ds);
    }

    const banner = document.createElement("div");
    banner.className = "play-banner";
    banner.innerHTML =
      "Every cell runs against the SAME in-browser SQLite database. " +
      "The setup block creates the tables and seeds the data. " +
      "Click <strong>↻ Reset DB</strong> to start over.";
    container.appendChild(banner);

    // Top toolbar — Reset DB + Reveal solution.
    const pageDb = makePageDb();
    const top = document.createElement("div");
    top.className = "play-top-toolbar";

    const resetSession = document.createElement("button");
    resetSession.className = "play-reset";
    resetSession.textContent = "↻ Reset DB";
    resetSession.addEventListener("click", async () => {
      await pageDb.reset();
      if (parsed.setup) {
        await pageDb.get();
        const db = await pageDb.get();
        try { db.exec(parsed.setup); } catch (e) {}
      }
      sharedOut.textContent = "DB reset — seed data re-applied.";
      sharedOut.classList.remove("err");
    });
    top.appendChild(resetSession);

    const solutionPath = "solutions/" + path;
    const hasSolution =
      window.FILES && Object.prototype.hasOwnProperty.call(window.FILES, solutionPath);
    const revealBtn = document.createElement("button");
    revealBtn.className = "play-reveal";
    revealBtn.textContent = hasSolution ? "👁 Reveal solution" : "👁 Solution not available yet";
    revealBtn.disabled = !hasSolution;
    top.appendChild(revealBtn);
    container.appendChild(top);

    let solutionRevealed = false;
    revealBtn.addEventListener("click", async () => {
      if (solutionRevealed) return;
      const ok = confirm(
        "Reveal the solution?\n\n" +
        "Try writing the query yourself first — even a wrong one teaches you " +
        "more than reading the answer."
      );
      if (!ok) return;
      let n = 5;
      revealBtn.disabled = true;
      const tick = () => {
        if (n > 0) {
          revealBtn.textContent = "👁 Revealing in " + n + "…";
          n--;
          setTimeout(tick, 1000);
        } else {
          showSolution();
        }
      };
      tick();
    });

    async function showSolution() {
      solutionRevealed = true;
      revealBtn.style.display = "none";
      const wrap = document.createElement("div");
      wrap.className = "play-cell play-cell-solution";
      const label = document.createElement("div");
      label.className = "play-cell-label";
      label.textContent = "Reference solution (read-only)";
      wrap.appendChild(label);
      const host = document.createElement("div");
      host.className = "play-monaco-host";
      const solCode = window.FILES[solutionPath] || "";
      autoSize(host, solCode, 4);
      wrap.appendChild(host);
      container.appendChild(wrap);
      await makeMonacoSql(host, solCode, { readOnly: true });
    }

    // Setup block (read-only, auto-run).
    if (parsed.setup) {
      const setupBlock = document.createElement("div");
      setupBlock.className = "play-cell play-cell-setup";
      const label = document.createElement("div");
      label.className = "play-cell-label";
      label.textContent = "📦 Setup (read-only, auto-run)";
      setupBlock.appendChild(label);
      const host = document.createElement("div");
      host.className = "play-monaco-host";
      autoSize(host, parsed.setup, 2);
      setupBlock.appendChild(host);
      container.appendChild(setupBlock);
      makeMonacoSql(host, parsed.setup, { readOnly: true });
      // Auto-run setup once sql.js is ready.
      ensureSqlJs().then(async () => {
        const db = await pageDb.get();
        try { db.exec(parsed.setup); } catch (e) {}
      });
    }

    // Per-step cells.
    parsed.cells.forEach((cell) => {
      const cellEl = document.createElement("div");
      cellEl.className = "play-cell";
      cellEl.appendChild(renderHint(cell.hint));

      const host = document.createElement("div");
      host.className = "play-monaco-host";
      const initial = cell.code || "-- write your query here\n";
      autoSize(host, initial, 4);
      cellEl.appendChild(host);

      const tb = makeSqlToolbar();
      tb.bar.classList.add("play-cell-toolbar");
      cellEl.appendChild(tb.bar);

      const out = document.createElement("div");
      out.className = "play-output sql-output play-cell-output";
      out.textContent = "(not run yet)";
      cellEl.appendChild(out);

      container.appendChild(cellEl);

      makeMonacoSql(host, initial, { readOnly: false }).then((handle) => {
        tb.runBtn.addEventListener("click", () => {
          tb.runBtn.disabled = true;
          runSql(handle.editor.getValue(), pageDb, out, tb.status)
            .finally(() => (tb.runBtn.disabled = false));
        });
        tb.resetBtn.addEventListener("click", () => {
          if (!confirm("Discard edits in this cell?")) return;
          handle.editor.setValue(initial);
          out.textContent = "(not run yet)";
          out.classList.remove("err");
          tb.status.textContent = "";
        });
        handle.editor.addCommand(
          window.monaco.KeyMod.CtrlCmd | window.monaco.KeyCode.Enter,
          () => tb.runBtn.click()
        );
      });
    });

    const sharedOut = document.createElement("pre");
    sharedOut.className = "play-output play-shared-output";
    sharedOut.style.display = "block";
    sharedOut.textContent = "";
    container.appendChild(sharedOut);

    // Pre-load sql.js so first run is snappy.
    ensureSqlJs().catch(() => {});
  }

  function applyThemeToEditors() {
    if (!window.monaco) return;
    window.monaco.editor.setTheme(getMonacoTheme());
  }
  const obs = new MutationObserver(applyThemeToEditors);
  obs.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["data-theme"],
  });

  // -------------------- Spreadsheet runner (x-spreadsheet + SheetJS) --------------------

  const XSPREADSHEET_CSS = "https://cdn.jsdelivr.net/npm/x-data-spreadsheet@1.1.9/dist/xspreadsheet.css";
  const XSPREADSHEET_JS  = "https://cdn.jsdelivr.net/npm/x-data-spreadsheet@1.1.9/dist/xspreadsheet.js";
  const SHEETJS_URL      = "https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js";

  let xSpreadsheetReadyPromise = null;
  let sheetJsReadyPromise = null;

  function loadStylesheet(href) {
    return new Promise((resolve) => {
      if (document.querySelector('link[href="' + href + '"]')) { resolve(); return; }
      const link = document.createElement("link");
      link.rel = "stylesheet";
      link.href = href;
      link.onload = resolve;
      link.onerror = resolve; // non-fatal if CDN unreachable
      document.head.appendChild(link);
    });
  }

  function ensureXSpreadsheet() {
    if (xSpreadsheetReadyPromise) return xSpreadsheetReadyPromise;
    xSpreadsheetReadyPromise = (async () => {
      await loadStylesheet(XSPREADSHEET_CSS);
      await loadScript(XSPREADSHEET_JS);
      return window.x_spreadsheet || (window.Spreadsheet && (window.Spreadsheet.default || window.Spreadsheet));
    })();
    return xSpreadsheetReadyPromise;
  }

  function ensureSheetJS() {
    if (sheetJsReadyPromise) return sheetJsReadyPromise;
    sheetJsReadyPromise = (async () => {
      await loadScript(SHEETJS_URL);
      return window.XLSX;
    })();
    return sheetJsReadyPromise;
  }

  // Convert a SheetJS workbook sheet to x-spreadsheet's "stox" data shape.
  function sheetjsToXspreadsheet(wb, sheetName) {
    const XLSX = window.XLSX;
    const ws = wb.Sheets[sheetName];
    if (!ws) return null;
    const range = XLSX.utils.decode_range(ws["!ref"] || "A1:A1");
    const rows = {};
    for (let R = range.s.r; R <= range.e.r; R++) {
      const cells = {};
      for (let C = range.s.c; C <= range.e.c; C++) {
        const addr = XLSX.utils.encode_cell({ r: R, c: C });
        const cell = ws[addr];
        if (!cell) continue;
        let text;
        if (cell.f) text = "=" + cell.f;
        else if (cell.w !== undefined) text = cell.w;
        else if (cell.v !== undefined) text = String(cell.v);
        else text = "";
        cells[C] = { text };
      }
      rows[R] = { cells };
    }
    return [{ name: sheetName, rows }];
  }

  // Parse a ```sheet or ```excel block body.
  // Returns { src, sheet, height, tsvLines }
  function parseSheetSpec(raw) {
    const spec = { src: null, sheet: null, height: 540, tsvLines: [] };
    const lines = raw.split("\n");
    let pastDivider = false;
    for (const line of lines) {
      if (line.trim() === "---") { pastDivider = true; continue; }
      if (pastDivider) { spec.tsvLines.push(line); continue; }
      const m = line.match(/^(\w+)\s*:\s*(.+)$/);
      if (!m) continue;
      const [, key, val] = m;
      if (key === "src")    spec.src    = val.trim();
      if (key === "sheet")  spec.sheet  = val.trim();
      if (key === "height") spec.height = parseInt(val, 10) || 540;
    }
    return spec;
  }

  // Decode a base64 string to Uint8Array (works without atob for large strings too).
  function b64ToUint8Array(b64) {
    const binary = atob(b64);
    const bytes = new Uint8Array(binary.length);
    for (let i = 0; i < binary.length; i++) bytes[i] = binary.charCodeAt(i);
    return bytes;
  }

  // Inject sheet wrap styles once into the document head.
  // x-spreadsheet ships its own grid styles; these are just for the surrounding chrome.
  function ensureSheetStyles() {
    if (document.getElementById("play-sheet-styles")) return;
    const style = document.createElement("style");
    style.id = "play-sheet-styles";
    style.textContent = `
.play-sheet-wrap { font-family: -apple-system, "Segoe UI", sans-serif; font-size: 13px; margin: 12px 0; color: #1f2328; }
.play-sheet-host { width: 100%; min-height: 360px; border: 1px solid #d8dee4; border-top: 0; overflow: hidden; color: #1f2328; background: #fff; }
[data-theme="dark"] .play-sheet-host { border-color: #30363d; color: #e6edf3; background: #fff; }
.play-sheet-wrap .play-toolbar { display: flex; align-items: center; gap: 8px; padding: 6px 10px; background: #fafbfc; border: 1px solid #d8dee4; border-bottom: 0; }
[data-theme="dark"] .play-sheet-wrap .play-toolbar { background: #161b22; border-color: #30363d; }
/* Force strong contrast inside x-spreadsheet — its defaults inherit page colors and read faded on this site. */
.play-sheet-host .x-spreadsheet-editor-area textarea,
.play-sheet-host .x-spreadsheet-editor-area input,
.play-sheet-host .x-spreadsheet-suggest,
.play-sheet-host .x-spreadsheet-toolbar-btn,
.play-sheet-host .x-spreadsheet-bottombar,
.play-sheet-host .x-spreadsheet-color-palette {
  color: #1f2328 !important;
  font-weight: 500;
  background: #fff !important;
}
.play-sheet-host .x-spreadsheet-editor-area { z-index: 10; }
.play-sheet-host .x-spreadsheet-overlayer .x-spreadsheet-editor textarea {
  color: #1f2328 !important;
  background: #fff !important;
  font-size: 14px;
  font-weight: 600;
  caret-color: #0969da;
}
/* Tip ribbon shown above the sheet to teach the no-click-during-edit workflow. */
.play-sheet-tip {
  display: flex; align-items: center; gap: 8px;
  padding: 6px 10px;
  background: #fff8c5; border: 1px solid #d4a72c; border-bottom: 0;
  color: #4d3800; font-size: 12px;
}
[data-theme="dark"] .play-sheet-tip { background: #4d3800; border-color: #d4a72c; color: #f0d77c; }
    `.trim();
    document.head.appendChild(style);
  }

  // Build a wrap with an x-spreadsheet inside, loaded with a workbook from `spec`.
  // Returns the wrap immediately; the wrap exposes wrap.__mount() which performs
  // the heavy XS instantiation AFTER the wrap is in the DOM (so offsetWidth is real).
  async function makeSheetBlockWidget(rawSpec) {
    const spec = parseSheetSpec(rawSpec);
    ensureSheetStyles();

    // Load both libraries in parallel — fast on warm cache.
    const [XS_ctor] = await Promise.all([ensureXSpreadsheet(), ensureSheetJS()]);
    const XLSX = window.XLSX;
    const XS = XS_ctor || window.x_spreadsheet;

    const wrap = document.createElement("div");
    wrap.className = "play-wrap play-sheet-wrap";

    // Tip ribbon — explains the formula-edit workflow.
    const tip = document.createElement("div");
    tip.className = "play-sheet-tip";
    tip.innerHTML = "<span>💡</span><span><strong>Tip:</strong> While editing a formula, type cell references like <code>C2:C7</code> directly — clicking another cell will exit edit mode. Press <kbd>Enter</kbd> to commit, <kbd>F2</kbd> to re-enter edit.</span>";
    wrap.appendChild(tip);

    // Toolbar (download + status)
    const toolbar = document.createElement("div");
    toolbar.className = "play-toolbar sheet-toolbar";
    const dlBtn = document.createElement("button");
    dlBtn.className = "play-reset";
    dlBtn.textContent = "Download .xlsx";
    const statusEl = document.createElement("span");
    statusEl.className = "play-status";
    statusEl.style.marginLeft = "12px";
    toolbar.append(dlBtn, statusEl);
    wrap.appendChild(toolbar);

    // Host div for x-spreadsheet
    const host = document.createElement("div");
    host.className = "play-sheet-host";
    host.style.height = (spec.height || 540) + "px";
    wrap.appendChild(host);

    // Lock page scroll while pointer is over the sheet — otherwise
    // wheel scroll inside x-spreadsheet bubbles up and scrolls the page.
    host.addEventListener("mouseenter", () => {
      document.body.dataset.prevOverflow = document.body.style.overflow || "";
      document.body.style.overflow = "hidden";
    });
    host.addEventListener("mouseleave", () => {
      document.body.style.overflow = document.body.dataset.prevOverflow || "";
      delete document.body.dataset.prevOverflow;
    });
    // Belt-and-braces: stop wheel events from bubbling past the host.
    host.addEventListener(
      "wheel",
      (e) => {
        e.stopPropagation();
      },
      { passive: true }
    );

    let wb = null;
    let xs = null;

    function renderXs(sheetName) {
      const xsData = sheetjsToXspreadsheet(wb, sheetName);
      if (!xsData) {
        statusEl.textContent = "Sheet \"" + sheetName + "\" not found.";
        return;
      }
      if (xs) {
        xs.loadData(xsData);
      } else {
        xs = XS(host, {
          mode: "edit",
          showToolbar: true,
          showGrid: true,
          showContextmenu: true,
          view: {
            height: () => spec.height || 540,
            width:  () => host.offsetWidth || host.clientWidth || (host.parentElement && host.parentElement.offsetWidth) || 800,
          },
          row: { len: Math.max(60, (xsData[0].rows && Object.keys(xsData[0].rows).length + 10) || 60), height: 28 },
          col: { len: 26, width: 110, indexWidth: 50, minWidth: 60 },
        });
        xs.loadData(xsData);
      }
    }

    async function loadFromSrc(srcPath) {
      statusEl.textContent = "Loading workbook…";
      try {
        const jsonKey = srcPath.endsWith(".xlsx.json") ? srcPath : srcPath.replace(/\.xlsx$/, ".xlsx.json");
        const raw = window.FILES && window.FILES[jsonKey];
        let parsed;
        if (raw) {
          parsed = JSON.parse(raw);
        } else {
          const res = await fetch(jsonKey);
          if (!res.ok) throw new Error("HTTP " + res.status + " for " + jsonKey);
          parsed = await res.json();
        }
        const bytes = b64ToUint8Array(parsed.data);
        wb = XLSX.read(bytes, { type: "array" });
        const targetSheet = spec.sheet || wb.SheetNames[0];
        renderXs(targetSheet);
        statusEl.textContent = "";
      } catch (err) {
        statusEl.textContent = "Error: " + (err.message || err);
      }
    }

    function loadFromTsv(lines) {
      wb = XLSX.utils.book_new();
      const rows = lines.map((line) => line.split("\t"));
      const ws = XLSX.utils.aoa_to_sheet(rows);
      XLSX.utils.book_append_sheet(wb, ws, "Sheet1");
      renderXs("Sheet1");
    }

    dlBtn.addEventListener("click", () => {
      if (!wb) { statusEl.textContent = "Nothing to download."; return; }
      try {
        const buf = XLSX.write(wb, { type: "array", bookType: "xlsx" });
        const blob = new Blob([buf], { type: "application/octet-stream" });
        const url = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        const filename = spec.src
          ? spec.src.split("/").pop().replace(/\.json$/, "").replace(/\.xlsx\.xlsx$/, ".xlsx")
          : "sheet.xlsx";
        a.download = filename;
        a.click();
        URL.revokeObjectURL(url);
      } catch (err) {
        statusEl.textContent = "Download failed: " + (err.message || err);
      }
    });

    // Deferred mount — call after wrap is in DOM so host.offsetWidth is real.
    wrap.__mount = async function mount() {
      if (spec.src) {
        await loadFromSrc(spec.src);
      } else if (spec.tsvLines.length > 0) {
        loadFromTsv(spec.tsvLines);
      } else {
        statusEl.textContent = "No src or inline data provided.";
      }
      // Re-measure once layout has settled — x-spreadsheet sometimes mis-sizes on first render.
      requestAnimationFrame(() => {
        if (xs && typeof xs.reRender === "function") xs.reRender();
      });
      // Also re-render on container resize.
      if (typeof ResizeObserver !== "undefined") {
        const ro = new ResizeObserver(() => {
          if (xs && typeof xs.reRender === "function") xs.reRender();
        });
        ro.observe(host);
      }
    };

    return wrap;
  }

  // -------------------- Markdown editor (used by Notes panel) --------------------

  async function createMarkdownEditor(host, value, opts) {
    opts = opts || {};
    const monaco = await ensureMonaco();
    const editor = monaco.editor.create(host, {
      value: value || "",
      language: "markdown",
      theme: getMonacoTheme(),
      fontSize: 13.5,
      fontFamily:
        'ui-monospace, "SF Mono", Menlo, Consolas, "DejaVu Sans Mono", monospace',
      minimap: { enabled: false },
      scrollBeyondLastLine: false,
      automaticLayout: true,
      tabSize: 2,
      insertSpaces: true,
      wordWrap: "on",
      lineNumbers: "on",
      lineNumbersMinChars: 3,
      padding: { top: 10, bottom: 10 },
      renderLineHighlight: "line",
      bracketPairColorization: { enabled: false },
    });
    if (opts.onChange) {
      editor.onDidChangeModelContent(() => opts.onChange(editor.getValue()));
    }
    if (opts.onCursor) {
      editor.onDidChangeCursorPosition((e) => opts.onCursor(e.position));
      opts.onCursor(editor.getPosition());
    }
    return editor;
  }

  window.Playground = {
    enhanceCodeBlocks,
    mountFullEditor,
    mountFullSqlEditor,
    ensurePyodide,
    ensureSqlJs,
    ensureSheetJS,
    createMarkdownEditor,
  };
})();
