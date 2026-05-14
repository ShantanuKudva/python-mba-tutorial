# Lesson 8 — Arguments and Unpacking

## Default arguments

You already saw default arguments briefly in Lesson 4. The rule is simple: parameters with defaults must come after parameters without defaults.

```python
def invoice_total(subtotal, tax_rate=0.18, discount=0.0):
    after_discount = subtotal * (1 - discount)
    return after_discount * (1 + tax_rate)

print(invoice_total(1_000))                  # 1180.0  — both defaults used
print(invoice_total(1_000, discount=0.10))   # 1062.0  — named arg skips tax_rate
print(invoice_total(1_000, 0.20, 0.05))      # 1140.0  — positional, all three
```

Calling arguments by name (`discount=0.10`) is called a **keyword argument**. It improves readability when a function has several parameters.

---

## `*args` — accept any number of positional arguments

When you don't know how many values will be passed, use `*args`. Inside the function, `args` is a plain tuple.

```python
def total_revenue(*amounts):
    """Sum any number of revenue figures."""
    return sum(amounts)

print(total_revenue(1_000, 2_500, 800))          # 4300
print(total_revenue(500))                         # 500
print(total_revenue(100, 200, 300, 400, 500))     # 1500
```

Real-world use: logging helpers, aggregation utilities, wrappers that forward arguments.

---

## `**kwargs` — accept any number of keyword arguments

`**kwargs` collects extra keyword arguments into a dict.

```python
def create_product(**fields):
    """Build a product dict from any keyword arguments."""
    required = {"name", "price"}
    missing = required - fields.keys()
    if missing:
        raise ValueError(f"Missing required fields: {missing}")
    return fields

p = create_product(name="Widget Alpha", price=9.99, sku="WGT-001", stock=200)
print(p)
# {'name': 'Widget Alpha', 'price': 9.99, 'sku': 'WGT-001', 'stock': 200}
```

You can combine all styles: `def func(required, *args, **kwargs)`.

---

## Tuple unpacking

Unpacking assigns multiple variables from a sequence in one statement.

```python
sale = ("North", "Q1", 12_450)
region, quarter, revenue = sale

print(region)    # North
print(revenue)   # 12450

# Swap two variables — no temp variable needed:
a, b = 10, 20
a, b = b, a
print(a, b)      # 20 10
```

Use `_` (underscore) as a throwaway variable when you need to unpack but don't care about some values.

```python
name, _, price = ("Widget Alpha", "WGT-001", 9.99)  # ignore SKU
print(name, price)  # Widget Alpha 9.99
```

---

## Spread unpacking with `*`

The `*` operator can unpack inside a list or function call.

```python
q1 = [10_000, 12_000, 9_500]
q2 = [11_000, 13_500, 10_200]

all_months = [*q1, *q2]          # combine two lists without .extend()
print(all_months)

# Unpack the first and last, collect the middle:
first, *middle, last = all_months
print(first, last)    # 10000 10200
print(middle)         # [12000, 9500, 11000, 13500]
```

And in function calls — unpack a list as positional args:

```python
def weighted_avg(a, b, c, weights=(1, 1, 1)):
    total_w = sum(weights)
    return (a * weights[0] + b * weights[1] + c * weights[2]) / total_w

scores = [85, 90, 78]
print(weighted_avg(*scores))   # same as weighted_avg(85, 90, 78)
```

---

## Dict unpacking with `**`

```python
defaults = {"region": "North", "currency": "USD", "tax_rate": 0.18}
override = {"region": "South", "discount": 0.10}

merged = {**defaults, **override}   # later keys win
print(merged)
# {'region': 'South', 'currency': 'USD', 'tax_rate': 0.18, 'discount': 0.1}
```

This is how you merge dicts cleanly and pass config dicts to functions.

---

## 🛠️ Try it

Run this to see `*args` and `**kwargs` working together. Try calling `order_summary` with different numbers of items and adding a new keyword argument like `currency="EUR"`.

```python
def order_summary(*items, customer="Unknown", **meta):
    """
    items   — variable number of (name, price) tuples
    customer — keyword-only with a default
    meta    — any extra keyword arguments (region, discount, etc.)
    """
    total = sum(price for _, price in items)
    print(f"Customer : {customer}")
    print(f"Items    : {len(items)}")
    print(f"Total    : ${total:,.2f}")
    for key, val in meta.items():
        print(f"  {key}: {val}")
    return total

order_summary(
    ("Widget A", 9.99),
    ("Widget B", 14.50),
    customer="Acme Corp",
    region="North",
    discount="10%",
)
```

---

## Common confusions

**Order matters in definitions.** Positional → `*args` → keyword-only → `**kwargs`. Python will raise a `SyntaxError` if you mix them up.

**`*args` is a tuple, not a list.** You can iterate over it and index it, but you cannot `append` to it.

**Unpacking a dict vs iterating it.** `for k in my_dict` gives keys. To get key-value pairs use `my_dict.items()`. To spread it into another dict, use `{**my_dict}`.

---

## 📚 Resources

**Official docs**
- [More on defining functions (`*args`, `**kwargs`, default values)](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
- [Unpacking argument lists](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists)

**Deep dives**
- [Real Python — `*args` and `**kwargs`](https://realpython.com/python-kwargs-and-args/)
- [Real Python — Unpacking in Python](https://realpython.com/python-unpacking-generalization/)

---

Next: [exercises](../exercises/) and [project](../project.md).

---

## 🏋️ Practice

### Easy

Write a function `summarize(*revenues)` that accepts any number of revenue figures and prints the count, total, minimum, maximum, and average. Call it three times with different numbers of arguments (one value, three values, six values).

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex19_variadic_summary.py)

### Medium

Write a function `build_report(**fields)` that accepts keyword arguments for `title`, `region`, `quarter`, and `revenue` (all required — raise `ValueError` if any are missing). Use dict unpacking to merge a `defaults` dict with an `overrides` dict and pass the result to `build_report` via `**`. Print the formatted report.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex20_kwargs_report.py)

### Hard

Write a function `process_orders(*orders, tax_rate=0.18, currency="USD")` where each order is a dict with `"customer"`, `"items"` (list of `(name, qty, unit_price)` tuples), and optional `"discount"`. The function must compute each order's subtotal, apply discount if present, add tax, and print a formatted invoice. At the end print the grand total across all orders.

[▶ Open exercise](#play/01-foundations/week-2/exercises/ex21_order_processor.py)
