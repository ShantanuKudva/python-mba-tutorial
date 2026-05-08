"""
Exercise 1 — groupby.

Read datasets/marketing/sample_orders.xlsx.
Group by `region`. Compute total revenue, average order value, and order count.
Print the result.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
df = pd.read_excel(ROOT / "datasets" / "marketing" / "sample_orders.xlsx")

# 🛠️ summary = df.groupby("region").agg(
#         revenue=("amount", "sum"),
#         avg_order=("amount", "mean"),
#         n=("amount", "count"),
#     )
# 🛠️ Print summary.
