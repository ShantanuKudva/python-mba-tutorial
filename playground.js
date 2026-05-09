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
    const codes = rootEl.querySelectorAll("pre code.language-python");
    if (codes.length === 0) return;

    // If any block does file I/O, inject a single file-toolbar before the first
    // block on this page.
    let needsFiles = false;
    codes.forEach((c) => {
      if (usesFileIO(c.textContent)) needsFiles = true;
    });
    if (needsFiles && !rootEl.querySelector(".play-file-toolbar")) {
      const firstPre = codes[0].parentElement;
      if (firstPre && firstPre.parentNode) {
        firstPre.parentNode.insertBefore(buildFileToolbar(), firstPre);
      }
    }

    for (const codeEl of codes) {
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

  function applyThemeToEditors() {
    if (!window.monaco) return;
    window.monaco.editor.setTheme(getMonacoTheme());
  }
  const obs = new MutationObserver(applyThemeToEditors);
  obs.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["data-theme"],
  });

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
    ensurePyodide,
    createMarkdownEditor,
  };
})();
