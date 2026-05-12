# Week 12 Project — "Explain This Dataset" CLI

## What you're building

A command-line tool that:

1. Takes any `.xlsx` file path as input.
2. Detects which sheets and columns it has.
3. Computes a domain-aware summary (totals, top items, time trends).
4. Sends the summary to Groq.
5. Prints a 5-bullet executive summary.

## Required structure

```python
def detect_columns(df) -> dict:                    # heuristic: which col is date, amount, category
def summarize_dataframe(df) -> str:                # text block to feed the LLM
def call_groq(summary: str, focus: str) -> str:   # wraps the API call
def main(): ...
```

## Run

```bash
python 06-ai-integration/explain.py datasets/finance/sample_pl.xlsx --focus "financial health"
```

Output should look like:

```
═══════════════════════════════════════════
  EXPLAIN: sample_pl.xlsx
═══════════════════════════════════════════

Computed summary:
  - 24 rows across 4 columns
  - Date range: 2025-01-01 → 2026-04-30
  - Total amount: $3,450,000
  - Top category: Operating Expenses (38%)

LLM Summary (model=llama-3.3-70b-versatile):
  • Revenue concentration in Q4 suggests seasonality...
  • Gross margin compressed by 2pts vs prior year...
  ...
```

## File to create

`06-ai-integration/explain.py`

## Done when

- The script runs end-to-end on at least 2 different sample workbooks.
- It handles missing API key (prints a clear message, doesn't crash).
- The summary is sent in a way that respects token limits (truncate or sample if needed).
- You committed.

🛠️ Stretch: cache the LLM response keyed by a hash of the input data, so re-running on the same file doesn't re-call Groq.
