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

### More to try

**Slicing + `enumerate`** — given the prices below, print the *top 3* with their rank:

```python
prices = [9.99, 14.50, 7.00, 22.00, 3.49, 18.75]
sorted_prices = sorted(prices, reverse=True)

# 🛠️ Use enumerate on sorted_prices[:3] to print:
#   "#1: $22.00", "#2: $18.75", "#3: $14.50"
```

**`max` / `min` with parallel lists** — find the priciest product by name:

```python
products = ["Widget A", "Widget B", "Widget C", "Widget D"]
prices   = [9.99, 14.50, 7.00, 22.00]

# 🛠️ Find the index of max(prices), then look up products[that_index].
# Hint: prices.index(max(prices))
```

**Mutation** — start with an empty cart, append 3 items, replace item at index 1, then remove one:

```python
cart = []
# 🛠️ append "Notebook", "Pen", "Eraser"
# 🛠️ replace cart[1] with "Blue Pen"
# 🛠️ remove "Eraser"
# print(cart)  # ["Notebook", "Blue Pen"]
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
