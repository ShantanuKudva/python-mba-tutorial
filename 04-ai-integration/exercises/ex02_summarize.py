"""
Exercise 2 — Summarize prompt.

Send the metrics below. Ask for a 4-bullet executive summary, ≤15 words per bullet.
Print the response.
"""

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

metrics = """
Revenue YoY: +18%
Gross margin: 47% (up 3 pts)
Customer churn: 7.2% (up from 5.1%)
New customers: 1,420 (down 9%)
Top product line: Widgets (62% of revenue)
"""

# 🛠️ Build the prompt and call Groq. Print the result.
