# Week 2 Project — Inventory Reorder-Flag Script

## What you're building

A script that takes a hard-coded list of inventory items and produces a reorder report.

You're going to use **dicts**, **loops**, and **functions** — and the result will look genuinely useful.

## Spec

Given:

```python
INVENTORY = [
    {"sku": "W-001", "name": "Widget A", "stock": 120, "weekly_sales": 30, "lead_time_weeks": 2},
    {"sku": "W-002", "name": "Widget B", "stock": 8,   "weekly_sales": 6,  "lead_time_weeks": 4},
    {"sku": "W-003", "name": "Widget C", "stock": 45,  "weekly_sales": 10, "lead_time_weeks": 1},
    {"sku": "W-004", "name": "Widget D", "stock": 0,   "weekly_sales": 5,  "lead_time_weeks": 3},
    {"sku": "W-005", "name": "Widget E", "stock": 200, "weekly_sales": 12, "lead_time_weeks": 2},
]
```

For each item, compute:

- **Weeks of stock** = `stock / weekly_sales`
- **Reorder needed** if `weeks_of_stock < lead_time_weeks * 1.5`  (1.5× safety buffer)

Output a report:

```
INVENTORY REPORT
================
W-001  Widget A    stock 120   ~4.0 wk cover   OK
W-002  Widget B    stock   8   ~1.3 wk cover   ⚠️  REORDER (need lead time 4 wk)
W-003  Widget C    stock  45   ~4.5 wk cover   OK
W-004  Widget D    stock   0   ~0.0 wk cover   ⚠️  REORDER (need lead time 3 wk)
W-005  Widget E    stock 200   ~16.7 wk cover  OK

Summary: 2 of 5 items need reordering.
```

## Required structure

You **must** define and use at least these two functions:

```python
def weeks_of_cover(item) -> float:
    ...

def needs_reorder(item, safety=1.5) -> bool:
    ...
```

The main script should loop through `INVENTORY`, call these functions, and print the report.

## File to create

`01-foundations/week-2/inventory_report.py`

## Done when

- The output matches the format above (column alignment doesn't have to be perfect).
- The summary count is correct.
- You used the two functions defined above.
- Edge case: `weekly_sales == 0` should not crash — treat as "infinite cover" → OK.

🛠️ Stretch: read the inventory from a CSV file instead of a hard-coded list. (Preview of week 3.)
