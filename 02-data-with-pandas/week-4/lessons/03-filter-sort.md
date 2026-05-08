# Lesson 3 — Selecting, Filtering, Sorting

## `.loc` vs `.iloc`

- `.loc[row_label, col_label]` — by **name** / label.
- `.iloc[row_index, col_index]` — by **position** (integer).

```python
df.loc[0, "price"]          # first row, price column
df.iloc[0, 2]               # first row, third column
df.loc[:, ["sku", "price"]] # all rows, two columns
df.iloc[:5]                 # first 5 rows
```

## Boolean filtering (the most-used pattern)

```python
high_stock = df[df["stock"] > 50]

cheap = df[df["price"] < 10]

high_value = df[(df["stock"] > 50) & (df["price"] > 10)]
```

⚠️ Use `&` and `|`, not `and`/`or`, when filtering pandas. And **wrap each condition in parentheses**.

## Sorting

```python
df.sort_values("price")                     # ascending
df.sort_values("price", ascending=False)    # descending
df.sort_values(["category", "price"])       # multi-key
```

## Adding / replacing columns

```python
df["revenue"] = df["price"] * df["stock"]
df["price_with_tax"] = df["price"] * 1.18
```

## Renaming columns

```python
df = df.rename(columns={"old_name": "new_name"})
```

---

Next: [`04-missing-data.md`](04-missing-data.md).
