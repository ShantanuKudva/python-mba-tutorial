"""
Exercise 7 — Unique SKUs and churn analysis.

Concepts: sets, set operations.
Lesson: lessons/05-tuples-and-sets.md
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

# 🛠️ Step 1: convert each list to a set.

# 🛠️ Step 2: union (|) → all unique SKUs across both.

# 🛠️ Step 3: intersection (&) → SKUs in both.

# 🛠️ Step 4: difference (last - this) → churned.

# 🛠️ Step 5: print the three counts using f-strings.
