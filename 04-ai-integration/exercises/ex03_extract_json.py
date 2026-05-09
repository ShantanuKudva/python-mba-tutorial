"""
Exercise 3 — Extract structured JSON.

Ask Groq to extract company, revenue, ceo from the text.
Parse the response with json.loads. Print the dict.

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

import json
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

text = (
    "Acme Corp reported $2.4B in 2025 revenue under CEO Jane Doe. "
    "Operating margin held at 18%. The company expanded into APAC."
)

# 🛠️ Build a prompt that returns ONLY JSON with keys company, revenue, ceo.
# 🛠️ Set temperature very low (0 or 0.1).
# 🛠️ json.loads(response) and print the dict.
