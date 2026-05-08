# Week 3 Project — Expense Categorizer

## What you're building

A script that reads a CSV of raw expenses, totals them per category, and writes a summary CSV out.

## Input

A CSV like `exercises/sample_expenses.csv`:

```
date,category,description,amount
2026-01-03,Travel,Flight to client,452.10
2026-01-05,Meals,Team lunch,86.50
...
```

## Output

A new CSV `summary.csv`:

```
category,total,count
Meals,254.70,2
Office,75.75,2
Software,84.00,2
Travel,762.10,2
```

Sorted alphabetically by category. Total formatted as a number (no `$`).

Also print a one-screen summary to the terminal:

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

## Required structure

Use **at least three functions**:

```python
def load_expenses(path) -> tuple[list[dict], int]:
    """Return (rows, skipped_count). Each row has float `amount`."""

def summarize(rows: list[dict]) -> dict:
    """Return {category: {'total': float, 'count': int}}."""

def write_summary_csv(summary: dict, out_path) -> None:
    """Write the summary CSV (sorted by category)."""
```

Plus a `main()` that wires them together, and the `if __name__ == "__main__":` guard.

## File to create

`01-foundations/week-3/categorizer.py`

Run with:

```bash
python 01-foundations/week-3/categorizer.py 01-foundations/week-3/exercises/sample_expenses.csv
```

(Read the input path from `sys.argv[1]`. If not provided, default to the sample file.)

## Done when

- The script reads a CSV path from the command line (with a default).
- It writes `summary.csv` in the current directory.
- It prints the formatted terminal summary above.
- It handles bad rows without crashing.
- You committed.

🛠️ Stretch:

- Add a `--top N` flag (use `argparse`) to print only the top N categories by spend.
- Group by month as well as category.
