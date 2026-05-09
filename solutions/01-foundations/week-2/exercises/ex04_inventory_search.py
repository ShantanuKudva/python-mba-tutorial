"""
Exercise 4 — Inventory search.

Concepts: list of dicts, loop + if.
Lesson: lessons/02-dicts.md
Difficulty: Medium
📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.

Goal: print every product with stock < 30 in a warning format.

Expected output:
    LOW STOCK: Widget B (sku W-002) — only 8 left
    LOW STOCK: Widget D (sku W-004) — only 22 left
    LOW STOCK: Widget E (sku W-005) — only 0 left
"""

inventory = [
    {"sku": "W-001", "name": "Widget A", "stock": 120},
    {"sku": "W-002", "name": "Widget B", "stock": 8},
    {"sku": "W-003", "name": "Widget C", "stock": 45},
    {"sku": "W-004", "name": "Widget D", "stock": 22},
    {"sku": "W-005", "name": "Widget E", "stock": 0},
]

for item in inventory:
    if item["stock"] < 30:
        print(f"LOW STOCK: {item['name']} (sku {item['sku']}) — only {item['stock']} left")
