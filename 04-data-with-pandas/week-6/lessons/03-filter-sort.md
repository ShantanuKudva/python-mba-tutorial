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

## 📚 Resources

**Official docs**
- [Indexing & selecting data](https://pandas.pydata.org/docs/user_guide/indexing.html)
- [Boolean indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#boolean-indexing)
- [`DataFrame.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html)

**Deep dives**
- [Real Python — pandas filtering](https://realpython.com/pandas-python-explore-dataset/)

**Video tutorials**
- [YouTube — pandas filter & sort](https://www.youtube.com/results?search_query=pandas+filter+sort+dataframe+tutorial)


---

Next: [`04-missing-data.md`](04-missing-data.md).

---

## 🏋️ Practice

### Easy

Given a DataFrame of products, filter it to show only rows where `price < 10`. Then sort the filtered result by `stock` descending. Print the result.

[▶ Open exercise](#play/04-data-with-pandas/week-6/exercises/ex03_filter.py)

### Medium

Add a computed column `revenue = price * stock`. Then filter to rows where `revenue > 500` AND `stock > 20`. Sort by `revenue` descending and print the top 3 products using `.iloc[:3]`.

[▶ Open exercise](#play/04-data-with-pandas/week-6/exercises/ex06_top_products.py)

### Hard

Use `.loc` to select all rows where the category column (as string) starts with `"W"` (use `.str.startswith()`). Use `.iloc` to select the last row and the second column. Rename two columns, add a `margin` column, and produce a final report DataFrame sorted by `margin` descending.

[▶ Open exercise](#play/04-data-with-pandas/week-6/exercises/ex07_columns_math.py)
