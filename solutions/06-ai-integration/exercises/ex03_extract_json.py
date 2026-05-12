"""
Exercise 3 — Extract structured JSON from free text.

Concepts: extract prompt pattern, json.loads, low temperature.
Lesson: 06-ai-integration/lessons/02-prompts.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: prompt Groq to extract company, revenue, and CEO from the text below.
Parse the response with json.loads and print each field on its own line.

Expected output:
    company : Acme Corp
    revenue : $2.4B
    ceo     : Jane Doe
"""

import json
import os

api_key = os.environ.get("GROQ_API_KEY")

text = (
    "Acme Corp reported $2.4B in 2025 revenue under CEO Jane Doe. "
    "Operating margin held at 18%. The company expanded into APAC."
)

if not api_key:
    print("GROQ_API_KEY not set — skipping API call.")
else:
    from groq import Groq
    client = Groq(api_key=api_key)

    prompt = (
        f"Extract the company name, revenue, and CEO from the text below. "
        f"Reply with ONLY a JSON object with keys 'company', 'revenue', and 'ceo'. "
        f"No extra text.\n\nText: {text}"
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You extract structured data. Reply ONLY with valid JSON."},
            {"role": "user",   "content": prompt},
        ],
        temperature=0,
        max_completion_tokens=80,
    )

    raw = response.choices[0].message.content.strip()
    data = json.loads(raw)

    for key, val in data.items():
        print(f"{key:<10}: {val}")
