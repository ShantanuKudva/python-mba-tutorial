# Lesson 1 — Lists and Loops

## Lists

A list is an ordered collection.

```python
products = ["Widget A", "Widget B", "Widget C"]
prices = [9.99, 14.50, 7.00]

print(products[0])     # Widget A   ← Python is 0-indexed
print(products[-1])    # Widget C   ← negative counts from the end
print(len(products))   # 3
```

Modify a list:

```python
products.append("Widget D")    # add to end
products[0] = "Widget A v2"    # replace by index
products.remove("Widget B")    # remove first matching value
```

Slice a list:

```python
products[1:3]    # items at index 1 and 2 (NOT 3)
products[:2]     # first two
products[-2:]    # last two
```

---

## `for` loops

```python
prices = [9.99, 14.50, 7.00]

for price in prices:
    print(f"Price: ${price:.2f}")
```

Loop with index using `enumerate`:

```python
for i, price in enumerate(prices):
    print(f"Item {i + 1}: ${price:.2f}")
```

Loop two lists in parallel using `zip`:

```python
for product, price in zip(products, prices):
    print(f"{product}: ${price:.2f}")
```

---

## Common operations

```python
total = sum(prices)
average = total / len(prices)
highest = max(prices)
lowest = min(prices)
```

---

## 🛠️ Try it

```python
units_per_product = [120, 80, 200, 45]
price_per_product = [10, 25, 5, 50]

revenue = 0
for units, price in zip(units_per_product, price_per_product):
    revenue += units * price

print(f"Total revenue: ${revenue:,}")
```

What if you wanted to skip products that sold less than 50 units? Add an `if` inside the loop.

---

## Common confusions

**`IndexError: list index out of range`** — you asked for `products[5]` on a list with 3 items.

**Modifying a list while looping over it** — don't. Build a new list instead (we'll see how with comprehensions in lesson 3).

---

Next: [`02-dicts.md`](02-dicts.md).
