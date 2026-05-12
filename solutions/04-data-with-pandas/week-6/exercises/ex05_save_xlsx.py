"""
Exercise 5 — Add a derived column and write to Excel.

Concepts: column arithmetic, to_excel (in-memory via BytesIO).
Lesson: 04-data-with-pandas/week-6/lessons/02-read-write-excel.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: add a `amount_thousands` column (amount / 1000), then write the result
to an in-memory Excel buffer and confirm the row count after round-tripping.

# (Browser note: we write to io.BytesIO instead of a file on disk.)

Expected output:
    Columns: ['line_item', 'amount', 'category', 'amount_thousands']
    Rows in round-tripped file: 5
"""

import io
import pandas as pd

# Setup — P&L data.
df = pd.DataFrame({
    "line_item": ["Revenue", "COGS", "Gross Profit", "Operating Income", "Net Income"],
    "amount":    [5_400, -3_240, 2_160, 1_000, 605],
    "category":  ["Revenue", "Cost", "Profit", "Profit", "Profit"],
})

df["amount_thousands"] = df["amount"] / 1_000

buf = io.BytesIO()
df.to_excel(buf, index=False)
buf.seek(0)

df2 = pd.read_excel(buf)

print(f"Columns: {list(df2.columns)}")
print(f"Rows in round-tripped file: {len(df2)}")
