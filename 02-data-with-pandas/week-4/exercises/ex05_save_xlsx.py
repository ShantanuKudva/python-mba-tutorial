"""
Exercise 5 — Round-trip an xlsx.

Read sample_pl.xlsx.
Add a derived column `amount_usd_thousands = amount / 1000`.
Save as `cleaned_pl.xlsx` next to this script.

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

from pathlib import Path
import pandas as pd

HERE = Path(__file__).parent
ROOT = HERE.resolve().parents[3]
df = pd.read_excel(ROOT / "datasets" / "finance" / "sample_pl.xlsx")

# 🛠️ df["amount_usd_thousands"] = df["amount"] / 1000

# 🛠️ Save to HERE / "cleaned_pl.xlsx" with index=False.
