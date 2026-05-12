# Week 6 — pandas Fundamentals

**Goal:** read a messy Excel workbook, clean it, and save the clean version.

## What you'll learn

- `DataFrame` and `Series` — the two core objects.
- `loc` vs `iloc` indexing.
- Reading/writing Excel with `pd.read_excel` / `df.to_excel`.
- Filtering, sorting, sampling, describing.
- Handling missing values (`NaN`, `fillna`, `dropna`).

## Map

| File | Topic |
|---|---|
| [`lessons/01-dataframes.md`](lessons/01-dataframes.md) | First DataFrame |
| [`lessons/02-read-write-excel.md`](lessons/02-read-write-excel.md) | Excel I/O |
| [`lessons/03-filter-sort.md`](lessons/03-filter-sort.md) | Selection, filter, sort |
| [`lessons/04-missing-data.md`](lessons/04-missing-data.md) | Cleaning NaNs |
| [`exercises/`](exercises/) | 5 problems |
| [`project.md`](project.md) | Clean a messy P&L |

## Checklist before week 5

- [ ] You can read an `.xlsx` into a DataFrame.
- [ ] You know when to use `.loc[...]` vs `.iloc[...]`.
- [ ] You filtered rows with a boolean condition.
- [ ] You handled `NaN` deliberately (not by ignoring it).
- [ ] You saved the cleaned DataFrame back to `.xlsx`.
