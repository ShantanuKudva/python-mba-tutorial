"""
Exercise 1 — Compute raw R, F, M per customer.
Print head() of the resulting DataFrame.

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
orders = pd.read_excel(ROOT / "datasets" / "marketing" / "sample_orders.xlsx", sheet_name="orders")
orders["order_date"] = pd.to_datetime(orders["order_date"])
ref_date = orders["order_date"].max() + pd.Timedelta(days=1)

# 🛠️ Build the rfm DataFrame using groupby + agg as in the lesson.
# Print rfm.head() and rfm.shape.
