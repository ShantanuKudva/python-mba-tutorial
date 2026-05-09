# Lesson 1 — RFM Segmentation

## The big idea

For each customer, compute three numbers:

- **R**ecency — days since last order (lower = more recent = better).
- **F**requency — number of orders.
- **M**onetary — total spend.

Then bucket each into 1–5 (5 = best) and concatenate. A "555" customer is a Champion. A "111" is Lost.

## Compute RFM

```python
import pandas as pd

orders = pd.read_excel("datasets/marketing/sample_orders.xlsx", sheet_name="orders")
orders["order_date"] = pd.to_datetime(orders["order_date"])

ref_date = orders["order_date"].max() + pd.Timedelta(days=1)

rfm = orders.groupby("customer_id").agg(
    recency=("order_date", lambda s: (ref_date - s.max()).days),
    frequency=("order_id", "count"),
    monetary=("amount", "sum"),
).reset_index()
```

## Score 1–5 with quintiles

`pd.qcut` divides into N equal-population buckets.

```python
rfm["R"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1]).astype(int)
rfm["F"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]).astype(int)
rfm["M"] = pd.qcut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5]).astype(int)
rfm["RFM"] = rfm["R"].astype(str) + rfm["F"].astype(str) + rfm["M"].astype(str)
```

⚠️ Recency is **inverted**: lower days = higher score. Use `labels=[5,4,3,2,1]`.

⚠️ Use `.rank(method="first")` on F if many customers tie at the same value, otherwise `qcut` complains.

## Label segments

```python
def label(row):
    R, F, M = row["R"], row["F"], row["M"]
    if R >= 4 and F >= 4 and M >= 4: return "Champions"
    if R >= 3 and F >= 3:            return "Loyal"
    if R >= 4 and F <= 2:            return "New"
    if R <= 2 and F >= 4:            return "At Risk"
    if R <= 2 and F <= 2:            return "Lost"
    return "Other"

rfm["segment"] = rfm.apply(label, axis=1)
```

`df.apply(fn, axis=1)` runs `fn` per row.

## Inspect

```python
print(rfm.groupby("segment").agg(
    customers=("customer_id", "count"),
    avg_spend=("monetary", "mean"),
).sort_values("avg_spend", ascending=False))
```

Expect Champions to have the highest average spend. If not — your scoring is inverted somewhere.

---

## 📚 Resources

**Official docs**
- [Wikipedia — RFM analysis](https://en.wikipedia.org/wiki/RFM_(market_research))
- [`pandas.qcut`](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html)

**Deep dives**
- [Towards Data Science — RFM with pandas (search)](https://www.youtube.com/results?search_query=RFM+segmentation+pandas+tutorial)

**Video tutorials**
- [YouTube — RFM segmentation](https://www.youtube.com/results?search_query=RFM+analysis+customer+segmentation+python)


---

Next: [`02-cohorts.md`](02-cohorts.md).
