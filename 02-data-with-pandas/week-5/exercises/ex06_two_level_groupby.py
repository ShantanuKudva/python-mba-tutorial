"""
Exercise 6 — Two-level groupby (region + quarter).

Concepts: groupby on multiple columns, agg, reset_index.
Lesson: lessons/01-groupby.md
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Goal: group by (region, quarter) and compute:
   - revenue sum
   - order count

Expected output (a tidy DataFrame, 4 rows):
      region quarter  revenue  orders
    0   East      Q1    14100       1
    1  North      Q1    12450       1
    2  North      Q2    13000       1
    3  South      Q1     9300       1
"""

import pandas as pd

df = pd.DataFrame({
    "region":  ["North", "South", "East",  "North"],
    "quarter": ["Q1",    "Q1",    "Q1",    "Q2"],
    "revenue": [12_450,   9_300,  14_100,  13_000],
})

# 🛠️ Step 1: grouped = df.groupby(["region", "quarter"]).agg(
#                revenue=("revenue", "sum"),
#                orders=("revenue", "count"),
#            ).reset_index()
# 🛠️ Step 2: print(grouped)
