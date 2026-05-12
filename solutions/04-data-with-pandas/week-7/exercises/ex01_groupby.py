"""
Exercise 1 — GroupBy with named aggregations.

Concepts: groupby, named aggregations (.agg), reset_index.
Lesson: 04-data-with-pandas/week-7/lessons/01-groupby.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: given the order data below, group by region and compute three stats:
  - revenue  = sum of amount
  - avg_order = mean of amount
  - n        = count of orders

Then print the summary sorted by revenue descending.

Expected output (approximate):
      region  revenue  avg_order   n
    0  North   38950      ...      4
    ...
"""

import pandas as pd

# Setup — synthetic order data.
df = pd.DataFrame({
    "order_id": range(1, 13),
    "region":   ["North", "South", "East", "North", "West", "South",
                 "North", "East", "North", "South", "West", "East"],
    "category": ["Widgets", "Gadgets", "Widgets", "Gadgets", "Widgets", "Widgets",
                 "Gadgets", "Gadgets", "Widgets", "Gadgets", "Gadgets", "Widgets"],
    "amount":   [4200, 8100, 2300, 5100, 3400, 9200, 6100, 1800, 2900, 4700, 3100, 8600],
})

summary = df.groupby("region").agg(
    revenue   =("amount", "sum"),
    avg_order =("amount", "mean"),
    n         =("amount", "count"),
).reset_index()

summary = summary.sort_values("revenue", ascending=False)

print(summary.to_string(index=False))
