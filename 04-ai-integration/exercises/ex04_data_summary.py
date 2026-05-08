"""
Exercise 4 — Real data → narrative.

Read sample_orders.xlsx. Compute:
  - Monthly revenue
  - Top 5 customers by revenue
  - Region breakdown

Send the rendered text to Groq. Ask for a 5-bullet exec summary
focusing on trends, concentration, and risks.

Print the model's response.
"""

import os
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

ROOT = Path(__file__).resolve().parents[3]
orders = pd.read_excel(ROOT / "datasets" / "marketing" / "sample_orders.xlsx", sheet_name="orders")
customers = pd.read_excel(ROOT / "datasets" / "marketing" / "sample_orders.xlsx", sheet_name="customers")
df = orders.merge(customers, on="customer_id", how="left")
df["order_date"] = pd.to_datetime(df["order_date"])

# 🛠️ Build the three summaries.
# 🛠️ Render them as a string.
# 🛠️ Build the prompt and call Groq with low temperature.
