"""
Exercise 1 — Hello, Groq!

Concepts: Groq client, chat.completions.create, system/user roles.
Lesson: 06-ai-integration/lessons/01-first-call.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: make your first API call to Groq and print a short answer about Python
for MBA students. The response will be different every time — that is normal.

Before running: click the "Install packages" button and install `groq`.
You will also need a GROQ_API_KEY. Enter it when prompted, or hard-code it
for quick testing (do not share it with others).

Expected output (example — yours will differ):
    Python is invaluable for MBA students because it automates repetitive
    data tasks, letting you focus on insights rather than spreadsheet formulas.
    It is also the language of choice for machine-learning libraries.
"""

import os
from groq import Groq

# Setup — client (reads GROQ_API_KEY from the environment or input() below).
api_key = os.environ.get("GROQ_API_KEY") or input("Enter your GROQ_API_KEY: ")
client = Groq(api_key=api_key)

# 🛠️ Step 1: build the messages list.
#    messages = [
#        {"role": "system",  "content": "You are concise."},
#        {"role": "user",    "content": "In 2 sentences, why is Python useful for MBA students?"},
#    ]

# 🛠️ Step 2: call chat.completions.create.
#    response = client.chat.completions.create(
#        model="llama-3.3-70b-versatile",
#        messages=messages,
#        temperature=0.3,
#        max_completion_tokens=120,
#    )

# 🛠️ Step 3: print the model's reply.
#    print(response.choices[0].message.content)
