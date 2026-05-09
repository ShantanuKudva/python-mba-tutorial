"""
Exercise 1 — Hello, Groq.

Verify your .env is set up and the API key works.
Should print one short paragraph about MBA + Python.

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.environ["GROQ_API_KEY"])

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "You are concise."},
        {"role": "user", "content": "In 2 sentences, why is Python useful for MBA students?"},
    ],
    temperature=0.3,
    max_completion_tokens=120,
)

print(response.choices[0].message.content)
