"""
Exercise 2 — Pivot table: region × category.

Concepts: pivot_table, fill_value, aggfunc.
Lesson: 02-data-with-pandas/week-5/lessons/02-pivot.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: build a pivot table with regions as rows, product categories as columns,
and sum of amount as values. Fill any NaN cells with 0.

Expected output (approximate):
    category  Gadgets  Widgets
    region
    East         1800    10900
    North       11800     7100
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

pivot = df.pivot_table(
    index="region",
    columns="category",
    values="amount",
    aggfunc="sum",
    fill_value=0,
)

print(pivot)
