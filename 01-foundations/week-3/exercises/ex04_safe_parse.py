"""
Exercise 4 — Safe parse with try/except.

Same as ex03, but ALSO count and report how many rows you skipped due to bad data.
Use try/except (ValueError, KeyError).

Expected output:
    Total: $1,083.55
    Skipped: 1 bad row

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

import csv
from pathlib import Path

path = Path(__file__).parent / "sample_expenses.csv"

# 🛠️ Loop with try/except. Track total and skipped count. Print both.
