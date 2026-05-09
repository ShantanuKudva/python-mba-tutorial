"""
Exercise 3 — Merge.

The marketing workbook has two sheets: `orders` and `customers`.
Read both and merge on customer_id (left join from orders).
Print the first 5 merged rows.

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
xlsx = ROOT / "datasets" / "marketing" / "sample_orders.xlsx"

# 🛠️ orders = pd.read_excel(xlsx, sheet_name="orders")
# 🛠️ customers = pd.read_excel(xlsx, sheet_name="customers")
# 🛠️ merged = orders.merge(customers, on="customer_id", how="left")
# 🛠️ Print merged.head().
