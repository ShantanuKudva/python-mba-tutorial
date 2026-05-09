"""
Exercise 1 — Moving-average forecast.

Read sample_demand.xlsx. Pick one SKU. Compute a 3-month moving average
forecast for the next 12 months. Print the forecast.

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
df = pd.read_excel(ROOT / "datasets" / "operations" / "sample_demand.xlsx")

# 🛠️ Pick one sku. Build a Series indexed by month. Compute 3-month moving avg
# 🛠️ as the constant forecast and print 12 future periods.
