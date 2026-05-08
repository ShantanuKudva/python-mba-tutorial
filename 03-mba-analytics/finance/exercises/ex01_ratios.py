"""
Exercise 1 — All-in-one ratio computation.

Read sample_pl.xlsx and sample_balance_sheet.xlsx.
Print all of: current ratio, quick ratio, D/E, gross/operating/net margin.
Format each per the lesson (% for margins, x for multiples).
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[4]


def to_lookup(df):
    return dict(zip(df["line_item"].str.strip(), df["amount"]))


pl = to_lookup(pd.read_excel(ROOT / "datasets" / "finance" / "sample_pl.xlsx"))
bs = to_lookup(pd.read_excel(ROOT / "datasets" / "finance" / "sample_balance_sheet.xlsx"))

# 🛠️ Implement each ratio function and print all 6 values.
