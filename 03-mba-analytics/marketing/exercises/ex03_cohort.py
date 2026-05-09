"""
Exercise 3 — Monthly cohort retention.

Build the cohort × period_index retention table from sample_orders.xlsx.
Print the percentages rounded to 1 decimal.

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
orders = pd.read_excel(ROOT / "datasets" / "marketing" / "sample_orders.xlsx", sheet_name="orders")
orders["order_date"] = pd.to_datetime(orders["order_date"])

# 🛠️ Follow lesson 2 to build retention. Print (retention * 100).round(1).
