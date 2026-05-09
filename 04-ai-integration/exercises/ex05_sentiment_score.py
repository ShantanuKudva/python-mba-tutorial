"""
Exercise 5 — Batch sentiment scoring.

Concepts: looping over prompts, structured output, json.loads, aggregation.
Lesson: 04-ai-integration/lessons/02-prompts.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: send each customer review below to Groq and ask it to return a JSON
object with keys "sentiment" ("positive"/"neutral"/"negative") and "score"
(1–5). Parse the responses and print a summary with counts per sentiment.

Expected output (example — actual sentiment may vary):
    Review 1: positive (5)
    Review 2: negative (1)
    ...
    Summary: positive=X, neutral=Y, negative=Z
"""

import json
import os
from groq import Groq

# Setup — client and reviews.
api_key = os.environ.get("GROQ_API_KEY") or input("Enter your GROQ_API_KEY: ")
client = Groq(api_key=api_key)

reviews = [
    "Absolutely love this product — it's transformed how I track expenses!",
    "Delivery was two days late and the packaging was damaged.",
    "Works as advertised. Nothing special, nothing wrong.",
    "Customer support resolved my issue within the hour. Impressive.",
    "The software crashes every time I try to export to Excel.",
]

# 🛠️ Step 1: initialise a results list and a counter dict.
#    results = []
#    counts = {"positive": 0, "neutral": 0, "negative": 0}

# 🛠️ Step 2: loop over reviews. For each, send a Groq call asking for:
#    ONLY a JSON object with keys "sentiment" and "score".
#    Use temperature=0 and max_completion_tokens=40.

# 🛠️ Step 3: parse the JSON response. Append to results. Increment counts.
#    data = json.loads(response.choices[0].message.content.strip())
#    results.append(data)
#    counts[data["sentiment"]] += 1

# 🛠️ Step 4: print each result labelled by review number.
#    for i, (review, r) in enumerate(zip(reviews, results), start=1):
#        print(f"Review {i}: {r['sentiment']} ({r['score']})")

# 🛠️ Step 5: print the summary.
#    print(f"\nSummary: positive={counts['positive']}, neutral={counts['neutral']}, negative={counts['negative']}")
