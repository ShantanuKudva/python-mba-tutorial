"""
Exercise 2 — Count lines.

Print the total number of NON-empty lines in sample_expenses.csv.
Hint: line.strip() == "" → empty.
"""

from pathlib import Path

path = Path(__file__).parent / "sample_expenses.csv"

# 🛠️ Count non-empty lines and print the total.
