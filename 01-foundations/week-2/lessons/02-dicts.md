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

## 📚 Resources

**Official docs**
- [Tutorial — dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [`dict` reference](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

**Deep dives**
- [Real Python — Dictionaries](https://realpython.com/python-dicts/)

**Video tutorials**
- [YouTube — Corey Schafer: dictionaries](https://www.youtube.com/results?search_query=corey+schafer+python+dictionaries)


---

Next: [`03-comprehensions.md`](03-comprehensions.md).

---

## 🏋️ Practice

### Easy

Create a dict representing a single product (name, price, stock, supplier). Print each key and value on a separate line using `.items()`. Use `.get()` with a default to safely look up a key that does not exist.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex03_customer_dict.py)

### Medium

Given a list of inventory dicts, loop through and print a warning for any item whose stock is below 50. Then add a `"reorder"` key set to `True` for each flagged item. Print only the flagged items at the end.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex04_inventory_search.py)

### Hard

Build a word-frequency counter from a multi-word string using a dict and `.get()`. Then sort the dict by frequency descending (hint: `sorted(d.items(), key=lambda x: x[1], reverse=True)`). Print the top 5 words and their counts in a right-aligned table.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex08_word_count.py)
