"""
Exercise 7 — Build and parse a JSON quarterly report.

Concepts: json.dumps, json.loads, dict operations, formatted output.
Lesson: 01-foundations/week-3/lessons/05-pathlib-and-json.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal:
  1. Serialise the report dict to a JSON string using json.dumps.
  2. Parse it back with json.loads.
  3. Compute and print the total revenue.

# (Browser note: this serialises to a string rather than writing to disk.)

Expected output:
    JSON length: <some number> characters
    Q1 total revenue: $3,635,000
"""

import json

# Setup — the report dict to serialise.
report = {
    "quarter": "Q1",
    "currency": "USD",
    "regions": {
        "North": 1_245_000,
        "South":   980_000,
        "East":  1_410_000,
    },
}

json_str = json.dumps(report, indent=2)
print(f"JSON length: {len(json_str)} characters")

data = json.loads(json_str)

total = sum(data["regions"].values())
print(f"Q1 total revenue: ${total:,.0f}")
