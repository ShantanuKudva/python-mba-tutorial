"""
Exercise 3 — Boolean filtering.

Read sample_pl.xlsx. Show only rows where amount > 50000.
Print the count and the sum of those amounts.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
df = pd.read_excel(ROOT / "datasets" / "finance" / "sample_pl.xlsx")

# 🛠️ big = df[df["amount"] > 50000]    # adjust column name to match the dataset
# 🛠️ Print len(big) and big["amount"].sum().
