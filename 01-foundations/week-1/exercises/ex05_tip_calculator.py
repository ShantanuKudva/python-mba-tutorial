"""
Exercise 5 — Tip calculator with rounding rules.

Concepts: everything from week 1.

Rules:
- Default tip is 15%.
- If the bill is over $200, raise tip to 18%.
- If service was "excellent", add 5 percentage points.
- Round the final total to 2 decimals.
- Print:
    Bill:  $XXX.XX
    Tip:   $YY.YY  (Z%)
    Total: $TTT.TT

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

bill = 240.00
service = "excellent"   # "excellent", "good", "poor"

# 🛠️ Step 1: pick base tip rate using if/elif on bill.
# Step 2: adjust if service == "excellent".
# Step 3: compute tip and total.
# Step 4: print three lines.
