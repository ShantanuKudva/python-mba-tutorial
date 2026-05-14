"""
Exercise 12 — Marketing budget burn-down.

Concepts: while loop, break, accumulator, else clause on loop.
Lesson: 01-foundations/week-1/lessons/05-loops.md
Difficulty: Hard
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: simulate drawing down a marketing budget month by month. Each month has
a known spend. Stop (break) when the next spend would take the budget below
zero. Report the month that would cause the shortfall and how much remains.
If the whole budget is consumed without going negative, print a success line.

Expected output (for the data below):
    Month 1: spent $18,000 — remaining $82,000
    Month 2: spent $24,500 — remaining $57,500
    Month 3: spent $31,000 — remaining $26,500
    Month 4 spend ($29,000) would exceed remaining budget ($26,500). Stopping.
    Budget remaining at end of month 3: $26,500
"""

budget = 100_000
monthly_spend = [18_000, 24_500, 31_000, 29_000, 15_000, 12_000]

remaining = budget
month = 0

while month < len(monthly_spend):
    spend = monthly_spend[month]
    month += 1

    if spend > remaining:
        print(f"Month {month} spend (${spend:,}) would exceed remaining budget (${remaining:,}). Stopping.")
        month -= 1   # step back so we report the last safe month
        break

    remaining -= spend
    print(f"Month {month}: spent ${spend:,} — remaining ${remaining:,}")

print(f"Budget remaining at end of month {month}: ${remaining:,}")
