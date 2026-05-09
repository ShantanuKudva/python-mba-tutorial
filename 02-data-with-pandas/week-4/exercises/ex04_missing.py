"""
Exercise 4 — Handle missing data (NaN).

Concepts: isna, fillna, dropna, selecting by dtype.
Lesson: 02-data-with-pandas/week-4/lessons/04-missing-data.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: inspect the NaN count per column in the DataFrame below, then fill
missing values appropriately: text columns → "Unknown", numeric → 0.
Print the NaN count before and after cleaning.

Expected output:
    NaN count before:
    line_item    1
    amount       2
    ...
    NaN count after:
    line_item    0
    ...
"""

import pandas as pd
import numpy as np

# Setup — P&L data with intentional blanks.
df = pd.DataFrame({
    "line_item": ["Revenue", None, "Gross Profit", "R&D", "Operating Income"],
    "amount":    [5_400, -3_240, np.nan, -280, np.nan],
    "category":  ["Revenue", "Cost", "Profit", "Opex", "Profit"],
})

# 🛠️ Step 1: print the NaN count per column before cleaning.
#    print("NaN count before:")
#    print(df.isna().sum())

# 🛠️ Step 2: fill text columns with "Unknown".
#    text_cols = df.select_dtypes(include="object").columns
#    df[text_cols] = df[text_cols].fillna("Unknown")

# 🛠️ Step 3: fill numeric columns with 0.
#    num_cols = df.select_dtypes(include="number").columns
#    df[num_cols] = df[num_cols].fillna(0)

# 🛠️ Step 4: print the NaN count after cleaning (should be all zeros).
#    print("\nNaN count after:")
#    print(df.isna().sum())

# 🛠️ Step 5: print the cleaned DataFrame.
#    print(df)
