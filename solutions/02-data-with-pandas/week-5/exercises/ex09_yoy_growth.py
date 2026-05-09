"""
Exercise 9 — Year-over-year growth with pandas.

Concepts: groupby, pct_change, sort_values, formatted output.
Lesson: 02-data-with-pandas/week-5/lessons/01-groupby.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: given a quarterly revenue DataFrame, compute year-over-year growth
for each product line and print the results.

Expected output (approximate):
    product_line  2024_revenue  2025_revenue  yoy_growth
    Widgets            450000        540000       20.0%
    Gadgets            280000        322000       15.0%
    Services           120000        138000       15.0%
"""

import pandas as pd

# Setup — quarterly data for two years.
df = pd.DataFrame({
    "product_line": ["Widgets", "Gadgets", "Services"] * 8,  # 8 quarters × 3 lines
    "year":  [2024]*12 + [2025]*12,
    "quarter": ["Q1","Q1","Q1","Q2","Q2","Q2","Q3","Q3","Q3","Q4","Q4","Q4"] * 2,
    "revenue": [
        # 2024
        100_000, 65_000, 28_000,
        110_000, 70_000, 30_000,
        115_000, 72_000, 32_000,
        125_000, 73_000, 30_000,
        # 2025
        120_000, 75_000, 33_000,
        130_000, 80_000, 35_000,
        135_000, 83_000, 36_000,
        155_000, 84_000, 34_000,
    ],
})

annual = df.groupby(["product_line", "year"])["revenue"].sum().unstack("year")

annual.columns = ["2024_revenue", "2025_revenue"]

annual["yoy_growth"] = (annual["2025_revenue"] - annual["2024_revenue"]) / annual["2024_revenue"]

annual = annual.sort_values("yoy_growth", ascending=False)
annual["yoy_growth"] = annual["yoy_growth"].map(lambda x: f"{x:.1%}")
print(annual.to_string())
