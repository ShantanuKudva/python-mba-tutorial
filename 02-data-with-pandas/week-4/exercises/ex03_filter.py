"""
Exercise 3 — Boolean filtering.

Read sample_pl.xlsx. Show only rows where amount > 50000.
Print the count and the sum of those amounts.

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]
df = pd.read_excel(ROOT / "datasets" / "finance" / "sample_pl.xlsx")

# 🛠️ big = df[df["amount"] > 50000]    # adjust column name to match the dataset
# 🛠️ Print len(big) and big["amount"].sum().
