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

Run this to see `zip` in action with parallel lists. Try skipping products that sold fewer than 50 units by adding an `if` inside the loop.

```python
units_per_product = [120, 80, 200, 45]
price_per_product = [10, 25, 5, 50]

revenue = 0
for units, price in zip(units_per_product, price_per_product):
    revenue += units * price

print(f"Total revenue: ${revenue:,}")
```

---

## Common confusions

**`IndexError: list index out of range`** — you asked for `products[5]` on a list with 3 items.

**Modifying a list while looping over it** — don't. Build a new list instead (we'll see how with comprehensions in lesson 3).

---

## 📚 Resources

**Official docs**

- [Tutorial — lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Tutorial — `for` statement](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [`range()`](https://docs.python.org/3/library/stdtypes.html#range)
- [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate)

**Deep dives**

- [Real Python — Lists & tuples](https://realpython.com/python-lists-tuples/)
- [Real Python — `for` loops](https://realpython.com/python-for-loop/)

**Video tutorials**

- [YouTube — Corey Schafer: lists, tuples, sets](https://www.youtube.com/results?search_query=corey+schafer+python+lists+tuples+sets)
- [YouTube — for loop tutorial](https://www.youtube.com/results?search_query=python+for+loop+tutorial)

---

Next: [`02-dicts.md`](02-dicts.md).

---

## 🏋️ Practice

### Easy

Start with an empty cart list. Append `"Notebook"`, `"Pen"`, `"Eraser"`, `"Mouse"`, and `"Keyboard"`. Then replace the second item with `"Blue Pen"`, remove `"Eraser"`, and insert `"Stapler"` at index 2. Print the final cart and slices of the first two and last two items.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex09_cart_mutation.py)

### Medium

Given a list of six monthly revenue figures, print the latest month and the prior month using negative indexing. Then use `try/except IndexError` to safely look up user-requested month numbers — print a friendly message instead of crashing when a month number is out of range.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex10_safe_lookup.py)

### Hard

Given parallel lists of product names, units sold, and prices, compute total revenue by looping with `zip`. Filter out products with fewer than 50 units sold. Sort the remaining products by revenue descending and print a ranked table using `enumerate`, starting at rank 1. Your output should look like:

```
#1  Widget D    $1,100.00
#2  Widget B    $1,160.00
```

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex01_total_revenue.py)
