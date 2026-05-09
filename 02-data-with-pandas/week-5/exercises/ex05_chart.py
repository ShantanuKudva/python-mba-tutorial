"""
Exercise 5 — Bar chart to PNG.

Same dataset. Make a bar chart of monthly revenue.
Save as `monthly.png` next to this script.
Use plt.tight_layout() and dpi=150.

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

HERE = Path(__file__).parent
ROOT = HERE.resolve().parents[3]
df = pd.read_excel(ROOT / "datasets" / "marketing" / "sample_orders.xlsx", sheet_name="orders")

df["order_date"] = pd.to_datetime(df["order_date"])
monthly = df.groupby(df["order_date"].dt.to_period("M"))["amount"].sum()

# 🛠️ Plot monthly as a bar chart.
# 🛠️ Save to HERE / "monthly.png".
