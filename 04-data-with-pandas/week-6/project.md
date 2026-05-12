# Week 6 Project — Clean a Messy P&L

## What you're building

A script that takes a raw P&L DataFrame (with intentional issues) and produces a clean, standardised version ready for analysis.

## The raw data has

- Inconsistent column casing and trailing whitespace.
- `None` values in text cells.
- `NaN` values in numeric cells.
- No `kind` column (revenue vs expense).

## Expected output

```
=== CLEANED P&L ===
(10-row DataFrame with columns: line_item, amount, category, kind)

=== SUMMARY ===
Total revenue  : $5,400,000
Total expenses : $4,440,000
Net            :   $960,000
Transactions   : 10
```

## Required structure

```python
def clean(df) -> pd.DataFrame:
    """Lowercase + strip column names; fill NaN; add `kind` column."""

def summary(df) -> dict:
    """Return total_revenue, total_expenses, net, transactions."""
```

## Done when

- The cleaned DataFrame has all-lowercase stripped column names.
- `NaN` values are gone (text → "Unknown", numeric → 0).
- The `kind` column correctly labels "revenue", "expense", or "zero".
- The summary numbers match the expected output.

**Stretch:** write the cleaned DataFrame to an in-memory Excel buffer and confirm the byte count (see Step 5 in the playground).

[▶ Open project playground](#play/04-data-with-pandas/week-6/project.py)
