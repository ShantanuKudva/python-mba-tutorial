"""
Exercise 5 — Add a derived column and write to Excel.

Concepts: column arithmetic, to_excel (in-memory via BytesIO).
Lesson: 02-data-with-pandas/week-4/lessons/02-read-write-excel.md
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

# 🛠️ Step 1: add the derived column.
#    df["amount_thousands"] = df["amount"] / 1_000

# 🛠️ Step 2: write to an in-memory Excel buffer.
#    buf = io.BytesIO()
#    df.to_excel(buf, index=False)
#    buf.seek(0)

# 🛠️ Step 3: read back from the buffer to verify.
#    df2 = pd.read_excel(buf)

# 🛠️ Step 4: print column names and row count.
#    print(f"Columns: {list(df2.columns)}")
#    print(f"Rows in round-tripped file: {len(df2)}")
