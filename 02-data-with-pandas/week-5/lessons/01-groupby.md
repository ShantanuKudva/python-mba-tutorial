# Lesson 1 — `groupby`

The pandas equivalent of an Excel pivot table.

## Basic shape

```python
df.groupby("category")["amount"].sum()
```

Read it: *"group rows by the `category` column. Within each group, take `amount` and sum it."*

## Multiple aggregations

```python
df.groupby("category")["amount"].agg(["sum", "mean", "count"])
```

## Multiple group keys

```python
df.groupby(["region", "category"])["amount"].sum()
```

## Named aggregations (cleanest)

```python
summary = df.groupby("category").agg(
    total_amount=("amount", "sum"),
    avg_amount=("amount", "mean"),
    n=("amount", "count"),
)
```

`summary` is a DataFrame you can write to Excel directly.

## Reset the index

After groupby, the group keys become the index. To get them back as columns:

```python
summary = summary.reset_index()
```

## Common confusions

**`KeyError: 'amount'`** — typo, or the column got renamed earlier. Check `df.columns`.

**Result looks weird (multi-level columns)** — that's a `MultiIndex`. Add `.reset_index()` and/or rename.

---

Next: [`02-pivot.md`](02-pivot.md).
