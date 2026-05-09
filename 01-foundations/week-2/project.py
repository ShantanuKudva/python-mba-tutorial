"""
Week 2 Project — Inventory Reorder-Flag Report.

Concepts: dicts, lists, loops, functions, formatted output.
Lesson: 01-foundations/week-2/project.md
Difficulty: Hard

Goal: given the inventory list below, compute weeks of cover for each item,
flag those that need reordering (cover < lead_time * 1.5), and print a report.

Expected output:
    INVENTORY REPORT
    ================
    W-001  Widget A    stock 120   ~4.0 wk cover   OK
    W-002  Widget B    stock   8   ~1.3 wk cover   ⚠️  REORDER (need lead time 4 wk)
    W-003  Widget C    stock  45   ~4.5 wk cover   OK
    W-004  Widget D    stock   0   ~0.0 wk cover   ⚠️  REORDER (need lead time 3 wk)
    W-005  Widget E    stock 200   ~16.7 wk cover  OK

    Summary: 2 of 5 items need reordering.
"""

# Setup — inventory data.
INVENTORY = [
    {"sku": "W-001", "name": "Widget A", "stock": 120, "weekly_sales": 30, "lead_time_weeks": 2},
    {"sku": "W-002", "name": "Widget B", "stock":   8, "weekly_sales":  6, "lead_time_weeks": 4},
    {"sku": "W-003", "name": "Widget C", "stock":  45, "weekly_sales": 10, "lead_time_weeks": 1},
    {"sku": "W-004", "name": "Widget D", "stock":   0, "weekly_sales":  5, "lead_time_weeks": 3},
    {"sku": "W-005", "name": "Widget E", "stock": 200, "weekly_sales": 12, "lead_time_weeks": 2},
]

# 🛠️ Step 1: define weeks_of_cover(item) → float.
#    If weekly_sales == 0 return float("inf") (infinite cover → always OK).
#    Otherwise return item["stock"] / item["weekly_sales"].

# 🛠️ Step 2: define needs_reorder(item, safety=1.5) → bool.
#    Return True if weeks_of_cover(item) < item["lead_time_weeks"] * safety.

# 🛠️ Step 3: print the report header.
#    print("INVENTORY REPORT")
#    print("=" * 16)

# 🛠️ Step 4: loop over INVENTORY, compute cover and reorder status, and
#    print each row in the format shown in the docstring.
#    Use ⚠️ for REORDER items, OK for the rest.

# 🛠️ Step 5: count reorder items and print the summary line.
#    reorder_count = sum(1 for item in INVENTORY if needs_reorder(item))
#    print(f"\nSummary: {reorder_count} of {len(INVENTORY)} items need reordering.")
