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

# 🛠️ Step 1: ask for company name, revenue (float), and costs (float).
#    Add an inline comment explaining what each variable stores.

# 🛠️ Step 2: compute gross_margin = (revenue - costs) / revenue * 100.
#    Add a comment noting that margin uses revenue in the denominator.

# 🛠️ Step 3: print the four-line snapshot.
#    Label width: :<14, revenue/costs: :>12,  (with $ prefix), margin: :>9.1f%.
