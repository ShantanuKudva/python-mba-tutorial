# Lesson 2 — Dictionaries

## The big idea

A **dict** is a labeled box. Instead of looking things up by position (like a list), you look them up by **name** (called a *key*).

```python
product = {
    "name": "Widget A",
    "price": 9.99,
    "stock": 120,
    "supplier": "Acme",
}

print(product["name"])      # Widget A
print(product["price"])     # 9.99
```

Update or add:

```python
product["price"] = 11.99
product["category"] = "small parts"
```

Safe access (won't crash if key missing):

```python
warranty = product.get("warranty", "no warranty")
```

Remove:

```python
del product["supplier"]
```

---

## A list of dicts ≈ an Excel sheet

This shape is the bridge to pandas. Memorize it:

```python
inventory = [
    {"sku": "W-001", "name": "Widget A", "price": 9.99,  "stock": 120},
    {"sku": "W-002", "name": "Widget B", "price": 14.50, "stock": 8},
    {"sku": "W-003", "name": "Widget C", "price": 7.00,  "stock": 45},
]
```

Loop through them:

```python
for row in inventory:
    print(f"{row['sku']}: ${row['price']:.2f}  (stock {row['stock']})")
```

Filter low stock:

```python
for row in inventory:
    if row["stock"] < 50:
        print(f"⚠️  {row['name']} is low: only {row['stock']} left")
```

🧠 This is exactly what a `for` loop + `if` does in pandas — just with one line of pandas code instead of seven.

---

## Iterating keys / values

```python
for key, value in product.items():
    print(f"{key} → {value}")
```

---

## Common confusions

**`KeyError: 'foo'`** — that key doesn't exist. Use `.get(key, default)` if it might not.

**Mutable default trap** — out of scope for now, but if you find yourself confused why a dict is "shared," ask.

---

Next: [`03-comprehensions.md`](03-comprehensions.md).
