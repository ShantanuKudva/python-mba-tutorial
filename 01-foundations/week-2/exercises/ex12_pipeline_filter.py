"""
Exercise 12 — Sales-pipeline filter and summary.

Concepts: list of dicts, multiple conditions, comprehensions, functions.
Lesson: 01-foundations/week-2/lessons/03-comprehensions.md
Difficulty: Hard
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: given a sales pipeline (list of opportunity dicts), filter to qualified
deals and compute: total expected value, average deal size, and largest deal.

A deal is "qualified" if:
  - stage is "Proposal" or "Negotiation"
  - probability >= 0.5
  - value >= 10_000

Expected output:
    Qualified deals: 3

    Deal                       Stage       Value    Probability
    ------------------------------------------------------------------
    Enterprise SaaS            Negotiation   $85,000       75%
    Analytics Platform         Proposal      $42,000       60%
    Data Warehouse             Negotiation   $38,000       80%
    ------------------------------------------------------------------
    Total expected value: $136,500
    Average deal size   :  $55,000
    Largest deal        : Enterprise SaaS ($85,000)
"""

# Setup — sales pipeline data.
pipeline = [
    {"name": "Enterprise SaaS",    "stage": "Negotiation", "value": 85_000, "probability": 0.75},
    {"name": "SMB Starter",        "stage": "Prospecting", "value":  8_000, "probability": 0.30},
    {"name": "Analytics Platform", "stage": "Proposal",    "value": 42_000, "probability": 0.60},
    {"name": "Quick Win",          "stage": "Proposal",    "value":  5_000, "probability": 0.80},
    {"name": "Data Warehouse",     "stage": "Negotiation", "value": 38_000, "probability": 0.80},
    {"name": "Consulting Project", "stage": "Closed",      "value": 25_000, "probability": 1.00},
    {"name": "Gov Contract",       "stage": "Proposal",    "value": 15_000, "probability": 0.40},
]

# 🛠️ Step 1: use a list comprehension to filter to qualified deals.
#    qualified = [d for d in pipeline
#                 if d["stage"] in ("Proposal", "Negotiation")
#                 and d["probability"] >= 0.5
#                 and d["value"] >= 10_000]

# 🛠️ Step 2: print the count and the table header.

# 🛠️ Step 3: loop over qualified and print each row with aligned columns.

# 🛠️ Step 4: compute and print the three summary statistics.
#    total_ev  = sum(d["value"] * d["probability"] for d in qualified)
#    avg_size  = sum(d["value"] for d in qualified) / len(qualified)
#    top_deal  = max(qualified, key=lambda d: d["value"])
