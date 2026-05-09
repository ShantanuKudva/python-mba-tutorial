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

customer = {"name": "Acme Corp", "tier": "gold", "ltv": 125_000}

print(f"{customer['name']} ({customer['tier']}) — LTV ${customer['ltv']:,}")

phone = customer.get("phone", "n/a")
print(f"Phone: {phone}")
