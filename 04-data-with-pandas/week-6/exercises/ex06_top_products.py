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

# 🛠️ Step 1: sort by `revenue` descending.
# 🛠️ Step 2: take the first 3 rows with .head(3).
# 🛠️ Step 3: print the result.
