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

api_key = os.environ.get("GROQ_API_KEY")

expenses = [
    {"description": "Flight to client meeting in London",  "amount": 452.10},
    {"description": "Team lunch after quarterly review",   "amount":  86.50},
    {"description": "Monthly SaaS subscription – Slack",  "amount":  29.00},
    {"description": "Business hotel, 2 nights",           "amount": 310.00},
    {"description": "A4 paper and printer ink",           "amount":  42.75},
    {"description": "Client dinner, Taj restaurant",      "amount": 168.20},
    {"description": "AWS cloud hosting bill",             "amount":  55.00},
]

if not api_key:
    print("GROQ_API_KEY not set — skipping API call.")
else:
    from groq import Groq
    client = Groq(api_key=api_key)

    few_shot_system = (
        "You classify expense descriptions. "
        "Valid categories: Travel, Meals, Software, Office, Marketing, Other. "
        "Reply ONLY with a JSON object: {\"category\": \"<category>\"}.\n\n"
        "Examples:\n"
        "Description: Uber ride to airport → {\"category\": \"Travel\"}\n"
        "Description: Office supplies, pens and notebooks → {\"category\": \"Office\"}"
    )

    results = []
    for exp in expenses:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": few_shot_system},
                {"role": "user",   "content": f"Description: {exp['description']}"},
            ],
            temperature=0,
            max_completion_tokens=30,
        )
        raw = response.choices[0].message.content.strip()
        data = json.loads(raw)
        results.append({"description": exp["description"], "amount": exp["amount"], "category": data["category"]})

    df = pd.DataFrame(results)
    summary = df.groupby("category").agg(
        total=("amount", "sum"),
        count=("amount", "count"),
    ).sort_values("total", ascending=False)
    print(summary.to_string())
