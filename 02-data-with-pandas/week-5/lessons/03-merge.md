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

## 📚 Resources

**Official docs**
- [Merge, join, concatenate](https://pandas.pydata.org/docs/user_guide/merging.html)
- [`pandas.merge`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)

**Deep dives**
- [Real Python — combining DataFrames](https://realpython.com/pandas-merge-join-and-concat/)

**Video tutorials**
- [YouTube — pandas merge & join](https://www.youtube.com/results?search_query=pandas+merge+join+concat+tutorial)


---

Next: [`04-dates.md`](04-dates.md).

---

## 🏋️ Practice

### Easy

Merge an `orders` DataFrame with a `customers` DataFrame on `customer_id` using a left join. Print the shape before and after the merge to confirm no orders were dropped.

[▶ Open exercise](#play/02-data-with-pandas/week-5/exercises/ex03_merge.py)

### Medium

Merge `orders` with `customers` using different column names (`left_on="cust_id"`, `right_on="id"`). After the merge, check for any rows where customer columns are `NaN` (unmatched orders). Print the count of unmatched orders.

[▶ Open exercise](#play/02-data-with-pandas/week-5/exercises/ex03_merge.py)

### Hard

Perform a three-way merge: `orders` → `customers` → `products`. Start with a left join from orders to customers, then left join that result to products on `sku`. After the merge, compute total revenue per customer segment. Handle any column name collisions with the `suffixes` argument.

[▶ Open exercise](#play/02-data-with-pandas/week-5/exercises/ex03_merge.py)
