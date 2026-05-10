// Progress tracker — localStorage-backed.
// Marks lessons/exercises/projects complete. Renders ✓ chips in sidebar +
// a top-of-sidebar overall progress bar. Works across browser sessions.
//
// Public API:
//   Progress.markComplete(key)
//   Progress.unmark(key)
//   Progress.isComplete(key)
//   Progress.hydrateSidebar()                — paint ✓ chips on links
//   Progress.attachMarkButton(rootEl, key)   — add "Mark complete" button to a page
//   Progress.refreshBar()                    — recompute and render top bar
//   Progress.getStats(prefix?)               — { done, total, pct }
//
// All keys are file paths (e.g. "01-foundations/week-2/exercises/ex09_cart_mutation.py").

(function () {
  const STORAGE_KEY = "progress-v1";

  function load() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch {
      return {};
    }
  }
  function save(data) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
  }

  let state = load();

  function isComplete(key) {
    return !!(state[key] && state[key].completed);
  }
  function markComplete(key) {
    const prevPct = getStats().pct;
    state[key] = Object.assign({}, state[key], {
      completed: true,
      completedAt: Date.now(),
    });
    save(state);
    hydrateSidebar();
    refreshBar();
    const newPct = getStats().pct;
    maybeCelebrate(prevPct, newPct);
  }

  function maybeCelebrate(prev, now) {
    const prevTier = Math.floor(prev / 10);
    const nowTier = Math.floor(now / 10);
    if (nowTier > prevTier && nowTier > 0) {
      showCelebration(nowTier * 10);
    }
  }
  function unmark(key) {
    if (state[key]) {
      delete state[key].completed;
      save(state);
      hydrateSidebar();
      refreshBar();
    }
  }

  function getKeyForLink(a) {
    if (a.dataset && a.dataset.md) return a.dataset.md;
    const href = a.getAttribute("href") || "";
    if (href.startsWith("#play/")) return decodeURIComponent(href.slice(6));
    if (href.startsWith("#")) {
      const path = decodeURIComponent(href.slice(1));
      // Skip notes/ and other route prefixes.
      if (path.startsWith("notes/")) return null;
      if (path.startsWith("play/")) return path.slice(5);
      return path;
    }
    return null;
  }

  function isCountable(key) {
    if (!key) return false;
    // Count lessons, exercises (.py), and projects.
    if (key.endsWith(".md") || key.endsWith(".py")) return true;
    return false;
  }

  function hydrateSidebar() {
    const links = document.querySelectorAll("aside a");
    links.forEach((a) => {
      const key = getKeyForLink(a);
      // Strip any prior chip.
      const old = a.querySelector(".progress-chip");
      if (old) old.remove();
      a.classList.remove("progress-done", "progress-todo");
      if (!key || !isCountable(key)) return;
      const chip = document.createElement("span");
      chip.className = "progress-chip";
      if (isComplete(key)) {
        a.classList.add("progress-done");
        chip.textContent = "✓";
        chip.title = "Completed";
      } else {
        a.classList.add("progress-todo");
        chip.textContent = "○";
        chip.title = "Not yet completed";
      }
      a.appendChild(chip);
    });
  }

  function getStats(prefix) {
    const keys = new Set();
    document.querySelectorAll("aside a").forEach((a) => {
      const k = getKeyForLink(a);
      if (k && isCountable(k)) {
        if (!prefix || k.startsWith(prefix)) keys.add(k);
      }
    });
    let done = 0;
    keys.forEach((k) => {
      if (isComplete(k)) done++;
    });
    const total = keys.size;
    const pct = total ? Math.round((done / total) * 100) : 0;
    return { done, total, pct };
  }

  // ---- Celebration popup (every 10% milestone) ----
  const ENCOURAGE = [
    "Solid start. Keep going.",
    "Quarter way there.",
    "Compound progress beats sprints.",
    "Big chunk done. Brain's wiring up.",
    "Halfway. The hard part is behind you.",
    "More than half. Momentum is real.",
    "Two-thirds. You're now harder to stop than to start.",
    "Most people quit before this. You didn't.",
    "Final stretch.",
    "Last 10%. Go finish it.",
  ];
  function showCelebration(pct) {
    const stats = getStats();
    const overlay = document.createElement("div");
    overlay.className = "celebration-overlay";
    const idx = Math.max(0, Math.min(9, Math.floor(pct / 10) - 1));
    const msg = ENCOURAGE[idx] || "Keep going.";
    overlay.innerHTML =
      '<div class="celebration-confetti"></div>' +
      '<div class="celebration-card">' +
      '<div class="celebration-emoji">🎉</div>' +
      '<h2>' + pct + '% complete!</h2>' +
      '<p>You\'ve finished <strong>' + stats.done + '</strong> of <strong>' +
      stats.total + '</strong> pages.</p>' +
      '<p class="celebration-line">' + msg + '</p>' +
      '<button class="celebration-btn">Keep going →</button>' +
      "</div>";
    document.body.appendChild(overlay);
    // Confetti: scatter 40 emoji pieces with random positions + delays.
    const cf = overlay.querySelector(".celebration-confetti");
    const items = ["🎉", "✨", "🎊", "⭐", "🌟", "💫"];
    for (let i = 0; i < 40; i++) {
      const s = document.createElement("span");
      s.textContent = items[i % items.length];
      s.style.left = Math.random() * 100 + "%";
      s.style.animationDelay = Math.random() * 0.8 + "s";
      s.style.animationDuration = 1.5 + Math.random() * 1.5 + "s";
      s.style.fontSize = 16 + Math.random() * 18 + "px";
      cf.appendChild(s);
    }
    const close = () => overlay.remove();
    overlay.querySelector(".celebration-btn").addEventListener("click", close);
    overlay.addEventListener("click", (e) => { if (e.target === overlay) close(); });
    document.addEventListener("keydown", function esc(e) {
      if (e.key === "Escape") { close(); document.removeEventListener("keydown", esc); }
    });
  }

  function refreshBar() {
    const bar = document.getElementById("progress-bar");
    if (!bar) return;
    const stats = getStats();
    const phase1 = getStats("01-foundations/");
    const phase2 = getStats("02-data-with-pandas/");
    const phase3 = getStats("03-mba-analytics/");
    const phase4 = getStats("04-ai-integration/");
    const phase5 = getStats("05-capstone-app/");

    const fillStyle = "width:" + stats.pct + "%";
    bar.innerHTML =
      '<div class="progress-bar-header">' +
      '<span class="progress-bar-label">Your progress</span>' +
      '<span class="progress-bar-count">' +
      stats.done + " / " + stats.total + " (" + stats.pct + "%)" +
      "</span></div>" +
      '<div class="progress-bar-track"><div class="progress-bar-fill" style="' +
      fillStyle + '"></div></div>' +
      '<div class="progress-bar-phases">' +
      phaseChip("P1", phase1) +
      phaseChip("P2", phase2) +
      phaseChip("P3", phase3) +
      phaseChip("P4", phase4) +
      phaseChip("P5", phase5) +
      "</div>";
  }
  function phaseChip(label, s) {
    if (s.total === 0) return "";
    return (
      '<span class="phase-chip" title="' +
      s.done + "/" + s.total + " in " + label +
      '"><span class="phase-chip-label">' + label +
      '</span><span class="phase-chip-count">' +
      s.done + "/" + s.total + "</span></span>"
    );
  }

  // Walk sidebar in DOM order to find next/prev countable link.
  function getNeighbours(currentKey) {
    const links = Array.from(document.querySelectorAll("aside a"));
    const ordered = [];
    links.forEach((a) => {
      const k = getKeyForLink(a);
      if (k && isCountable(k)) {
        ordered.push({ key: k, label: a.textContent.trim(), el: a });
      }
    });
    const idx = ordered.findIndex((o) => o.key === currentKey);
    return {
      prev: idx > 0 ? ordered[idx - 1] : null,
      next: idx >= 0 && idx < ordered.length - 1 ? ordered[idx + 1] : null,
      idx,
      total: ordered.length,
    };
  }

  function gotoKey(k) {
    if (k.endsWith(".py")) location.hash = "play/" + k;
    else location.hash = k;
  }

  function attachMarkButton(rootEl, key) {
    if (!rootEl || !key) return;
    if (!isCountable(key)) return;
    rootEl.querySelectorAll(".progress-mark-wrap").forEach((b) => b.remove());

    const wrap = document.createElement("div");
    wrap.className = "progress-mark-wrap";

    // Nudge banner — only when not yet complete.
    const nudge = document.createElement("div");
    nudge.className = "mark-nudge";
    nudge.innerHTML =
      '<span class="mark-arrow">↓</span>' +
      '<span>Done with this page? <strong>Mark it complete</strong> to track your progress.</span>' +
      '<span class="mark-arrow">↓</span>';
    wrap.appendChild(nudge);

    const btn = document.createElement("button");
    btn.className = "progress-mark-btn";
    function paint() {
      if (isComplete(key)) {
        btn.classList.add("done");
        btn.innerHTML = "✓ Completed — click to unmark";
        nudge.style.display = "none";
      } else {
        btn.classList.remove("done");
        btn.innerHTML = "Mark as complete";
        nudge.style.display = "";
      }
    }
    paint();
    btn.addEventListener("click", () => {
      if (isComplete(key)) unmark(key);
      else markComplete(key);
      paint();
    });
    wrap.appendChild(btn);

    // Prev / Next nav.
    const nav = document.createElement("div");
    nav.className = "page-nav";
    const { prev, next } = getNeighbours(key);
    if (prev) {
      const p = document.createElement("button");
      p.className = "page-nav-btn page-nav-prev";
      p.innerHTML = "← " + escHtml(prev.label);
      p.title = "Previous: " + prev.label;
      p.addEventListener("click", () => gotoKey(prev.key));
      nav.appendChild(p);
    } else {
      nav.appendChild(document.createElement("span"));
    }
    if (next) {
      const n = document.createElement("button");
      n.className = "page-nav-btn page-nav-next";
      n.innerHTML = "Next: " + escHtml(next.label) + " →";
      n.title = "Next: " + next.label;
      n.addEventListener("click", () => {
        if (!isComplete(key)) {
          if (
            confirm(
              "You haven't marked this page complete yet. Mark it complete and continue?"
            )
          ) {
            markComplete(key);
          }
        }
        gotoKey(next.key);
      });
      nav.appendChild(n);
    } else {
      nav.appendChild(document.createElement("span"));
    }
    wrap.appendChild(nav);

    rootEl.appendChild(wrap);
  }

  function escHtml(s) {
    return String(s).replace(
      /[&<>"']/g,
      (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c])
    );
  }

  // ---- Top scroll-progress bar ----
  function initScrollBar() {
    const bar = document.getElementById("scroll-progress-fill");
    if (!bar) return;
    const update = () => {
      const h = document.documentElement;
      const scrolled = h.scrollTop || document.body.scrollTop;
      const max = (h.scrollHeight || document.body.scrollHeight) - h.clientHeight;
      const pct = max > 0 ? (scrolled / max) * 100 : 0;
      bar.style.width = pct + "%";
    };
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    // Run after layout settles for new content.
    setTimeout(update, 50);
    setTimeout(update, 500);
    update();
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initScrollBar);
  } else {
    initScrollBar();
  }

  // Listen for storage changes from other tabs.
  window.addEventListener("storage", (e) => {
    if (e.key === STORAGE_KEY) {
      state = load();
      hydrateSidebar();
      refreshBar();
    }
  });

  window.Progress = {
    markComplete,
    unmark,
    isComplete,
    hydrateSidebar,
    attachMarkButton,
    refreshBar,
    getStats,
    celebrate: showCelebration, // call window.Progress.celebrate(30) from devtools
  };
})();
