"""
Exercise 4 — Safety stock + reorder point.

Use weekly demand resampled from the same SKU.
Compute weekly_avg, weekly_std, safety_stock at z=1.65, lead_time=4 wk,
and the reorder point.

Print all four values.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
df = pd.read_excel(ROOT / "datasets" / "operations" / "sample_demand.xlsx")

# 🛠️ Resample to weekly. Compute mean, std. Compute safety stock + reorder point.
