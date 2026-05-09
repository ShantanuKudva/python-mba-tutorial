"""
Exercise 8 — Customer-segment dashboard.

Concepts: merge, groupby, pivot_table, cumsum, matplotlib subplots.
Lesson: 02-data-with-pandas/week-5/lessons/05-plotting.md
Difficulty: Hard
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: merge orders with customers, produce two summary tables (segment revenue
and monthly cumulative revenue), then draw a 1×2 subplot dashboard.

Expected output:
    A 1×2 chart: left = bar by segment, right = line of cumulative monthly revenue.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Setup — orders and customers data.
orders = pd.DataFrame({
    "order_id":    range(1, 13),
    "customer_id": [101, 102, 103, 101, 104, 102, 103, 105, 101, 104, 102, 105],
    "amount":      [4200, 8100, 2300, 5100, 3400, 9200, 6100, 1800, 2900, 4700, 3100, 8600],
    "order_date":  pd.to_datetime([
        "2026-01-05", "2026-01-15", "2026-02-01", "2026-02-20",
        "2026-03-05", "2026-03-12", "2026-04-01", "2026-04-10",
        "2026-04-25", "2026-05-02", "2026-05-15", "2026-05-28",
    ]),
})

customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 104, 105],
    "name":        ["Acme", "Globex", "Initech", "Umbrella", "Stark"],
    "segment":     ["Enterprise", "Enterprise", "SMB", "Enterprise", "SMB"],
})

# 🛠️ Step 1: merge orders with customers on customer_id (left join).
#    df = orders.merge(customers, on="customer_id", how="left")

# 🛠️ Step 2: compute revenue by segment.
#    seg_rev = df.groupby("segment")["amount"].sum().sort_values(ascending=False)

# 🛠️ Step 3: compute monthly cumulative revenue.
#    monthly = df.groupby(df["order_date"].dt.to_period("M"))["amount"].sum()
#    cumulative = monthly.cumsum()

# 🛠️ Step 4: create a 1×2 subplot.
#    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# 🛠️ Step 5: draw a bar chart of revenue by segment on ax1.
#    seg_rev.plot(kind="bar", ax=ax1, color="steelblue")
#    ax1.set_title("Revenue by Segment")
#    ax1.set_xlabel("Segment"); ax1.set_ylabel("Revenue ($)")
#    ax1.tick_params(axis="x", rotation=0)

# 🛠️ Step 6: draw a line chart of cumulative revenue on ax2.
#    cumulative.plot(kind="line", ax=ax2, marker="o", color="darkorange")
#    ax2.set_title("Cumulative Monthly Revenue")
#    ax2.set_xlabel("Month"); ax2.set_ylabel("Cumulative Revenue ($)")

# 🛠️ Step 7: display the chart.
#    plt.tight_layout()
#    plt.show()
