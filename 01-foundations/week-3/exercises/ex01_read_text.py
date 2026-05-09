"""
Exercise 1 — Read a text file.

Open `sample_expenses.csv` and print the first 3 lines.
Use the `with open(...)` pattern.

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

from pathlib import Path

path = Path(__file__).parent / "sample_expenses.csv"

# 🛠️ Open the file, read all lines, print the first 3.
