"""
Exercise 4 — Aggregate data → narrative summary.

Concepts: aggregate → render → prompt → parse pipeline, pandas, Groq.
Lesson: 04-ai-integration/lessons/03-data-to-prompt.md
Difficulty: Hard
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: given the synthetic order data below, compute three summaries
(monthly revenue, top-5 customers, region breakdown), render them as a text
block, then send to Groq asking for a 5-bullet exec summary focused on
trends, concentration risk, and recommended actions. Print the response.

Expected output (example — yours will differ):
    • Revenue peaked in Q3 at $42,000 before declining 12% in Q4.
    • The top 5 customers represent 68% of total revenue — concentration risk.
    ...
"""

import os
import pandas as pd
from groq import Groq

# Setup — synthetic order data (no file read needed in the browser).
api_key = os.environ.get("GROQ_API_KEY") or input("Enter your GROQ_API_KEY: ")
client = Groq(api_key=api_key)

orders = pd.DataFrame({
    "order_id":    range(1, 21),
    "customer":    ["Acme", "Globex", "Initech", "Acme", "Umbrella",
                    "Globex", "Acme", "Stark", "Initech", "Acme",
                    "Umbrella", "Globex", "Acme", "Initech", "Stark",
                    "Globex", "Acme", "Initech", "Umbrella", "Acme"],
    "region":      ["North", "South", "East", "North", "West",
                    "South", "North", "East", "East", "North",
                    "West", "South", "North", "East", "East",
                    "South", "North", "East", "West", "North"],
    "amount":      [4200, 8100, 2300, 5100, 3400,
                    9200, 6100, 1800, 2900, 4700,
                    3100, 8600, 5300, 3200, 1900,
                    9800, 6400, 2700, 3600, 5500],
    "order_date":  pd.to_datetime([
        "2026-01-15", "2026-02-03", "2026-02-20", "2026-03-10", "2026-03-25",
        "2026-04-05", "2026-04-18", "2026-05-02", "2026-05-20", "2026-06-08",
        "2026-06-22", "2026-07-14", "2026-07-28", "2026-08-10", "2026-08-25",
        "2026-09-05", "2026-09-18", "2026-10-02", "2026-10-20", "2026-11-08",
    ]),
})

# 🛠️ Step 1: compute the three summaries.
#    monthly = orders.groupby(orders["order_date"].dt.to_period("M"))["amount"].sum()
#    top5    = orders.groupby("customer")["amount"].sum().nlargest(5)
#    regions = orders.groupby("region")["amount"].sum().sort_values(ascending=False)

# 🛠️ Step 2: render them as a plain-text block.
#    summary_text = (
#        f"Monthly revenue:\n{monthly.to_string()}\n\n"
#        f"Top 5 customers:\n{top5.to_string()}\n\n"
#        f"Region breakdown:\n{regions.to_string()}"
#    )

# 🛠️ Step 3: build the prompt and call Groq.
#    Ask for 5 bullets focused on trends, concentration risk, and recommendations.
#    Use temperature=0.4 and max_completion_tokens=300.

# 🛠️ Step 4: print the model's response.
#    print(response.choices[0].message.content)
