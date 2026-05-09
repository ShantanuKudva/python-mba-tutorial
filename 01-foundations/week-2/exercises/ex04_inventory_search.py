"""
Exercise 4 — Inventory search.

Concepts: list of dicts, loop + if.

Print every product with stock < 30. Format:
    LOW STOCK: <name> (sku <sku>) — only <n> left

📚 References: see the 📚 Resources block at the bottom of the related lesson(s) in `lessons/` for official docs, deep dives, and video tutorials. Global resource index lives in ROADMAP.md.
"""

inventory = [
    {"sku": "W-001", "name": "Widget A", "stock": 120},
    {"sku": "W-002", "name": "Widget B", "stock": 8},
    {"sku": "W-003", "name": "Widget C", "stock": 45},
    {"sku": "W-004", "name": "Widget D", "stock": 22},
    {"sku": "W-005", "name": "Widget E", "stock": 0},
]

# 🛠️ Loop through inventory and print the line for each low-stock item.
