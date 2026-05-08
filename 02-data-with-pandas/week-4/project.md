# Week 4 Project — Clean a Messy P&L

## What you're building

A script that takes the messy P&L workbook and produces a clean, standardized version ready for analysis.

## Input

`datasets/finance/sample_pl.xlsx` (generate it via `datasets/generate_samples.py`). It intentionally has:

- Inconsistent column casing.
- Trailing whitespace in text cells.
- "N/A" strings instead of real blanks.
- A few rows with missing amounts.
- A few rows with negative amounts that should be expenses.

## Output

`cleaned_pl.xlsx` next to your script, with:

- All column names lowercased and stripped.
- All text cells stripped of whitespace.
- Numeric `amount` column with no NaN (drop or fill — your call, document it).
- A new `kind` column: `"revenue"` if amount > 0, `"expense"` if < 0.
- Sorted by date ascending.
- A second sheet `Summary` with:
  - Total revenue
  - Total expense
  - Net
  - Number of transactions

## Required structure

```python
def load_raw(path) -> pd.DataFrame: ...
def clean(df) -> pd.DataFrame: ...
def summary(df) -> pd.DataFrame: ...
def save(df, summary_df, out_path) -> None: ...
```

Plus a `main()` and the `if __name__ == "__main__":` guard.

## File to create

`02-data-with-pandas/week-4/clean_pl.py`

## Done when

- `cleaned_pl.xlsx` exists and opens in Excel without warnings.
- The Summary sheet shows the right totals.
- You committed.

🛠️ Stretch: add a `--input` and `--output` flag with `argparse`.
