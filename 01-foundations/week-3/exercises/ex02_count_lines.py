"""
Exercise 2 — Count lines.

Print the total number of NON-empty lines in sample_expenses.csv.
Hint: line.strip() == "" → empty.

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

from pathlib import Path

path = Path(__file__).parent / "sample_expenses.csv"

# 🛠️ Count non-empty lines and print the total.
