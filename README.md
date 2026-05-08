# Python + MBA Workspace

Welcome. This repository is a self-paced course that takes a complete beginner from "I've never written code" to "I shipped a working web app that analyzes Excel files with AI." It is built specifically for an MBA learner — every Python concept is tied to something you already do (or will do) in spreadsheets.

> **Read [`ROADMAP.md`](ROADMAP.md) first** for the full 12-week plan, philosophy, and resource library.
> This `README.md` is the **navigation map** — how to move through the repo day to day.

---

## 🌐 Browse this repo as a website

Don't want to read raw markdown? There's a self-contained [`index.html`](index.html) at the repo root that renders every doc as a clean, navigable web page (sidebar + breadcrumbs + syntax-highlighted code).

### How to open it

**Just double-click `index.html`.** It opens in your browser and works.

No server, no install, no build step. All the markdown is bundled into [`site_data.js`](site_data.js) so it loads directly from `file://`.

### After editing markdown (or pulling new content)

If you (or someone else) added or edited any `.md` file, regenerate the bundle once:

```bash
python build_site.py
```

Then refresh `index.html` in the browser. That's it.

> Why this exists: most browsers block JavaScript `fetch()` from `file://`, which would normally break a static site. The build step pre-bundles all markdown into `site_data.js` so the page never needs to fetch anything from disk at runtime.

---

## Who this is for

- You know Excel reasonably well.
- You have **never** written Python (or any code) before.
- You are studying for an MBA or already in business analytics, finance, marketing, ops, or strategy work.
- You want to *build* something real, not just watch tutorials.

If that's you — you're in the right place.

---

## How the folders work

| Folder | What's inside | When to open it |
|---|---|---|
| [`00-setup/`](00-setup/) | Install Python, VSCode, git. One-time setup. | Before week 1, day 1. |
| [`01-foundations/`](01-foundations/) | Weeks 1–3: pure Python basics. | Weeks 1, 2, 3. |
| [`02-data-with-pandas/`](02-data-with-pandas/) | Weeks 4–5: read/write Excel with pandas. | Weeks 4, 5. |
| [`03-mba-analytics/`](03-mba-analytics/) | Weeks 6–9: one MBA domain per week. | Weeks 6, 7, 8, 9. |
| [`04-ai-integration/`](04-ai-integration/) | Week 10: connect to Groq AI. | Week 10. |
| [`05-capstone-app/`](05-capstone-app/) | Weeks 11–12: full app — frontend done, backend you build. | Weeks 11, 12. |
| [`datasets/`](datasets/) | Sample Excel/CSV files to practice on. | Any time you need data. |
| [`notebooks/`](notebooks/) | Scratch space for experiments. | Whenever curious. |
| [`solutions/`](solutions/) | Reference answers. | **Only after** you've tried. |

Inside each weekly folder you will always find the same four things:

```
week-N/
├── README.md       ← start here. Goals + concepts for the week.
├── lessons/        ← short readings, one concept each.
├── exercises/      ← practice problems. Try, fail, fix, repeat.
└── project.md      ← the mini-project that ties the week together.
```

---

## Daily flow (suggested, ~1 hour/day)

1. **Open the week's `README.md`.** Skim the goals.
2. **Read one lesson** in `lessons/`. Type the examples out — don't copy-paste.
3. **Do one exercise** in `exercises/`. If you get stuck for >15 minutes:
   - Re-read the lesson.
   - Search the linked official docs.
   - Ask an AI to **explain the error**, not solve the problem.
4. **End with a git commit.** Even if ugly. Even if just one line.

```
git add .
git commit -m "week 1 day 2 — done with conditionals exercise"
```

5. **Once a week**, do the project in `project.md`. This is what you'll show off.

---

## Getting unstuck — in this order

When something doesn't work:

1. **Read the error message slowly.** Python's errors are usually honest.
2. **Run a smaller version of the code.** Comment out half of it.
3. **Print everything.** `print(x, type(x))` is your best friend.
4. **Search the exact error.** Stack Overflow, Real Python, official docs.
5. **Ask an AI** (Claude / ChatGPT). Phrase it as:
   > "I'm learning Python. I expected X to happen, but Y happened. Here is my code. Explain the error."
   Don't say "fix it for me." You won't learn that way.
6. Only after all that — peek at `solutions/`.

---

## What you'll be able to do at the end

- Open any messy Excel file and clean it programmatically.
- Build reusable analysis functions for finance, marketing, ops, strategy.
- Run a small web server (FastAPI) that other people can hit.
- Use a free AI API (Groq) to turn numbers into plain-English insight.
- Deploy and share a working URL with classmates / interviewers.

---

## Tools you'll install (week 1)

- **Python 3.12** — the language.
- **VSCode** — the editor.
- **git** — for saving snapshots of your work.
- **Node.js 20+** — only needed for the capstone frontend (week 11).

Step-by-step in [`00-setup/README.md`](00-setup/README.md).

---

## The capstone, in one line

> Upload an Excel file → pick "Finance / Marketing / Ops / Strategy" → get back a chart, the numbers, an AI-written summary, and a polished Excel report you can download.

Frontend (Next.js) is **already built**. You wire up the backend (FastAPI). Everything you learned weeks 1–10 plugs into this. See [`05-capstone-app/README.md`](05-capstone-app/README.md).

---

## Conventions used in this repo

- `📍` = checkpoint — stop here and run something before moving on.
- `🧠` = concept callout — *why* this matters, not just *how*.
- `🛠️` = your turn — code to write yourself.
- `✅` = solution exists in `solutions/` for this exercise.
- File mentions like [`week-1/lessons/01-variables.md`](01-foundations/week-1/lessons/01-variables.md) are clickable in VSCode and GitHub.

---

## Need help mid-course?

- Re-read [`ROADMAP.md`](ROADMAP.md) — the why and how.
- Open [`00-setup/README.md`](00-setup/README.md) if Python or VSCode breaks.
- Skim [`solutions/README.md`](solutions/README.md) for the "peek policy."

You've got this. 12 weeks. One commit at a time.
