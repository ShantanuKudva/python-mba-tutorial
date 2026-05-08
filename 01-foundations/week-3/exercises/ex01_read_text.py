"""
Exercise 1 — Read a text file.

Open `sample_expenses.csv` and print the first 3 lines.
Use the `with open(...)` pattern.
"""

from pathlib import Path

path = Path(__file__).parent / "sample_expenses.csv"

# 🛠️ Open the file, read all lines, print the first 3.
