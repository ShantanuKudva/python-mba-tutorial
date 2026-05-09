"""
Exercise 2 — Executive summary from bullet points.

Concepts: prompt design, summarise pattern, temperature.
Lesson: 04-ai-integration/lessons/02-prompts.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: send the business metrics below to Groq and ask for a 4-bullet executive
summary with at most 15 words per bullet. Print the model's response.

Expected output (example — yours will differ):
    • Revenue grew 18% YoY, outpacing the 10% industry average.
    • Gross margin improved 3 pts to 47%, signalling strong pricing power.
    • Churn rose to 7.2%, reversing a three-year declining trend.
    • New customer additions fell 9%, suggesting slower top-of-funnel activity.
"""

import os
from groq import Groq

# Setup — client and metrics.
api_key = os.environ.get("GROQ_API_KEY") or input("Enter your GROQ_API_KEY: ")
client = Groq(api_key=api_key)

metrics = """
Revenue YoY: +18%
Gross margin: 47% (up 3 pts)
Customer churn: 7.2% (up from 5.1%)
New customers: 1,420 (down 9%)
Top product line: Widgets (62% of revenue)
"""

# 🛠️ Step 1: build a user message asking for a 4-bullet executive summary
#    with at most 15 words per bullet, based on `metrics`.
#    Include `metrics` in the prompt string.

# 🛠️ Step 2: call Groq with temperature=0.3 and max_completion_tokens=200.

# 🛠️ Step 3: print the model's reply.
#    print(response.choices[0].message.content)
