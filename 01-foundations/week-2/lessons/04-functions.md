# Lesson 4 — Functions

## The big idea

A function is a **named, reusable** chunk of logic. Inputs go in, an output comes out.

```python
def gross_margin(revenue, cost):
    return (revenue - cost) / revenue * 100

print(gross_margin(1_000_000, 750_000))   # 25.0
print(gross_margin(500_000, 480_000))     # 4.0
```

You write the formula **once**, use it everywhere.

---

## Anatomy

```python
def function_name(parameter1, parameter2):
    # body
    return some_value
```

- `def` keyword.
- Name (snake_case).
- Parentheses with parameters (zero or more).
- Colon, indented body.
- `return` sends a value back. Without it, the function returns `None`.

---

## Default values

```python
def apply_discount(price, rate=0.10):
    return price * (1 - rate)

apply_discount(100)         # 90.0  (uses default 10%)
apply_discount(100, 0.20)   # 80.0
```

---

## Multiple returns (via tuple)

```python
def split_revenue(total, tax_rate=0.18):
    tax = total * tax_rate
    net = total - tax
    return net, tax

net, tax = split_revenue(1180)
print(net, tax)   # 967.6 212.4
```

---

## Why this matters

Once you write `gross_margin(...)`, you can call it from:

- A loop over a list of products.
- A pandas `.apply()` (week 4).
- A FastAPI endpoint (week 11).

Same function, three contexts. **That's the point of functions.**

---

## 🛠️ Try it

```python
def is_low_stock(product, threshold=50):
    return product["stock"] < threshold

inventory = [
    {"name": "A", "stock": 80},
    {"name": "B", "stock": 12},
    {"name": "C", "stock": 200},
]

low = [p for p in inventory if is_low_stock(p)]
print(low)
```

---

## Common confusions

**Forgot `return`** — function "works" but every call gives `None`.

**Calling without parentheses** — `gross_margin` (no parens) refers to the function itself, doesn't run it. You wanted `gross_margin(rev, cost)`.

**Indentation** — body must be indented under `def`. VSCode handles this.

---

## 📚 Resources

**Official docs**
- [Tutorial — defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Default args, *args, **kwargs](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)

**Deep dives**
- [Real Python — Defining functions](https://realpython.com/defining-your-own-python-function/)
- [Real Python — *args and **kwargs](https://realpython.com/python-kwargs-and-args/)

**Video tutorials**
- [YouTube — Corey Schafer: functions](https://www.youtube.com/results?search_query=corey+schafer+python+functions)


---

Next: [`05-tuples-and-sets.md`](05-tuples-and-sets.md).
