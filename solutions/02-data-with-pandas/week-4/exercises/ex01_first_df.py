"""
Exercise 1 — Build a DataFrame from a dict.

Concepts: pd.DataFrame, .shape, .dtypes, .describe.
Lesson: lessons/01-dataframes.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.

Goal: build a small product DataFrame and inspect it with built-in methods.

Expected output (shape example):
    (4, 5)
"""

import pandas as pd

df = pd.DataFrame({
    "sku":      ["W-001", "W-002", "W-003", "W-004"],
    "name":     ["Widget A", "Widget B", "Gadget A", "Bolt Pro"],
    "category": ["Hardware", "Hardware", "Software", "Hardware"],
    "price":    [29.99, 49.99, 199.00, 9.99],
    "stock":    [120, 8, 45, 200],
})

print(df)
print(df.shape)
print(df.dtypes)
print(df.describe())
