"""
Exercise 3 — Grade a profit margin.

Concepts: if / elif / else, comparison operators.
Lesson: 01-foundations/week-1/lessons/03-conditionals.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Given a profit margin (in %), classify it as one of:
    >= 25      "Excellent"
    15 to <25  "Healthy"
    5  to <15  "Thin"
    0  to <5   "At risk"
    <0         "Loss-making"

Expected output for margin = 18.0:
    Margin 18.0% → Healthy
"""

margin = 18.0

if margin >= 25:
    grade = "Excellent"
elif margin >= 15:
    grade = "Healthy"
elif margin >= 5:
    grade = "Thin"
elif margin >= 0:
    grade = "At risk"
else:
    grade = "Loss-making"

print(f"Margin {margin}% → {grade}")
