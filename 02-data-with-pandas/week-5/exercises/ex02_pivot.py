"""
Exercise 2 — Pivot table.

Same dataset. Build a pivot: region × product_category, values = sum of amount.
Fill NaN with 0.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
df = pd.read_excel(ROOT / "datasets" / "marketing" / "sample_orders.xlsx")

# 🛠️ pivot = df.pivot_table(...)
# 🛠️ Print it.
