# Lesson 2 — Cohort Retention

## What it answers

*"Of the customers who first ordered in January, how many are still ordering 1, 2, 3, 6 months later?"*

## Build it

```python
import pandas as pd

orders = pd.read_excel("datasets/marketing/sample_orders.xlsx", sheet_name="orders")
orders["order_date"] = pd.to_datetime(orders["order_date"])

# 1. Cohort = month of customer's first order.
orders["cohort"] = orders.groupby("customer_id")["order_date"].transform("min").dt.to_period("M")

# 2. Order period.
orders["order_period"] = orders["order_date"].dt.to_period("M")

# 3. Periods elapsed since cohort start.
orders["period_index"] = (
    orders["order_period"].astype("int64") - orders["cohort"].astype("int64")
)

# 4. Cohort × period_index → unique customers.
cohort = (
    orders.groupby(["cohort", "period_index"])["customer_id"]
    .nunique()
    .unstack(fill_value=0)
)

# 5. Retention rates: divide by the cohort's size at period 0.
retention = cohort.div(cohort.iloc[:, 0], axis=0)
print((retention * 100).round(1))
```

The result: rows = cohort month, cols = period index (0, 1, 2, …), values = % of original customers retained.

## Interpret

- Period 0 is always 100% (everyone in the cohort orders in that month by definition).
- A drop from 100 → 30 between period 0 and 1 means 70% of those customers never came back.
- Compare across cohorts to see if recent ones are improving (good acquisition) or worsening.

---

Next: [`03-ab-test.md`](03-ab-test.md).
