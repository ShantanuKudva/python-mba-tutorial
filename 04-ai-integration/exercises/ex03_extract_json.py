"""
Exercise 3 — Extract structured JSON from free text.

Concepts: extract prompt pattern, json.loads, low temperature.
Lesson: 04-ai-integration/lessons/02-prompts.md
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
from groq import Groq

# Setup — client and text to extract from.
api_key = os.environ.get("GROQ_API_KEY") or input("Enter your GROQ_API_KEY: ")
client = Groq(api_key=api_key)

text = (
    "Acme Corp reported $2.4B in 2025 revenue under CEO Jane Doe. "
    "Operating margin held at 18%. The company expanded into APAC."
)

# 🛠️ Step 1: build a prompt that instructs the model to reply with ONLY a
#    JSON object containing exactly the keys "company", "revenue", and "ceo".
#    Include `text` in the prompt.

# 🛠️ Step 2: call Groq with temperature=0 (or 0.1) and max_completion_tokens=80.

# 🛠️ Step 3: parse the response.
#    raw = response.choices[0].message.content.strip()
#    data = json.loads(raw)

# 🛠️ Step 4: print each extracted field.
#    for key, val in data.items():
#        print(f"{key:<10}: {val}")
