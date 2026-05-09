"""
Exercise 8 — Year-over-year growth rate.

Concepts: arithmetic, conditionals, percent formatting.
Lessons: lessons/03-conditionals.md, lessons/04-strings.md
Difficulty: Hard
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Goal: given last year's revenue and this year's revenue,
print the growth rate AND a one-word verdict.

    growth = (this_year - last_year) / last_year

Verdicts:
    > 10%   → "Strong"
    0–10%   → "Modest"
    < 0%    → "Decline"

Expected output for last=100, this=125:
    YoY growth: 25.0% — Strong

Expected output for last=200, this=190:
    YoY growth: -5.0% — Decline
"""

last_year = 100
this_year = 125

growth = (this_year - last_year) / last_year

if growth > 0.10:
    verdict = "Strong"
elif growth >= 0:
    verdict = "Modest"
else:
    verdict = "Decline"

print(f"YoY growth: {growth:.1%} — {verdict}")
