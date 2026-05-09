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

## 📚 Resources

**Official docs**
- [Group by: split-apply-combine](https://pandas.pydata.org/docs/user_guide/groupby.html)
- [`DataFrame.groupby`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)

**Deep dives**
- [Real Python — pandas GroupBy](https://realpython.com/pandas-groupby/)

**Video tutorials**
- [YouTube — pandas groupby](https://www.youtube.com/results?search_query=pandas+groupby+tutorial)


---

Next: [`02-pivot.md`](02-pivot.md).

---

## 🏋️ Practice

### Easy

Given a DataFrame of sales transactions with `category` and `amount` columns, use `groupby` to compute the total amount per category. Reset the index and print the result sorted by total descending.

[▶ Open exercise](#play/02-data-with-pandas/week-5/exercises/ex01_groupby.py)

### Medium

Use named aggregations (`agg(total=..., avg=..., count=...)`) to compute total, average, and count for the `amount` column grouped by both `region` and `category`. Reset the index and print the result.

[▶ Open exercise](#play/02-data-with-pandas/week-5/exercises/ex06_two_level_groupby.py)

### Hard

Compute a running total (cumulative sum) of `amount` ordered by `date`. Then group by month and compute the month-over-month growth rate for each group. Flag any month with negative growth. Print the full result as a formatted table.

[▶ Open exercise](#play/02-data-with-pandas/week-5/exercises/ex07_running_total.py)
