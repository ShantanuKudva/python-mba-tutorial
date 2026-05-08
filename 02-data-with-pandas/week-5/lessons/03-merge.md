# Lesson 3 — Merging Two DataFrames

Excel's `VLOOKUP` / `XLOOKUP`, but for entire tables.

## Inner join (default)

```python
result = orders.merge(customers, on="customer_id")
```

Keeps only rows that match in **both** tables.

## Left join (most common)

```python
result = orders.merge(customers, on="customer_id", how="left")
```

Keep all rows from `orders`. Bring in matching `customers` data. Unmatched → `NaN` in the customer columns.

## Different key names

```python
result = orders.merge(
    customers,
    left_on="cust_id",
    right_on="id",
    how="left",
)
```

## Suffixes when columns collide

```python
orders.merge(customers, on="customer_id", suffixes=("_order", "_cust"))
```

## Common confusions

**Result has more rows than expected** — your right table has duplicate keys. Each match multiplies. Investigate with `customers["customer_id"].duplicated().sum()`.

**All-NaN columns after merge** — keys didn't match. Compare data types: `orders["customer_id"].dtype` vs `customers["customer_id"].dtype`.

---

Next: [`04-dates.md`](04-dates.md).
