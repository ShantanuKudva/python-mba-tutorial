# Python + MBA Roadmap — 12-Week Plan

A comprehensive, hands-on learning workspace combining **Python programming**, **MBA analytics**, and a **capstone web app**. Built for a learner with zero coding background, ramping up to shipping a real Excel-analysis tool.

- **Pace:** 12 weeks · ~6–8 hrs/week
- **Stack:** Python · pandas · Streamlit (early) → FastAPI + Next.js (capstone)
- **AI:** Groq free tier (Llama 3.x / Mixtral)
- **MBA domains:** Finance · Marketing · Operations · Strategy

---

## How this repo is organized

```
python-excel-mba/
├── ROADMAP.md                  ← this file (master plan)
├── README.md                   ← quickstart, install, daily workflow
├── 00-setup/                   ← install Python, VSCode, git, venv
├── 01-foundations/             ← weeks 1–3: Python core
├── 02-data-with-pandas/        ← weeks 4–5: Excel + pandas
├── 03-mba-analytics/           ← weeks 6–9: domain-specific projects
│   ├── finance/
│   ├── marketing/
│   ├── operations/
│   └── strategy/
├── 04-ai-integration/          ← week 10: Groq API basics
├── 05-capstone-app/            ← weeks 11–12: full-stack analyzer
│   ├── backend/                ← FastAPI (LEARNER FILLS IN)
│   └── frontend/               ← Next.js (PRE-BUILT)
├── datasets/                   ← sample Excel/CSV files per domain
├── notebooks/                  ← scratch space, Jupyter
└── solutions/                  ← reference answers (peek only after attempt)
```

Each weekly folder contains:

- `README.md` — concepts, why-it-matters, MBA tie-in
- `lessons/` — short walkthroughs
- `exercises/` — graded practice
- `project.md` — mini-project spec

---

## Week-by-week

### Phase 1 — Foundations (Weeks 1–3)

**Week 1 — Setup + Python basics**

- Install [Python 3.12](https://www.python.org/downloads/), [VSCode](https://code.visualstudio.com/docs/python/python-tutorial), [git](https://git-scm.com/doc). [Virtual envs (`venv`)](https://docs.python.org/3/library/venv.html).
- [Variables & types](https://docs.python.org/3/tutorial/introduction.html), [strings](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str), [numbers](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex), [booleans](https://docs.python.org/3/library/stdtypes.html#truth-value-testing).
- [`if/elif/else`](https://docs.python.org/3/tutorial/controlflow.html#if-statements), [comparison ops](https://docs.python.org/3/library/stdtypes.html#comparisons), [logical ops (`and`/`or`/`not`)](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not).
- **MBA tie-in:** Convert a manual Excel calc (e.g., simple interest) into Python. Reference: [Investopedia — Simple Interest](https://www.investopedia.com/terms/s/simple_interest.asp).
- Mini-project: CLI calculator for [break-even point](https://corporatefinanceinstitute.com/resources/accounting/break-even-analysis/).

**Week 2 — Collections + control flow**

- [Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists), [dicts](https://docs.python.org/3/tutorial/datastructures.html#dictionaries), [tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences), [sets](https://docs.python.org/3/tutorial/datastructures.html#sets).
- [`for`](https://docs.python.org/3/tutorial/controlflow.html#for-statements), [`while`](https://docs.python.org/3/reference/compound_stmts.html#while), [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions).
- [Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions), parameters, [return](https://docs.python.org/3/reference/simple_stmts.html#the-return-statement), [scope (LEGB)](https://realpython.com/python-scope-legb-rule/).
- **MBA tie-in:** Iterate over list of products → compute [gross margin](https://corporatefinanceinstitute.com/resources/accounting/gross-margin/) per row.
- Mini-project: Inventory [reorder-flag](https://corporatefinanceinstitute.com/resources/management/reorder-point/) script (pure Python, no pandas yet).

**Week 3 — Files, errors, modules**

- [File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files), [CSV via stdlib](https://docs.python.org/3/library/csv.html).
- [`try/except`](https://docs.python.org/3/tutorial/errors.html#handling-exceptions), [built-in exceptions](https://docs.python.org/3/library/exceptions.html).
- [Imports / modules](https://docs.python.org/3/tutorial/modules.html), [`pip install`](https://pip.pypa.io/en/stable/cli/pip_install/), [`requirements.txt`](https://pip.pypa.io/en/stable/reference/requirements-file-format/).
- Reading documentation — [How to read Python docs](https://realpython.com/python-documentation-online/).
- **MBA tie-in:** Parse CSV of monthly sales → output totals.
- Mini-project: Expense-categorizer reads CSV, outputs summary.

### Phase 2 — Data with pandas (Weeks 4–5)

**Week 4 — pandas fundamentals**

- [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html), [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html), [indexing with `loc`/`iloc`](https://pandas.pydata.org/docs/user_guide/indexing.html).
- [Read Excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html) (via [openpyxl](https://openpyxl.readthedocs.io/)), [write Excel](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html).
- [Filter / boolean indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#boolean-indexing), [sort](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html), [sample](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html), [describe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html).
- [Missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) (`NaN`, `fillna`, `dropna`).
- **Project:** Clean messy P&L workbook → standardized DataFrame. Reference: [P&L statement explained](https://corporatefinanceinstitute.com/resources/accounting/profit-and-loss-statement-pl/).

**Week 5 — Aggregations + plotting**

- [`groupby`](https://pandas.pydata.org/docs/user_guide/groupby.html), [pivot tables](https://pandas.pydata.org/docs/user_guide/reshaping.html#pivot-tables), [merge / join](https://pandas.pydata.org/docs/user_guide/merging.html).
- [Date handling](https://pandas.pydata.org/docs/user_guide/timeseries.html), [resampling](https://pandas.pydata.org/docs/user_guide/timeseries.html#resampling).
- [matplotlib pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html), [pandas built-in plotting](https://pandas.pydata.org/docs/user_guide/visualization.html).
- **Project:** Multi-sheet workbook → consolidated dashboard image.

### Phase 3 — MBA analytics (Weeks 6–9)

Each week = one domain, one dataset, one deliverable.

**Week 6 — Finance**

- Ratio analysis: [liquidity](https://corporatefinanceinstitute.com/resources/accounting/liquidity-ratio/), [leverage](https://corporatefinanceinstitute.com/resources/accounting/leverage-ratios/), [profitability](https://corporatefinanceinstitute.com/resources/accounting/profitability-ratios/). Cheat sheet: [Investopedia ratios](https://www.investopedia.com/financial-ratios-4689817).
- [DCF model](https://corporatefinanceinstitute.com/resources/financial-modeling/dcf-model-training-free-guide/) in pandas. Theory: [Damodaran on valuation](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures/valintro.html).
- [NPV](https://numpy.org/numpy-financial/latest/npv.html) / [IRR](https://numpy.org/numpy-financial/latest/irr.html) via [`numpy-financial`](https://numpy.org/numpy-financial/).
- **Project:** Auto-generate 1-page financial-health report from raw P&L + balance-sheet Excel.

**Week 7 — Marketing/Sales**

- [Cohort retention analysis](https://mode.com/blog/cohort-analysis-tutorial), [funnel conversion](https://amplitude.com/explore/analytics/funnel-analysis-guide).
- [RFM segmentation tutorial (Kaggle)](https://www.kaggle.com/code/regivm/rfm-analysis-tutorial). Background: [RFM model — Optimove](https://www.optimove.com/resources/learning-center/rfm-segmentation).
- A/B test → [`scipy.stats.ttest_ind`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html). Concept: [StatQuest — t-test](https://www.youtube.com/watch?v=pTmLQvMM-1M).
- **Project:** Customer-segmentation script → Excel with segment labels + chart.

**Week 8 — Operations**

- Inventory: [EOQ](https://corporatefinanceinstitute.com/resources/management/economic-order-quantity-eoq/), [safety stock](https://www.investopedia.com/terms/s/safety-stock.asp), [reorder point](https://corporatefinanceinstitute.com/resources/management/reorder-point/).
- Time-series forecasting: [moving average (`Series.rolling`)](https://pandas.pydata.org/docs/user_guide/window.html), [exponential smoothing (`statsmodels` ETS)](https://www.statsmodels.org/stable/examples/notebooks/generated/exponential_smoothing.html). Free book: [Forecasting: Principles and Practice (Hyndman)](https://otexts.com/fpp3/).
- **Project:** 12-month demand forecast workbook with confidence band.

**Week 9 — Strategy/Consulting**

- [KPI design (KPI.org)](https://kpi.org/KPI-Basics), [market sizing — TAM/SAM/SOM](https://corporatefinanceinstitute.com/resources/management/total-addressable-market-tam/).
- [Sensitivity analysis](https://corporatefinanceinstitute.com/resources/financial-modeling/what-is-sensitivity-analysis/), [scenario analysis](https://corporatefinanceinstitute.com/resources/financial-modeling/scenario-analysis/) in pandas.
- [Tornado chart in matplotlib](https://matplotlib.org/stable/gallery/lines_bars_and_markers/horizontal_barchart_distribution.html), [Plotly bar examples](https://plotly.com/python/bar-charts/).
- **Project:** Scenario model (best/base/worst) exported as formatted Excel.

### Phase 4 — AI integration (Week 10)

**Week 10 — Groq API**

- [Groq API keys](https://console.groq.com/keys), env vars, [`python-dotenv`](https://github.com/theskumar/python-dotenv).
- HTTP basics: [MDN — HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview), [`requests` quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/), [`httpx`](https://www.python-httpx.org/).
- [Groq Python SDK](https://github.com/groq/groq-python), [chat completions reference](https://console.groq.com/docs/api-reference#chat).
- Prompt patterns: [Prompting Guide — techniques](https://www.promptingguide.ai/techniques), [Anthropic prompt engineering overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview).
- [Groq rate limits](https://console.groq.com/docs/rate-limits), [model pricing](https://groq.com/pricing/).
- **Project:** "Explain this dataset" — pass DataFrame summary to Groq, get plain-English insights.

### Phase 5 — Capstone (Weeks 11–12)

**The app:** _Excel Insights_ — upload an Excel file, pick a domain (finance/marketing/ops/strategy), get analysis + AI summary + downloadable report.

**Pre-built (frontend, Next.js):**

- Upload UI, domain selector, results panel, download button.
- Calls backend endpoints; learner does NOT touch this except styling tweaks.

**Learner builds (backend, FastAPI):**

- `POST /upload` — accept xlsx, return file ID.
- `POST /analyze` — run domain pipeline, return JSON metrics + chart URLs.
- `POST /summarize` — call Groq with metrics, return narrative.
- `GET /report/{id}` — return generated xlsx.

**Week 11 — Backend wiring**

- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/), [path operations](https://fastapi.tiangolo.com/tutorial/first-steps/), [request body via pydantic](https://fastapi.tiangolo.com/tutorial/body/). [pydantic v2 docs](https://docs.pydantic.dev/latest/).
- [File uploads](https://fastapi.tiangolo.com/tutorial/request-files/), [Python `tempfile`](https://docs.python.org/3/library/tempfile.html).
- Reuse pandas pipelines from weeks 6–9.

**Week 12 — Polish + ship**

- [FastAPI CORS](https://fastapi.tiangolo.com/tutorial/cors/), [error handling](https://fastapi.tiangolo.com/tutorial/handling-errors/).
- Connect Groq endpoint (reuse Week 10 client).
- Deploy: [Railway docs](https://docs.railway.com/), [Render — Python service](https://render.com/docs/deploy-fastapi). Frontend: [Vercel — Next.js](https://vercel.com/docs/frameworks/nextjs).
- Record demo video — [OBS Studio (free)](https://obsproject.com/) or [Loom free tier](https://www.loom.com/).

---

## Use cases the capstone covers

1. Upload sales workbook → cohort + RFM segments + AI exec summary.
2. Upload P&L → ratio dashboard + AI commentary on weak areas.
3. Upload demand history → forecast + reorder recommendations.
4. Upload scenario inputs → tornado chart + AI strategic options memo.

---

## Learning principles

- **Type code, don't copy.** Muscle memory matters.
- **Break things on purpose.** Errors are the curriculum.
- **One concept → one Excel parallel.** Always tie to something you'd otherwise do manually.
- **AI as tutor, not author.** Use Claude / ChatGPT to explain errors; do not paste assignment solutions.
- **Commit daily.** `git commit -m "week 2 day 3"` even if ugly.

---

## Docs & source links

Curated, all free. Organized to match the weekly phases — bookmark these, you will return often.

### Setup & tooling (Week 1)

- Python official docs — https://docs.python.org/3/
- Python tutorial (official) — https://docs.python.org/3/tutorial/
- VSCode Python setup — https://code.visualstudio.com/docs/python/python-tutorial
- Virtual environments (`venv`) — https://docs.python.org/3/library/venv.html
- pip user guide — https://pip.pypa.io/en/stable/user_guide/
- Git docs — https://git-scm.com/doc
- Pro Git book (free) — https://git-scm.com/book/en/v2

### Python core (Weeks 1–3)

- *Automate the Boring Stuff with Python* (free online) — https://automatetheboringstuff.com/
- Real Python tutorials — https://realpython.com/
- Python standard library reference — https://docs.python.org/3/library/index.html
- `csv` module — https://docs.python.org/3/library/csv.html
- Errors and exceptions — https://docs.python.org/3/tutorial/errors.html

### pandas + Excel (Weeks 4–5)

- pandas user guide — https://pandas.pydata.org/docs/user_guide/index.html
- 10 minutes to pandas — https://pandas.pydata.org/docs/user_guide/10min.html
- Kaggle "Pandas" micro-course — https://www.kaggle.com/learn/pandas
- pandas Excel I/O — https://pandas.pydata.org/docs/user_guide/io.html#excel-files
- openpyxl docs — https://openpyxl.readthedocs.io/
- matplotlib tutorials — https://matplotlib.org/stable/tutorials/index.html
- Jupyter docs — https://docs.jupyter.org/

### Finance (Week 6)

- `numpy-financial` — https://numpy.org/numpy-financial/
- Corporate Finance Institute free resources — https://corporatefinanceinstitute.com/resources/
- Investopedia ratio library — https://www.investopedia.com/financial-ratios-4689817
- Damodaran Online (valuation, free) — https://pages.stern.nyu.edu/~adamodar/

### Marketing/Sales analytics (Week 7)

- `scipy.stats` — https://docs.scipy.org/doc/scipy/reference/stats.html
- Cohort analysis primer (Mode) — https://mode.com/blog/cohort-analysis-tutorial
- RFM segmentation walkthrough — https://www.kaggle.com/code/regivm/rfm-analysis-tutorial

### Operations / forecasting (Week 8)

- statsmodels user guide — https://www.statsmodels.org/stable/user-guide.html
- Forecasting: Principles and Practice (Hyndman, free book) — https://otexts.com/fpp3/
- EOQ / inventory primer — https://corporatefinanceinstitute.com/resources/management/economic-order-quantity-eoq/

### Strategy / scenario modeling (Week 9)

- McKinsey "Three horizons" + scenario writing — https://www.mckinsey.com/featured-insights
- Plotly tornado/sensitivity examples — https://plotly.com/python/

### Stats foundations (cross-cutting)

- StatQuest YouTube — https://www.youtube.com/@statquest
- Khan Academy statistics — https://www.khanacademy.org/math/statistics-probability

### AI / Groq (Week 10)

- Groq console + docs — https://console.groq.com/docs
- Groq Python SDK — https://github.com/groq/groq-python
- `python-dotenv` — https://github.com/theskumar/python-dotenv
- `httpx` — https://www.python-httpx.org/
- `requests` quickstart — https://requests.readthedocs.io/en/latest/user/quickstart/
- Prompt engineering guide (free) — https://www.promptingguide.ai/

### Capstone — backend (Weeks 11–12)

- FastAPI tutorial — https://fastapi.tiangolo.com/tutorial/
- FastAPI file uploads — https://fastapi.tiangolo.com/tutorial/request-files/
- pydantic v2 docs — https://docs.pydantic.dev/latest/
- Uvicorn — https://www.uvicorn.org/

### Capstone — frontend (pre-built, reference only)

- Next.js docs — https://nextjs.org/docs
- React docs — https://react.dev/learn
- Tailwind CSS — https://tailwindcss.com/docs

### Deployment

- Railway docs — https://docs.railway.com/
- Render docs — https://render.com/docs
- Vercel (Next.js host) — https://vercel.com/docs

### Bonus — alternate frontend if Next.js feels heavy

- Streamlit docs — https://docs.streamlit.io/
- Streamlit gallery — https://streamlit.io/gallery

---

## What "done" looks like

By end of week 12, learner can:

- Read any Excel file into pandas, clean it, analyze it.
- Write a function library reusable across workbooks.
- Build a small web API that wraps that library.
- Call an LLM and integrate its output into a workflow.
- Ship a working demo someone non-technical can use.

---

## Next steps to scaffold this repo

1. `00-setup/` — write install guide for macOS + Windows.
2. `01-foundations/week-1/` — first lesson + 5 exercises + solution stubs.
3. `datasets/` — seed 4 sample workbooks (one per MBA domain).
4. `05-capstone-app/frontend/` — Next.js scaffold with mocked API.
5. `README.md` — top-level quickstart pointing into Week 1.

Order of build: setup → week 1 → datasets → capstone frontend skeleton → fill weeks 2–12 progressively.
