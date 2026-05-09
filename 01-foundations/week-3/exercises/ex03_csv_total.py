"""
Exercise 3 — Total a CSV column.

Read sample_expenses.csv with csv.DictReader.
Sum the `amount` column. Print as $X,XXX.XX.

⚠️ Some rows have a non-numeric amount. Skipping them is fine for now —
exercise 4 handles it cleanly.

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

import csv
from pathlib import Path

path = Path(__file__).parent / "sample_expenses.csv"

# 🛠️ Open the file, build a total. Use try/except OR test if amount is digit-y.
