"""
Exercise 6 — Expense classification pipeline.

Concepts: few-shot prompting, json.loads, pandas, aggregation.
Lesson: 06-ai-integration/lessons/03-data-to-prompt.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: use Groq to classify each expense description into a standard category,
then aggregate total spend per category and print a summary table.

Categories to use: Travel, Meals, Software, Office, Marketing, Other.

Expected output (example — actual categories depend on the model):
    Category     Total     Count
    Travel       $762.10       2
    Software      $84.00       2
    ...
"""

import json
import os
import pandas as pd
from groq import Groq

# Setup — client and expense data.
api_key = os.environ.get("GROQ_API_KEY") or input("Enter your GROQ_API_KEY: ")
client = Groq(api_key=api_key)

expenses = [
    {"description": "Flight to client meeting in London",  "amount": 452.10},
    {"description": "Team lunch after quarterly review",   "amount":  86.50},
    {"description": "Monthly SaaS subscription – Slack",  "amount":  29.00},
    {"description": "Business hotel, 2 nights",           "amount": 310.00},
    {"description": "A4 paper and printer ink",           "amount":  42.75},
    {"description": "Client dinner, Taj restaurant",      "amount": 168.20},
    {"description": "AWS cloud hosting bill",             "amount":  55.00},
]

# 🛠️ Step 1: define a few-shot prompt that shows the model two labelled examples
#    then asks it to classify the given description.
#    The reply must be ONLY a JSON object: {"category": "<category>"}

# 🛠️ Step 2: loop over expenses. For each, call Groq with the description
#    and parse the JSON response to get the category.

# 🛠️ Step 3: store results in a list of dicts (description, amount, category).

# 🛠️ Step 4: create a DataFrame and group by category.
#    df = pd.DataFrame(results)
#    summary = df.groupby("category").agg(
#        total=("amount", "sum"),
#        count=("amount", "count"),
#    ).sort_values("total", ascending=False)
#    print(summary.to_string())
