"""
Exercise 7 — Write and re-read a JSON quarterly report.

Concepts: json.dumps / json.loads, pathlib.write_text / read_text.
Lesson: lessons/05-pathlib-and-json.md
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Goal:
  1. Build a Python dict describing Q1 revenue by region.
  2. Write it to `q1_report.json` next to this file.
  3. Read it back and print the total revenue.

Expected output:
    Wrote q1_report.json
    Q1 total revenue: $3,635,000
"""

import json
from pathlib import Path

report = {
    "quarter": "Q1",
    "currency": "USD",
    "regions": {
        "North": 1_245_000,
        "South":   980_000,
        "East":  1_410_000,
    },
}

out = Path(__file__).parent / "q1_report.json"

# 🛠️ Step 1: write the report.
#    out.write_text(json.dumps(report, indent=2))

# 🛠️ Step 2: read it back and parse.
#    data = json.loads(out.read_text())

# 🛠️ Step 3: total = sum(data["regions"].values())

# 🛠️ Step 4: print confirmation and total (use ":,.0f" formatting).
