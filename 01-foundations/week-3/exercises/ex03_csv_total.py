"""
Exercise 3 — Total a CSV column.

Concepts: csv.DictReader, io.StringIO, float conversion, accumulation.
Lesson: 01-foundations/week-3/lessons/02-csv.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: read the expense CSV with csv.DictReader and sum the `amount` column.
Some rows have a non-numeric amount — skip those rows for now
(exercise 4 handles them properly with try/except).

# (Browser note: this uses io.StringIO instead of a real file.)

Expected output:
    Total expenses: $1,083.55
"""

import csv
from io import StringIO

# Setup — the CSV data lives in memory.
csv_data = """date,category,description,amount
2026-01-03,Travel,Flight to client,452.10
2026-01-05,Meals,Team lunch,86.50
2026-01-09,Software,SaaS subscription,29.00
2026-01-12,Travel,Hotel,310.00
2026-01-15,Office,Stationery,42.75
2026-01-18,Meals,Client dinner,168.20
2026-01-22,Software,Cloud hosting,55.00
2026-01-25,Travel,Taxi,bad-value
2026-01-28,Office,,33.00"""

# 🛠️ Step 1: create a DictReader over the in-memory string.
#    reader = csv.DictReader(StringIO(csv_data))

# 🛠️ Step 2: initialise `total = 0.0`.

# 🛠️ Step 3: loop over `reader`. For each row, try to add float(row["amount"])
#    to total. Skip the row if the conversion raises a ValueError.
#    Hint: use a simple try/except ValueError block.

# 🛠️ Step 4: print the formatted total.
#    print(f"Total expenses: ${total:,.2f}")
