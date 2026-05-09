# Lesson 2 — Reading and Writing Excel

## Read

```python
import pandas as pd

df = pd.read_excel("datasets/finance/sample_pl.xlsx")
print(df.head())
```

Multi-sheet workbook? Pick a sheet:

```python
df_q1 = pd.read_excel("workbook.xlsx", sheet_name="Q1")
all_sheets = pd.read_excel("workbook.xlsx", sheet_name=None)   # dict of DataFrames
```

Skip junk rows / pick header row:

```python
df = pd.read_excel("file.xlsx", skiprows=3, header=0)
```

## Write

```python
df.to_excel("output.xlsx", index=False)
```

`index=False` skips writing the row numbers as a column. You almost always want this.

Multi-sheet output:

```python
with pd.ExcelWriter("report.xlsx") as writer:
    summary_df.to_excel(writer, sheet_name="Summary", index=False)
    raw_df.to_excel(writer, sheet_name="Raw", index=False)
```

## CSV equivalents

```python
pd.read_csv("file.csv")
df.to_csv("out.csv", index=False)
```

Same patterns, faster format.

## Common confusions

**`No engine for filetype: 'xlsx'`** — install `openpyxl` (already in `requirements.txt`).

**Numbers come in as text** — Excel is sometimes formatted weirdly. Use `df["col"] = df["col"].astype(float)` after reading.

---

## 📚 Resources

**Official docs**
- [`pandas.read_excel`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
- [`DataFrame.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html)
- [openpyxl docs](https://openpyxl.readthedocs.io/en/stable/)

**Deep dives**
- [Real Python — Working with Excel](https://realpython.com/openpyxl-excel-spreadsheets-python/)

**Video tutorials**
- [YouTube — pandas Excel I/O](https://www.youtube.com/results?search_query=python+pandas+read+excel+write+excel+tutorial)


---

Next: [`03-filter-sort.md`](03-filter-sort.md).

---

## 🏋️ Practice

### Easy

Read `datasets/finance/sample_pl.xlsx` with `pd.read_excel`. Print the first five rows, the column names, and the shape of the resulting DataFrame.

[▶ Open exercise](#play/02-data-with-pandas/week-4/exercises/ex02_read_xlsx.py)

### Medium

Read a multi-sheet workbook. For each sheet name, print the sheet name and its number of rows. Then write a combined DataFrame (all sheets stacked) to a new file called `combined.xlsx` with `index=False`.

[▶ Open exercise](#play/02-data-with-pandas/week-4/exercises/ex02_read_xlsx.py)

### Hard

Read `sample_pl.xlsx`, add a column `margin_pct` computed from two existing columns, sort by that column descending, and write the result to a two-sheet workbook: one sheet for rows with positive margin and one for rows with negative margin.

[▶ Open exercise](#play/02-data-with-pandas/week-4/exercises/ex05_save_xlsx.py)
