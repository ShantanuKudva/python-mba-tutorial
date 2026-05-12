"""
Exercise 2 — Build and inspect a DataFrame.

Concepts: pd.DataFrame from dict, .head(), .shape, .dtypes.
Lesson: 04-data-with-pandas/week-6/lessons/02-read-write-excel.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: build a 10-row P&L DataFrame from the data below and inspect it
using the standard exploration methods.

Expected output:
    (10, 4)   ← from df.shape
    ... (head of the DataFrame)
"""

import pandas as pd

# Setup — simplified P&L data (replaces reading from an xlsx file in the browser).
df = pd.DataFrame({
    "line_item": [
        "Revenue", "COGS", "Gross Profit",
        "R&D", "Sales & Marketing", "G&A",
        "Operating Income", "Interest Expense",
        "Pre-tax Income", "Net Income",
    ],
    "amount": [5_400, -3_240, 2_160, -280, -420, -200, 1_000, -60, 940, 605],
    "quarter": ["Q1"] * 10,
    "category": [
        "Revenue", "Cost", "Profit",
        "Opex", "Opex", "Opex",
        "Profit", "Financing", "Profit", "Profit",
    ],
})

# 🛠️ Step 1: print df.head() to see the first few rows.

# 🛠️ Step 2: print df.shape to see the number of rows and columns.

# 🛠️ Step 3: print df.dtypes to inspect column types.
