"""
Exercise 7 — Derived columns: profit and margin.

Concepts: column arithmetic, derived columns.
Lesson: lessons/01-dataframes.md
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Goal: add two new columns to the DataFrame:
   - profit = revenue - cost
   - margin = profit / revenue

Then print the row with the HIGHEST margin.

Expected output (only the winning row):
       product  revenue  cost  profit    margin
    1  Sprocket    4100  1000    3100  0.756098
"""

import pandas as pd

df = pd.DataFrame({
    "product": ["Widget", "Sprocket", "Gadget", "Bolt"],
    "revenue": [12_300, 4_100, 14_500, 9_800],
    "cost":    [ 8_000, 1_000, 11_200, 7_500],
})

# 🛠️ Step 1: df["profit"] = df["revenue"] - df["cost"]
# 🛠️ Step 2: df["margin"] = df["profit"] / df["revenue"]
# 🛠️ Step 3: idx = df["margin"].idxmax()
# 🛠️ Step 4: print(df.loc[[idx]])
