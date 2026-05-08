# Week 6 Project — 1-Page Financial Health Report

## What you're building

A script that reads the P&L + balance sheet and produces a single Excel file with:

- **Sheet "Ratios"** — ratio name | value | benchmark | status
- **Sheet "Score"** — composite health score + verdict + key drivers
- **Sheet "Raw"** — copy of the source P&L and balance sheet for traceability

## Required functions (in `03-mba-analytics/finance/health.py`)

```python
def load_statements(pl_path, bs_path) -> tuple[dict, dict]: ...
def all_ratios(pl, bs) -> dict[str, float]: ...
def benchmark(name, value) -> str:    # "Strong" / "OK" / "Weak"
    ...
def health_score(ratios) -> tuple[float, str]:    # (score, verdict)
    ...
def write_report(pl, bs, ratios, score, verdict, out_path) -> None: ...
```

Plus `main()` and the `__name__` guard.

## Output

`health_report.xlsx` next to the script.

## Done when

- The Ratios sheet shows all 6 ratios with proper formatting.
- The Score sheet shows the composite + verdict + at least 3 driver bullets.
- The script handles missing line items gracefully (skip + log warning, don't crash).
- You committed.

🛠️ Stretch: also produce `health_report.png` — a 2×3 grid of bar gauges, one per ratio, comparing actual vs. benchmark.
