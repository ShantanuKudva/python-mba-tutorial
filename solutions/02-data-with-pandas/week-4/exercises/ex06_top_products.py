"""
Exercise 6 — Top-N products by revenue (pandas).

Concepts: DataFrame creation, sort_values, head.
Lesson: lessons/03-filter-sort.md
Difficulty: Easy
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Goal: from the `df` below, print the 3 highest-revenue rows,
sorted descending.

Expected output:
       product  revenue
    2  Gadget    14500
    0  Widget    12300
    3  Bolt       9800
"""

import pandas as pd

df = pd.DataFrame({
    "product": ["Widget", "Sprocket", "Gadget", "Bolt", "Pipe"],
    "revenue": [12_300, 4_100, 14_500, 9_800, 3_400],
})

top3 = df.sort_values("revenue", ascending=False).head(3)
print(top3)
