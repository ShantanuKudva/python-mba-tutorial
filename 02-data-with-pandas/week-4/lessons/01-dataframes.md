# Lesson 1 — DataFrames and Series

## The shape

A `DataFrame` is a table. Rows + columns. Each column is a `Series`.

```python
import pandas as pd

df = pd.DataFrame({
    "sku":     ["W-001", "W-002", "W-003"],
    "name":    ["Widget A", "Widget B", "Widget C"],
    "price":   [9.99, 14.50, 7.00],
    "stock":   [120, 8, 45],
})

print(df)
```

```
     sku      name  price  stock
0  W-001  Widget A   9.99    120
1  W-002  Widget B  14.50      8
2  W-003  Widget C   7.00     45
```

🧠 You just made the same thing as your week-2 list of dicts — but pandas can do orders of magnitude more with it.

## Inspecting

```python
df.head()        # first 5 rows
df.tail(3)       # last 3 rows
df.shape         # (rows, cols)
df.columns       # column names
df.dtypes        # type of each column
df.describe()    # summary statistics for numeric cols
df.info()        # types + memory + non-null counts
```

## Selecting columns

```python
df["price"]                  # one column → Series
df[["sku", "price"]]         # multiple → DataFrame
```

## Quick math on a column

```python
df["price"].mean()
df["stock"].sum()
df["price"].max()
df["price"] * 1.10           # vectorized — operates on every row at once
```

🧠 No loop needed. This is why pandas exists. One operation, N rows.

---

## 📚 Resources

**Official docs**
- [pandas — Intro to data structures](https://pandas.pydata.org/docs/user_guide/dsintro.html)
- [`pandas.DataFrame` reference](https://pandas.pydata.org/docs/reference/frame.html)
- [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

**Deep dives**
- [Real Python — pandas DataFrames](https://realpython.com/pandas-dataframe/)

**Video tutorials**
- [YouTube — Corey Schafer: pandas series and DataFrames](https://www.youtube.com/results?search_query=corey+schafer+pandas+dataframe)
- [YouTube — Keith Galli: complete pandas tutorial](https://www.youtube.com/results?search_query=keith+galli+pandas+tutorial)


---

Next: [`02-read-write-excel.md`](02-read-write-excel.md).
