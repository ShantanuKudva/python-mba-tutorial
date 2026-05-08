# Lesson 2 — Pivot Tables

Identical idea to Excel's pivot. Rows on one axis, columns on another, values in the cells.

```python
pivot = df.pivot_table(
    index="region",
    columns="category",
    values="amount",
    aggfunc="sum",
    fill_value=0,
)
```

Output:

```
category   Office  Software  Travel
region
EMEA        1200      4500    8300
NA          900       3000    5100
APAC        450       1200    2900
```

## Multiple value columns

```python
df.pivot_table(
    index="region",
    columns="category",
    values=["amount", "units"],
    aggfunc="sum",
)
```

## When `groupby` vs `pivot_table`

- **`groupby`** when result is a long table with one row per group.
- **`pivot_table`** when you want a 2D grid (region × category).

---

Next: [`03-merge.md`](03-merge.md).
