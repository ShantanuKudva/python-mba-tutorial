# Exercises — Week 6 · DataFrames

> Practice problems for the lessons in this module. Each exercise opens directly in the browser playground — fill in the steps and click ▶ Run.

## 📚 Read first

Skim these before attempting the harder exercises:
- [Lesson 01 — DataFrames](../lessons/01-dataframes.md)
- [Lesson 02 — Read/Write Excel](../lessons/02-read-write-excel.md)
- [Lesson 03 — Filter & Sort](../lessons/03-filter-sort.md)
- [Lesson 04 — Missing Data](../lessons/04-missing-data.md)
- [pandas official docs — DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- [Real Python — pandas Tutorial](https://realpython.com/pandas-dataframe/)

## 🟢 Easy

- [ex01 — Build a DataFrame from a dict](#play/04-data-with-pandas/week-6/exercises/ex01_first_df.py) — `pd.DataFrame`, `.shape`, `.dtypes`, `.describe`.
- [ex02 — Inspect a P&L DataFrame](#play/04-data-with-pandas/week-6/exercises/ex02_read_xlsx.py) — `.head()`, `.shape`, `.dtypes`.
- [ex06 — Top-N products](#play/04-data-with-pandas/week-6/exercises/ex06_top_products.py) — `sort_values`, `head`.

## 🟡 Medium

- [ex03 — Boolean filtering](#play/04-data-with-pandas/week-6/exercises/ex03_filter.py) — boolean indexing, `sort_values`.
- [ex04 — NaN handling](#play/04-data-with-pandas/week-6/exercises/ex04_missing.py) — `isna`, `fillna`, `select_dtypes`.
- [ex05 — Round-trip to Excel (in-memory)](#play/04-data-with-pandas/week-6/exercises/ex05_save_xlsx.py) — derived columns, `io.BytesIO`, `to_excel`.

## 🔴 Hard

- [ex07 — Profit and margin columns](#play/04-data-with-pandas/week-6/exercises/ex07_columns_math.py) — column arithmetic, `idxmax`, `loc`.
- [ex08 — Multi-column sort and rank](#play/04-data-with-pandas/week-6/exercises/ex08_multi_column_sort.py) — `sort_values` with multiple keys, `.rank()` within groups.
