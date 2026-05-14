"""
Exercise 13 — Weeks from days and compound growth.

Concepts: floor division (//), modulo (%), exponentiation (**).
Lesson: 01-foundations/week-1/lessons/06-operators-and-math.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: practice // and % to break a day-count into weeks and leftover days,
then use ** to compute compound revenue growth over multiple years.

Expected output:
    250 days = 35 weeks and 5 days
    Revenue after 3 years at 8% growth: $1,259,712.00
"""

total_days      = 250
start_revenue   = 1_000_000
growth_rate     = 0.08
years           = 3

weeks    = total_days // 7
leftover = total_days % 7

print(f"{total_days} days = {weeks} weeks and {leftover} days")

end_revenue = start_revenue * (1 + growth_rate) ** years

print(f"Revenue after {years} years at {growth_rate:.0%} growth: ${end_revenue:,.2f}")
