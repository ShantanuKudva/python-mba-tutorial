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

## 📚 Resources

**Official docs**
- [Tutorial — list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [Tutorial — dict & set comprehensions](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

**Deep dives**
- [Real Python — list comprehensions](https://realpython.com/list-comprehension-python/)

**Video tutorials**
- [YouTube — list comprehensions](https://www.youtube.com/results?search_query=python+list+comprehension+tutorial)


---

Next: [`04-functions.md`](04-functions.md).

---

## 🏋️ Practice

### Easy

Use a list comprehension to filter a list of prices, keeping only those above $10. Then create a second comprehension that applies a 10% discount to every price in the original list. Print both results.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex02_filter_high_value.py)

### Medium

Given a list of customer dicts (each with `"name"`, `"revenue"`, `"region"`), write one comprehension that extracts only the names of customers whose revenue exceeds $5,000. Write a second comprehension that builds a new list of dicts with a `"tier"` key added (`"Gold"` for revenue ≥ $10,000, `"Silver"` otherwise).

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex06_top_n_customers.py)

### Hard

Given a list of raw SKU strings like `["W-001", "S-002", "W-003", "S-001"]`, use comprehensions to: (1) extract only Widget SKUs (starting with `"W"`), (2) build a dict mapping each SKU to its integer suffix (`{"W-001": 1, "W-003": 3}`), and (3) extract a sorted list of unique prefix letters across all SKUs. Combine all three in one script.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex07_unique_skus.py)
