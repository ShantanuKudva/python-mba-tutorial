# Phase 7 — Capstone: Excel Insights (Weeks 13–14)

The capstone takes everything from weeks 1–12 and packages it into a real web app.

> 📦 **Heads-up — local install required for this phase.** Phases 1–5 run entirely in the browser. The capstone needs a real Python + Node.js environment because it deploys a backend (FastAPI) and frontend (Next.js). Treat this phase as your transition from "playground learner" to "shipping engineer". The [00-setup](../00-setup/README.md) page has the optional local-install steps.

## What you ship

A web page where a user can:

1. Upload an `.xlsx` file (drag-and-drop).
2. Pick a domain: Finance / Marketing / Operations / Strategy.
3. See computed metrics + a chart.
4. Read an AI-written executive summary.
5. Download a polished `.xlsx` report.

End to end. Live URL at the end of week 14.

## Architecture

```
   ┌─────────────────────┐                ┌────────────────────────┐
   │  Frontend (Next.js) │  HTTP / JSON   │  Backend (FastAPI)     │
   │  + shadcn/ui        │ ─────────────► │  (you build this)      │
   │  (already built)    │ ◄───────────── │                        │
   └─────────────────────┘                │  ─ /upload             │
                                          │  ─ /analyze            │
                                          │  ─ /summarize  → Groq  │
                                          │  ─ /report             │
                                          └────────────────────────┘
```

You **do not** touch the frontend (except styling tweaks if you want). It already calls all four endpoints and renders the responses.

You **do** build the backend. Every endpoint starts as a stub returning mock data so the frontend works on day 1. Your job is to progressively replace each stub with the real pandas/Groq logic you wrote in weeks 6–12.

## Folder map

| Folder | What's there | Who owns it |
|---|---|---|
| [`backend/`](backend/) | FastAPI app with stubbed routes + pipeline modules | **You build** |
| [`frontend/`](frontend/) | Next.js + shadcn/ui — fully working | Pre-built |

## Getting started

1. Open [`backend/README.md`](backend/README.md) — install deps, run dev server.
2. Open [`frontend/README.md`](frontend/README.md) — install Node deps, run dev server.
3. Open both URLs side-by-side. Upload a sample workbook. Watch it round-trip with mock data.
4. Replace one mock at a time with real logic. Test each before moving on.

## Two-week plan

| Week | Focus |
|---|---|
| 13 | Wire `/upload` and `/analyze` — get real metrics flowing. |
| 14 | Wire `/summarize` (Groq) and `/report` (xlsx generation). Deploy. |

## Done when

- Visiting the deployed URL → uploading a sample workbook → getting metrics + AI summary + download all works.
- You recorded a 60-second demo video.
- Marked the capstone page complete in this workspace.

---

## Extension menu (for your portfolio / MBA project pitch)

The same architecture (Upload → Analyze → Summarize → Report) plugs into many real problems. Each adds one new `pipelines/<topic>.py` and one new domain option in [`DomainPicker.tsx`](frontend/components/DomainPicker.tsx). Pick one as a project pitch.

| Use case | Difficulty | Pitch |
|---|---|---|
| **Financial red-flag screener** | Beginner | Upload P&L + balance sheet for 50 Nifty 500 firms. Surface receivables-vs-revenue spikes, hidden leverage, profit-without-cash anomalies. |
| **Consulting intern automator** | Intermediate | Market-size any sector ("EV chargers in India") with TAM/SAM/SOM, assumptions table, and McKinsey-style one-pager. |
| **Resume screener for HR** | Beginner | Upload JD criteria + resume text. AI scores, ranks, explains. Pitch to your placement cell. |
| **SME cash-flow tracker** | Beginner | Daily entries → weekly projections → simple risk flags. Interview 3 real business owners — that's primary research too. |
| **Equity research agent** | Advanced | Ticker → fetched financials + news → ratios + sentiment → structured research note. Compare to a real analyst report. |
| **MIS report automator** | Intermediate | ERP data dumps → auto-clean, auto-pivot, auto-chart. Reuses the polished xlsx output flow. |
| **Job application tracker** | Beginner | Paste JD + resume. Score fit, suggest resume edits, track application status per company. |
| **Competitor price tracker** | Beginner | Weekly prices in. AI summarizes trends + suggests positioning. |
| **News sentiment tracker** | Intermediate | Daily news for a company/sector → sentiment score trend over time. |
| **TDS / tax helper** | Intermediate | Income + deductions + investments → tax liability + missed deductions + summary PDF. |

### How to extend (the recipe)

1. Add `backend/pipelines/<your_topic>.py` with `def run(xlsx_path) -> dict[str, Any]:` returning `{metrics, headline}`.
2. Add the new key to `PIPELINES` in [`backend/routers/analyze.py`](backend/routers/analyze.py).
3. Add the new option to [`frontend/components/DomainPicker.tsx`](frontend/components/DomainPicker.tsx) and the `Domain` type in [`frontend/lib/api.ts`](frontend/lib/api.ts).
4. Optional: add a stat-extraction case to [`frontend/lib/derive.ts`](frontend/lib/derive.ts).
5. Tune the LLM prompt in [`backend/llm/groq_client.py`](backend/llm/groq_client.py) for the new domain.

The frontend, upload flow, error handling, theme, and report download are reusable as-is.

> 🎯 Frame any of these as a problem you solved, not a course you completed. "I screened 50 Nifty 500 companies and found 3 patterns" beats any certificate.
