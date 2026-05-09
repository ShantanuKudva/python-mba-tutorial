"""
Week 5 Project — Multi-Sheet Dashboard.

Concepts: merge, groupby, pivot_table, cumsum, matplotlib subplots, io.BytesIO.
Lesson: 02-data-with-pandas/week-5/project.md
Difficulty: Hard

Goal: merge orders with customers, produce a pivot table (monthly × region)
and a top-segments table, then draw a two-panel dashboard chart.

Expected output:
    === MONTHLY × REGION PIVOT ===
    (DataFrame with months as rows, regions as columns)

    === TOP SEGMENTS ===
    (DataFrame sorted by revenue descending)

    A 1×2 matplotlib chart displayed in the output area.
"""

import io
import pandas as pd
import matplotlib.pyplot as plt

# Setup — synthetic multi-sheet data.
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
    "region":      ["North", "South", "East", "North", "West"],
    "segment":     ["Enterprise", "Enterprise", "SMB", "Enterprise", "SMB"],
})

# 🛠️ Step 1: define load(orders_df, customers_df) → merged DataFrame.
#    df = orders.merge(customers, on="customer_id", how="left")
#    df["month"] = df["order_date"].dt.to_period("M")

# 🛠️ Step 2: define monthly_by_region(df) → pivot_table.
#    pivot = df.pivot_table(index="month", columns="region",
#                           values="amount", aggfunc="sum", fill_value=0)
#    print("=== MONTHLY × REGION PIVOT ===")
#    print(pivot)

# 🛠️ Step 3: define top_segments(df) → sorted DataFrame.
#    seg = df.groupby("segment").agg(
#        revenue=("amount", "sum"), orders=("order_id", "count")
#    ).sort_values("revenue", ascending=False)
#    print("\n=== TOP SEGMENTS ===")
#    print(seg)

# 🛠️ Step 4: define make_dashboard(df) — draws a 1×2 subplot.
#    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
#    seg["revenue"].plot(kind="bar", ax=ax1, color="steelblue")
#    ax1.set_title("Revenue by Segment"); ax1.tick_params(axis="x", rotation=0)
#    monthly = df.groupby("month")["amount"].sum().cumsum()
#    monthly.plot(kind="line", ax=ax2, marker="o", color="darkorange")
#    ax2.set_title("Cumulative Monthly Revenue")
#    plt.tight_layout(); plt.show()

# 🛠️ Step 5: call the functions in sequence.
