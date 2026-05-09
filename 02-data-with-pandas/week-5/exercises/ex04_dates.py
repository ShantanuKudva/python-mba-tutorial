"""
Exercise 4 — Parse dates and compute monthly totals.

Concepts: pd.to_datetime, dt accessor, to_period, groupby.
Lesson: 02-data-with-pandas/week-5/lessons/04-dates.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: parse order_date to datetime, extract the month, and compute monthly
revenue totals. Print the monthly series.

Expected output (approximate):
    order_date
    2026-01    9300
    2026-02    5500
    ...
"""

import pandas as pd

# Setup — synthetic order data with string dates.
df = pd.DataFrame({
    "order_id":   range(1, 11),
    "order_date": [
        "2026-01-05", "2026-01-18", "2026-02-03",
        "2026-02-22", "2026-03-11", "2026-03-28",
        "2026-04-09", "2026-04-20", "2026-05-07", "2026-05-25",
    ],
    "amount": [4200, 5100, 8100, 9200, 2300, 1800, 6100, 3400, 4700, 2900],
})

# 🛠️ Step 1: convert the string column to datetime.
#    df["order_date"] = pd.to_datetime(df["order_date"])

# 🛠️ Step 2: group by month using .dt.to_period("M").
#    monthly = df.groupby(df["order_date"].dt.to_period("M"))["amount"].sum()

# 🛠️ Step 3: print the monthly series.
#    print(monthly)

# 🛠️ Bonus: which month had the highest revenue?
#    print(f"\nBest month: {monthly.idxmax()} — ${monthly.max():,}")
