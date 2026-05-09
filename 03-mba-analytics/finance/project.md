# Week 6 Project — 1-Page Financial Health Report

## What you're building

A script that reads a P&L and a balance sheet, computes six ratios, scores them into a composite health score, and prints a formatted report.

## Required functions

```python
def all_ratios(pl, bs) -> dict[str, float]: ...
def benchmark(name, value) -> str:    # "Strong" / "OK" / "Weak"
    ...
def health_score(ratios) -> tuple[float, str]:    # (score, verdict)
    ...
```

Plus code in the main body that calls them and prints the report.

## Expected output

```
=== RATIOS ===
Current ratio     : 1.88x   (Benchmark ≥ 1.5)  Strong
Quick ratio       : 1.18x   (Benchmark ≥ 1.0)  Strong
D/E ratio         : 0.72x   (Benchmark ≤ 1.0)  Strong
Gross margin      : 40.0%   (Benchmark ≥ 30%)  Strong
Operating margin  : 18.5%   (Benchmark ≥ 10%)  Strong
Net margin        : 11.2%   (Benchmark ≥  5%)  Strong

=== HEALTH SCORE ===
Score: 96 / 100 — Healthy
```

## Done when

- All six ratios print with correct formatting (x for multiples, % for margins).
- The score is between 0 and 100.
- The verdict is one of "Healthy", "Stable", or "Distressed".

**Stretch:** write the report to a two-sheet Excel workbook in memory (see Step 5 in the playground).

[▶ Open project playground](#play/03-mba-analytics/finance/project.py)
