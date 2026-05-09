"""
Exercise 3 — Boolean filtering and sorting.

Concepts: boolean indexing, sort_values, head.
Lesson: 02-data-with-pandas/week-4/lessons/03-filter-sort.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: from the P&L DataFrame below, filter to rows with amount > 0
(revenue / profit lines only), sort by amount descending, and print the
count and sum of those amounts.

Expected output (approximate):
    Positive line items: 4
    Total positive amount: $9,305
    (sorted table)
"""

import pandas as pd

# Setup — P&L data.
df = pd.DataFrame({
    "line_item": [
        "Revenue", "COGS", "Gross Profit",
        "R&D", "Sales & Marketing", "G&A",
        "Operating Income", "Interest Expense",
        "Pre-tax Income", "Net Income",
    ],
    "amount": [5_400, -3_240, 2_160, -280, -420, -200, 1_000, -60, 940, 605],
    "category": [
        "Revenue", "Cost", "Profit",
        "Opex", "Opex", "Opex",
        "Profit", "Financing", "Profit", "Profit",
    ],
})

positive = df[df["amount"] > 0]

positive = positive.sort_values("amount", ascending=False)

print(f"Positive line items: {len(positive)}")
print(f"Total positive amount: ${positive['amount'].sum():,}")
print(positive.to_string(index=False))
