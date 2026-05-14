"""
Exercise 17 — Company snapshot from user input.

Concepts: input(), float(), print() formatting, inline comments.
Lesson: 01-foundations/week-1/lessons/07-input-and-print.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: ask the user for company name, revenue, and costs. Compute gross margin
and print a four-line snapshot with labels left-aligned in 14 characters and
monetary values right-aligned with thousands separators.

Expected output (for "Acme Corp", 1_245_000, 820_000):
    Company       : Acme Corp
    Revenue       :  $1,245,000
    Costs         :    $820,000
    Gross margin  :      34.1%
"""

company = input("Company name: ")
revenue = float(input("Annual revenue ($): "))
costs   = float(input("Annual costs ($): "))   # total operating costs

# Gross margin: profit as a percentage of revenue (not costs)
gross_margin = (revenue - costs) / revenue * 100

print(f"{'Company':<14}: {company}")
print(f"{'Revenue':<14}: ${revenue:>11,.0f}")
print(f"{'Costs':<14}: ${costs:>11,.0f}")
print(f"{'Gross margin':<14}: {gross_margin:>10.1f}%")
