"""
Exercise 2 — Executive summary from bullet points.

Concepts: prompt design, summarise pattern, temperature.
Lesson: 06-ai-integration/lessons/02-prompts.md
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

api_key = os.environ.get("GROQ_API_KEY")

metrics = """
Revenue YoY: +18%
Gross margin: 47% (up 3 pts)
Customer churn: 7.2% (up from 5.1%)
New customers: 1,420 (down 9%)
Top product line: Widgets (62% of revenue)
"""

if not api_key:
    print("GROQ_API_KEY not set — skipping API call.")
else:
    from groq import Groq
    client = Groq(api_key=api_key)

    user_message = (
        f"Write a 4-bullet executive summary (max 15 words per bullet) "
        f"based on these business metrics:\n{metrics}"
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a concise business analyst."},
            {"role": "user",   "content": user_message},
        ],
        temperature=0.3,
        max_completion_tokens=200,
    )

    print(response.choices[0].message.content)
