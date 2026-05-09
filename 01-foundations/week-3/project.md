# Week 3 Project — Expense Categoriser

## What you're building

A script that parses a CSV of raw expenses, totals them per category, and prints a formatted summary.

## Input

The CSV data is embedded in-memory (no real file needed in the browser):

```
date,category,description,amount
2026-01-03,Travel,Flight to client,452.10
2026-01-05,Meals,Team lunch,86.50
...
```

## Expected output

```
EXPENSE SUMMARY
===============
Travel       $762.10  (2 transactions)
Meals        $254.70  (2 transactions)
Software      $84.00  (2 transactions)
Office        $75.75  (2 transactions)
---
TOTAL      $1,176.55  (8 transactions)
Skipped 1 bad row.
```

Sorted by total spend descending.

## Required structure

Use at least three functions:

```python
def load_expenses(csv_text) -> tuple[list[dict], int]:
    """Return (rows, skipped_count). Each row has a float `amount`."""

def summarise(rows: list[dict]) -> dict:
    """Return {category: {'total': float, 'count': int}}."""
```

Plus code in the main body that wires them together and prints the report.

## Done when

- The output matches the format above.
- Bad rows (non-numeric amount) are skipped and counted.
- Categories are sorted by total descending.

**Stretch:** flag any single transaction that exceeds a per-category spending limit (see ex09 for the approach).

[▶ Open project playground](#play/01-foundations/week-3/project.py)
