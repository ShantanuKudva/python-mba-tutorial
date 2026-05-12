"""
Exercise 1 — Compute raw Recency, Frequency, Monetary per customer.

Concepts: groupby, agg, timedelta, lambda.
Lesson: 05-mba-analytics/marketing/lessons/01-rfm.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: compute three RFM metrics per customer from the synthetic order data below:
  - Recency    = days since the customer's most recent order (relative to ref_date)
  - Frequency  = total number of orders
  - Monetary   = total spend

Expected output:
    rfm table with columns: customer_id, recency, frequency, monetary
    (5 rows, values will match the data below)
"""

import pandas as pd

# Setup — synthetic order data (no file needed in the browser).
orders = pd.DataFrame({
    "customer_id": [101, 102, 103, 101, 104, 102, 103, 105, 101, 104],
    "order_date":  pd.to_datetime([
        "2026-01-10", "2026-01-15", "2026-02-01", "2026-02-20",
        "2026-03-05", "2026-03-15", "2026-04-01", "2026-04-10",
        "2026-04-25", "2026-04-30",
    ]),
    "amount": [1200, 800, 500, 1500, 300, 950, 700, 200, 1100, 400],
})

ref_date = pd.Timestamp("2026-05-01")   # "today" for recency calculation

rfm = orders.groupby("customer_id").agg(
    recency  =("order_date", lambda x: (ref_date - x.max()).days),
    frequency=("order_date", "count"),
    monetary =("amount",     "sum"),
).reset_index()

rfm = rfm.sort_values("recency")

print(rfm.to_string(index=False))
print(f"\nShape: {rfm.shape}")
