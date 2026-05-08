# Lesson 3 — List Comprehensions

## The big idea

A list comprehension turns a loop **plus** a condition **plus** a transformation into one line.

```python
prices = [9.99, 14.50, 7.00, 22.00]

# Old way:
high_prices = []
for p in prices:
    if p > 10:
        high_prices.append(p)

# Comprehension way:
high_prices = [p for p in prices if p > 10]
```

Read left to right: *"give me `p` for each `p` in `prices`, but only if `p > 10`."*

---

## With a transformation

```python
# Convert to cents
cents = [int(p * 100) for p in prices]   # [999, 1450, 700, 2200]

# Apply a discount
discounted = [round(p * 0.9, 2) for p in prices]
```

---

## With a list of dicts

```python
inventory = [
    {"sku": "W-001", "name": "Widget A", "stock": 120},
    {"sku": "W-002", "name": "Widget B", "stock": 8},
    {"sku": "W-003", "name": "Widget C", "stock": 45},
]

low_stock_skus = [row["sku"] for row in inventory if row["stock"] < 50]
# ['W-002', 'W-003']
```

🧠 This is *one line*. In Excel you'd be filtering, copying, pasting. Here it's a single expression you can save in a function.

---

## When NOT to use comprehensions

- When the logic gets complex (more than one `if`, or anything that doesn't fit on a line). Use a regular loop.
- When you don't actually need a list — just looping for side effects (like `print`). Use a regular `for` loop.

---

Next: [`04-functions.md`](04-functions.md).
