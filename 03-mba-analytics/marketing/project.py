"""
Week 7 Project — Customer Segmentation Report.

Concepts: RFM scoring, groupby, pivot, formatted output.
Lesson: 03-mba-analytics/marketing/project.md
Difficulty: Hard

Goal: compute RFM scores for each customer, assign segment labels, then
print a per-segment summary table showing customer count, average spend,
and average recency.

Expected output:
    === PER-CUSTOMER RFM ===
    (table with columns: customer_id, recency, frequency, monetary, segment)

    === SEGMENT SUMMARY ===
    segment       customers   avg_spend   avg_recency
    Champion              2      2850.0         6.0
    Loyal                 1      1200.0        15.0
    At Risk               1       400.0        45.0
    Potential             1       900.0        31.0
"""

import pandas as pd

# Setup — synthetic order data.
orders = pd.DataFrame({
    "customer_id": [101, 102, 103, 101, 104, 102, 103, 105, 101, 104],
    "order_date":  pd.to_datetime([
        "2026-01-10", "2026-01-15", "2026-02-01", "2026-02-20",
        "2026-03-05", "2026-03-15", "2026-04-01", "2026-04-10",
        "2026-04-25", "2026-04-30",
    ]),
    "amount": [1200, 800, 500, 1500, 300, 950, 700, 200, 1100, 400],
})

ref_date = pd.Timestamp("2026-05-01")

# 🛠️ Step 1: define rfm(orders, ref_date) → DataFrame.
#    Group by customer_id and compute recency, frequency, monetary.
#    (Use the same approach as ex01.)

# 🛠️ Step 2: define score(rfm_df) → DataFrame.
#    Add R_score, F_score, M_score using pd.qcut (q=3 for small dataset).

# 🛠️ Step 3: define label(row) → str.
#    Use the same rules as ex02 (Champion / Loyal / At Risk / Potential).

# 🛠️ Step 4: apply the label function.
#    rfm_df["segment"] = rfm_df.apply(label, axis=1)

# 🛠️ Step 5: print the per-customer RFM table and the segment summary.
#    summary = rfm_df.groupby("segment").agg(
#        customers=("monetary", "count"),
#        avg_spend =("monetary", "mean"),
#        avg_recency=("recency", "mean"),
#    ).sort_values("avg_spend", ascending=False)
#    print(summary)
