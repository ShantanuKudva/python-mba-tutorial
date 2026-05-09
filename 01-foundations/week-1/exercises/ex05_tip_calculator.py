"""
Exercise 5 — Tip calculator with rounding rules.

Concepts: variables, conditionals, arithmetic, f-strings.
Lesson: 01-foundations/week-1/lessons/03-conditionals.md
Difficulty: Hard
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Rules:
- Default tip is 15%.
- If the bill is over $200, raise tip to 18%.
- If service was "excellent", add 5 percentage points on top.
- Round the final total to 2 decimal places.

Expected output for bill = 240.00, service = "excellent":
    Bill:  $240.00
    Tip:   $ 55.20  (23%)
    Total: $295.20
"""

bill = 240.00
service = "excellent"   # try "good" or "poor" as well

# 🛠️ Step 1: pick the base tip rate.
#    tip_rate = 0.15
#    if bill > 200: tip_rate = 0.18

# 🛠️ Step 2: adjust for excellent service.
#    if service == "excellent": tip_rate += 0.05

# 🛠️ Step 3: compute tip and total.
#    tip   = round(bill * tip_rate, 2)
#    total = round(bill + tip, 2)

# 🛠️ Step 4: print the three lines.
#    print(f"Bill:  ${bill:>7.2f}")
#    print(f"Tip:   ${tip:>7.2f}  ({tip_rate:.0%})")
#    print(f"Total: ${total:>7.2f}")
