"""
Exercise 7 — Unique SKUs and churn analysis.

Concepts: sets, set operations.
Lesson: lessons/05-tuples-and-sets.md
Difficulty: Medium
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Goal: compare two months of orders and report:
   - all unique SKUs sold across both months
   - SKUs that sold in BOTH months (loyal demand)
   - SKUs that sold last month but NOT this month (churned)

Expected output:
    Unique SKUs total : 5
    Sold both months  : 2
    Churned this month: 1
"""

last_month = ["WIDGET-RED", "WIDGET-RED", "GADGET-BLUE", "BOLT-12"]
this_month = ["WIDGET-RED", "GADGET-BLUE", "PIPE-XL"]

last_set = set(last_month)
this_set = set(this_month)

all_skus = last_set | this_set
both_months = last_set & this_set
churned = last_set - this_set

print(f"Unique SKUs total : {len(all_skus)}")
print(f"Sold both months  : {len(both_months)}")
print(f"Churned this month: {len(churned)}")
