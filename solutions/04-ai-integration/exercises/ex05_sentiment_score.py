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

api_key = os.environ.get("GROQ_API_KEY")

reviews = [
    "Absolutely love this product — it's transformed how I track expenses!",
    "Delivery was two days late and the packaging was damaged.",
    "Works as advertised. Nothing special, nothing wrong.",
    "Customer support resolved my issue within the hour. Impressive.",
    "The software crashes every time I try to export to Excel.",
]

if not api_key:
    print("GROQ_API_KEY not set — skipping API call.")
else:
    from groq import Groq
    client = Groq(api_key=api_key)

    results = []
    counts = {"positive": 0, "neutral": 0, "negative": 0}

    for review in reviews:
        prompt = (
            f"Classify the sentiment of this review. "
            f"Reply with ONLY a JSON object: {{\"sentiment\": \"positive\"|\"neutral\"|\"negative\", \"score\": 1-5}}.\n"
            f"Review: {review}"
        )
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You classify sentiment. Reply ONLY with valid JSON."},
                {"role": "user",   "content": prompt},
            ],
            temperature=0,
            max_completion_tokens=40,
        )
        data = json.loads(response.choices[0].message.content.strip())
        results.append(data)
        counts[data["sentiment"]] += 1

    for i, (review, r) in enumerate(zip(reviews, results), start=1):
        print(f"Review {i}: {r['sentiment']} ({r['score']})")

    print(f"\nSummary: positive={counts['positive']}, neutral={counts['neutral']}, negative={counts['negative']}")
