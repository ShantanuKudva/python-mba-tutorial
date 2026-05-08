"""
Exercise 4 — NaN handling.

Read sample_pl.xlsx (which has a few intentional blanks).
Print:
  - count of NaN per column
  - the DataFrame after filling text NaN with "Unknown"
    and numeric NaN with 0
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
df = pd.read_excel(ROOT / "datasets" / "finance" / "sample_pl.xlsx")

# 🛠️ print(df.isna().sum())

# 🛠️ Fill text columns with "Unknown" and numeric with 0.
# Hint: select numeric cols via df.select_dtypes(include="number").columns
