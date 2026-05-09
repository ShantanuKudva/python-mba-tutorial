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

### 📝 Personal notes

The sidebar has a **Notes** section. Click `+ Folder` and `+ Note` to build your own markdown notebook — organized in folders, edited in-browser with live preview. Notes are saved to your browser's `localStorage`, so they persist across reloads on the same machine + browser.

Use `Export` to download all notes as one `notes.json` file (back-up or move to another machine), and `Import` to restore. Each note also has a `Download .md` button to save it as a standalone markdown file.

> Notes live in your browser only — they are **not** committed to the repo.

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
| [`00-setup/`](00-setup/) | Optional: local Python install for power users. | Only if you want to run Python outside the browser. |
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
├── exercises/      ← practice problems. Open in the playground → fill in → click ▶ Run.
├── project.md      ← the mini-project that ties the week together.
└── project.py      ← the project as a runnable playground (click ▶ Open project playground).
```

Every lesson ends with a **📚 Resources** section linking to:
- The relevant **official docs** (Python, pandas, scipy, statsmodels, etc.)
- A **deep-dive** read (Real Python, Investopedia, CFI, FPP3)
- **Video tutorials** (curated YouTube searches: Corey Schafer, Keith Galli, freeCodeCamp, etc.)

Use them when the lesson skims a topic you'd like to understand more deeply.

---

## Daily flow (suggested, ~1 hour/day)

1. **Open `index.html`** in your browser (or double-click it). Use the sidebar to navigate.
2. **Read one lesson** — click it in the sidebar. Read through the walkthrough.
3. **Do one exercise** — click the `▶` link next to the exercise name in the sidebar. Edit and run right there.
   If stuck for >15 minutes:
   - Re-read the lesson.
   - Search the linked official docs.
   - Ask an AI to **explain the error**, not solve the problem.
4. **Once a week**, do the project in `project.md`. This is what you'll show off.

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

## How to use this workspace

**Option A — Browser only (recommended to start)**

Double-click `index.html`. Done. Everything opens in your browser — lessons, exercises, runnable code. No install needed. Python runs inside the browser via [Pyodide](https://pyodide.org/).

> If you (or Shantanu) edited any `.md` file, regenerate the bundle once with `python build_site.py`, then refresh.

**Option B — Local Python install (optional, needed for AI + capstone weeks)**

See [`00-setup/README.md`](00-setup/README.md) for the full Python + VSCode + git install guide. Required only for Week 10 (Groq API keys, `.env`) and Weeks 11–12 (FastAPI backend).

---

## The capstone, in one line

> Upload an Excel file → pick "Finance / Marketing / Ops / Strategy" → get back a chart, the numbers, an AI-written summary, and a polished Excel report you can download.

Frontend (Next.js) is **already built**. You wire up the backend (FastAPI). Everything you learned weeks 1–10 plugs into this. See [`05-capstone-app/README.md`](05-capstone-app/README.md).

---

## Conventions used in this repo

- `📍` = checkpoint — stop here and run something before moving on.
- `🧠` = concept callout — *why* this matters, not just *how*.
- `🛠️` = your turn — code to write yourself.
- `📚` = resources — docs / deep-dives / videos at the end of each lesson.
- `✅` = solution exists in `solutions/` for this exercise.

---

## Global reference shelf

Bookmark these — you'll come back to them constantly.

**Python core**
- [Official Python tutorial](https://docs.python.org/3/tutorial/index.html)
- [Python standard library reference](https://docs.python.org/3/library/index.html)
- [Real Python](https://realpython.com/) — best long-form tutorials
- [Corey Schafer — Python tutorials (YouTube)](https://www.youtube.com/@coreyms)

**Data**
- [pandas user guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [matplotlib pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
- [Keith Galli — pandas tutorials (YouTube search)](https://www.youtube.com/results?search_query=keith+galli+pandas)

**MBA analytics**
- [Investopedia](https://www.investopedia.com/) — quick definitions, formulas
- [Corporate Finance Institute](https://corporatefinanceinstitute.com/resources/) — finance deep-dives
- [Forecasting: Principles and Practice (free book)](https://otexts.com/fpp3/)

**AI / LLMs**
- [Groq quickstart](https://console.groq.com/docs/quickstart)
- [Anthropic prompt engineering guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [OpenAI prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [learnprompting.org](https://learnprompting.org/)

---

## Need help mid-course?

- Re-read [`ROADMAP.md`](ROADMAP.md) — the why and how.
- Open [`00-setup/README.md`](00-setup/README.md) if Python or VSCode breaks.
- Skim [`solutions/README.md`](solutions/README.md) for the "peek policy."

You've got this. 12 weeks. One exercise at a time.
