"""
Exercise 4 — Safe parse with try/except.

Concepts: try/except, ValueError, KeyError, csv.DictReader, io.StringIO.
Lesson: 01-foundations/week-3/lessons/03-errors.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: same as ex03, but also count and report how many rows were skipped
due to bad data. Catch both ValueError (non-numeric amount) and KeyError
(missing column).

# (Browser note: this uses io.StringIO instead of a real file.)

Expected output:
    Total: $1,083.55
    Skipped: 1 bad row
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

reader = csv.DictReader(StringIO(csv_data))

total = 0.0
skipped = 0

for row in reader:
    try:
        total += float(row["amount"])
    except (ValueError, KeyError):
        skipped += 1

print(f"Total: ${total:,.2f}")
print(f"Skipped: {skipped} bad row{'s' if skipped != 1 else ''}")
