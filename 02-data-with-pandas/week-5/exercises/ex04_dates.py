"""
Exercise 4 — Dates and monthly totals.

Read the orders sheet.
Parse `order_date` to datetime.
Compute monthly revenue using groupby on month period (or resample).
Print the resulting series.

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
xlsx = ROOT / "datasets" / "marketing" / "sample_orders.xlsx"
df = pd.read_excel(xlsx, sheet_name="orders")

# 🛠️ df["order_date"] = pd.to_datetime(df["order_date"])
# 🛠️ Compute monthly = df.groupby(df["order_date"].dt.to_period("M"))["amount"].sum()
# 🛠️ Print it.
