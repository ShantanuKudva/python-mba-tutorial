"""
Week 4 Project — Clean a Messy P&L.

Concepts: pandas DataFrames, cleaning, derived columns, groupby, io.BytesIO.
Lesson: 02-data-with-pandas/week-4/project.md
Difficulty: Hard

Goal: clean the raw P&L DataFrame (fix NaN values, normalise column names,
add a `kind` column), then produce a summary and write the result to an
in-memory Excel buffer.

Expected output:
    === CLEANED P&L ===
    (a 10-row DataFrame with columns: line_item, amount, category, kind)

    === SUMMARY ===
    Total revenue  : $5,400,000
    Total expenses : $4,440,000
    Net            :   $960,000
    Transactions   : 10
"""

import io
import numpy as np
import pandas as pd

# Setup — raw P&L data with intentional issues.
raw = pd.DataFrame({
    "Line_Item": ["Revenue ", None, "Gross Profit", "R&D", "Sales & Marketing",
                  "G&A", "Operating Income", "Interest Expense", "Pre-tax Income", "Net Income"],
    "Amount":    [5_400_000, -3_240_000, np.nan, -280_000, -420_000,
                  -200_000, 1_000_000, -60_000, 940_000, 605_000],
    "CATEGORY":  ["Revenue", "Cost", "Profit", "Opex", "Opex",
                  "Opex", "Profit", "Financing", "Profit", "Profit"],
})

# 🛠️ Step 1: define clean(df) → pd.DataFrame.
#    - Lowercase and strip column names: df.columns = df.columns.str.lower().str.strip()
#    - Strip whitespace from text columns.
#    - Fill NaN in text columns with "Unknown"; in numeric columns with 0.
#    - Add `kind` column: "revenue" if amount > 0, "expense" if amount < 0, "zero" if 0.

# 🛠️ Step 2: call clean(raw) and print the result.
#    df = clean(raw)
#    print("=== CLEANED P&L ===")
#    print(df.to_string(index=False))

# 🛠️ Step 3: define summary(df) → dict.
#    total_revenue  = df.loc[df["amount"] > 0, "amount"].sum()
#    total_expenses = df.loc[df["amount"] < 0, "amount"].sum()
#    net            = df["amount"].sum()
#    transactions   = len(df)

# 🛠️ Step 4: print the summary.

# 🛠️ Step 5 (stretch): write the cleaned DataFrame to an in-memory Excel buffer.
#    buf = io.BytesIO()
#    df.to_excel(buf, index=False, sheet_name="Cleaned")
#    buf.seek(0)
#    print(f"\nExcel buffer ready: {len(buf.read()):,} bytes")
