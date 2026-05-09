"""
Exercise 6 — Walk a list of file metadata.

Concepts: list of dicts, loops, formatted output, string methods.
Lesson: 01-foundations/week-3/lessons/05-pathlib-and-json.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson for
official docs, deep dives, and video tutorials.

Goal: given a simulated directory listing (list of dicts with name and size),
print every CSV file's name and size in bytes.

# (Browser note: this uses an in-memory list instead of scanning a real folder.)

Expected output:
    sample_expenses.csv   — 318 bytes
    q1_sales.csv          — 204 bytes
"""

# Setup — simulated directory listing (what pathlib.rglob would return on disk).
file_listing = [
    {"name": "sample_expenses.csv", "size": 318},
    {"name": "helpers.py",          "size": 142},
    {"name": "q1_sales.csv",        "size": 204},
    {"name": "README.md",           "size": 876},
    {"name": "ex01_read_text.py",   "size": 512},
]

for entry in file_listing:
    if entry["name"].endswith(".csv"):
        print(f"{entry['name']:<22} — {entry['size']} bytes")
