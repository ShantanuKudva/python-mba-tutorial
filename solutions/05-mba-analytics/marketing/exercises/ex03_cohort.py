"""
Exercise 3 — Monthly cohort retention table.

Concepts: cohort analysis, period arithmetic, unstack, div.
Lesson: 05-mba-analytics/marketing/lessons/02-cohorts.md
Difficulty: Hard
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: given the synthetic order data below, build a cohort × period_index
retention table showing what fraction of customers from each acquisition
cohort returned in each subsequent month. Print percentages rounded to
1 decimal place.

Expected output (approximate):
    period_index    0      1      2      3
    cohort
    2026-01       100.0  75.0  50.0   NaN
    2026-02       100.0  60.0   NaN   NaN
    ...
"""

import pandas as pd

# Setup — synthetic order data (no file needed in the browser).
orders = pd.DataFrame({
    "customer_id": [1, 2, 3, 1, 2, 4, 1, 3, 5, 2, 1, 4, 5, 2, 3],
    "order_date":  pd.to_datetime([
        "2026-01-05", "2026-01-12", "2026-01-20",   # cohort Jan
        "2026-02-08", "2026-02-15", "2026-02-20",   # cohort Jan returns + Feb new
        "2026-03-01", "2026-03-10", "2026-03-15",   # various
        "2026-03-22", "2026-04-05", "2026-04-10",
        "2026-04-18", "2026-04-25", "2026-05-01",
    ]),
})

orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["order_period"] = orders["order_date"].dt.to_period("M")

cohort_map = orders.groupby("customer_id")["order_period"].min()
cohort_map.name = "cohort"
orders = orders.join(cohort_map, on="customer_id")

orders["period_index"] = orders["order_period"].astype(int) - orders["cohort"].astype(int)

retention = (
    orders.groupby(["cohort", "period_index"])["customer_id"]
    .nunique()
    .unstack()
)

retention = retention.div(retention[0], axis=0)
print((retention * 100).round(1).to_string())
