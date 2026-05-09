"""
Exercise 1 — Age in days.

Concepts: variables, integer arithmetic.
Lesson: lessons/02-variables-and-types.md
Difficulty: Easy
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Goal: given an age in years, print the (approximate) age in days.
Use 365 days/year.

Expected output for age = 28:
    A 28-year-old has lived approximately 10220 days.
"""

age_years = 28

age_days = age_years * 365

print(f"A {age_years}-year-old has lived approximately {age_days} days.")
