"""
Exercise 6 — Walk a folder and find every CSV.

Concepts: pathlib, .rglob, iteration.
Lesson: lessons/05-pathlib-and-json.md
📚 References: open the lesson above and see its 📚 Resources section at the bottom (official docs, deep dives, video tutorials). Global index in ROADMAP.md.

Goal: starting from THIS exercise folder, find every file whose name
ends in `.csv` (recursively) and print its name and size in bytes.

Expected output (sample):
    sample_expenses.csv  — 318 bytes

Tip: only sample_expenses.csv is shipped here, but your code should
work if more CSVs are added later.
"""

from pathlib import Path

here = Path(__file__).parent

# 🛠️ Step 1: use `here.rglob("*.csv")` and loop over the results.

# 🛠️ Step 2: for each path, get its size with `p.stat().st_size`.

# 🛠️ Step 3: print  f"{p.name}  — {size} bytes"
