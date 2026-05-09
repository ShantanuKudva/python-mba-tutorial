"""
Exercise 3 — Build and query a customer dict.

Concepts: dicts, key access, .get() with default.
Lesson: 01-foundations/week-2/lessons/02-dicts.md
Difficulty: Easy
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: build a dict for a customer, print a formatted summary line, and
use .get() to safely access an optional field.

Expected output:
    Acme Corp (gold) — LTV $125,000
    Phone: n/a
"""

# 🛠️ Step 1: build the customer dict with keys:
#    name, tier, ltv.  (e.g. {"name": "Acme Corp", "tier": "gold", "ltv": 125_000})

# 🛠️ Step 2: print the formatted summary line.
#    print(f"{customer['name']} ({customer['tier']}) — LTV ${customer['ltv']:,}")

# 🛠️ Step 3: use .get("phone", "n/a") to safely retrieve the optional phone
#    field, then print:  print(f"Phone: {phone}")
