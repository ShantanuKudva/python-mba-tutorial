"""
Exercise 2 — Read an xlsx.

Read datasets/finance/sample_pl.xlsx and print its head + shape.
"""

from pathlib import Path
import pandas as pd

# Path resolves to the dataset regardless of where you run from.
ROOT = Path(__file__).resolve().parents[4]
xlsx = ROOT / "datasets" / "finance" / "sample_pl.xlsx"

# 🛠️ df = pd.read_excel(xlsx)
# 🛠️ Print df.head() and df.shape.
