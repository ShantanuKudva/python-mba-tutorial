"""
Exercise 8 — Multi-column sort and rank.

Concepts: sort_values with multiple keys, rank(), assign.
Lesson: 04-data-with-pandas/week-6/lessons/03-filter-sort.md
Difficulty: Hard
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: sort the product DataFrame first by category, then by margin descending
within each category. Add a `margin_rank` column that ranks products 1, 2, 3…
within their category (1 = highest margin). Print the result.

Expected output (approximate):
    category   product   revenue    cost   margin  margin_rank
    Hardware   Widget B    4100     1000    0.756       1
    Hardware   Widget D    9800     7500    0.235       2
    Software   Gadget A   14500    11200    0.228       1
    Software   Gadget B   12300     8000    0.350       2  ← wait, re-check order
    ...
"""

import pandas as pd

# Setup — product data with category.
df = pd.DataFrame({
    "product":  ["Widget A", "Widget B", "Gadget A", "Widget D", "Gadget B"],
    "category": ["Hardware", "Hardware", "Software", "Hardware", "Software"],
    "revenue":  [12_300, 4_100, 14_500, 9_800, 12_300],
    "cost":     [ 8_000, 1_000, 11_200, 7_500,  8_000],
})

df["margin"] = (df["revenue"] - df["cost"]) / df["revenue"]

df = df.sort_values(["category", "margin"], ascending=[True, False]).reset_index(drop=True)

df["margin_rank"] = df.groupby("category")["margin"].rank(
    method="first", ascending=False
).astype(int)

print(df.assign(margin=df["margin"].round(3)).to_string(index=False))
