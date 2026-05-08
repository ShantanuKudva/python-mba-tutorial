# Lesson 2 — Variables and Types

## 🧠 The big idea

A **variable** is a labeled box that holds a value. You put something in, you take it out by name.

```python
revenue = 1_000_000
cost = 750_000
profit = revenue - cost

print(profit)   # 250000
```

In Excel, `A1` is a variable. The cell holds a value, you reference it by name.
In Python, the *name you choose* is the reference: `revenue`, not `A1`.

---

## The four types you'll use 99% of the time

| Python type | Looks like | Excel-equivalent |
|---|---|---|
| `int` | `42`, `-5`, `1000000` | a whole number cell |
| `float` | `3.14`, `0.07`, `2_500.50` | a decimal cell |
| `str` | `"Acme Corp"`, `'Q3'` | a text cell |
| `bool` | `True`, `False` | TRUE / FALSE |

You can check the type:

```python
print(type(revenue))   # <class 'int'>
print(type("hello"))   # <class 'str'>
```

---

## Arithmetic

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333...   ← always a float
print(a // b)  # 3           ← integer division (floor)
print(a % b)   # 1           ← remainder (modulo)
print(a ** b)  # 1000        ← exponent
```

---

## Strings

```python
company = "Acme"
quarter = "Q3"

# Concatenation
label = company + " " + quarter
print(label)        # Acme Q3

# f-strings (preferred — easier to read)
print(f"{company} reported earnings in {quarter}")

# Multi-line
report = f"""
Company: {company}
Quarter: {quarter}
"""
print(report)
```

🧠 **f-strings** (the `f"..."` ones) are the cleanest way to mix variables and text. Use them.

---

## Type conversion

```python
price_str = "1500"
price = int(price_str)        # 1500 as an integer
print(price + 100)            # 1600

revenue = 1234567
formatted = f"${revenue:,}"   # "$1,234,567"
print(formatted)
```

---

## 🛠️ Try it

Open a new file `scratch.py` anywhere and write:

```python
units_sold = 1200
price_per_unit = 49.99
revenue = units_sold * price_per_unit

print(f"Revenue: ${revenue:,.2f}")
```

Run it. You should see `Revenue: $59,988.00`.

---

## Naming rules

- Use lowercase. Words separated by underscores: `total_revenue`, not `TotalRevenue`.
- Be **descriptive**: `customer_count` beats `c`.
- Don't start with a number: `2024_revenue` is illegal. Use `revenue_2024`.

---

## Common confusions

**`"5" + 5` → TypeError.** A string and an int are different. Convert one: `int("5") + 5`.

**Decimal weirdness:** `0.1 + 0.2` is `0.30000000000000004`. That's floating-point math. Round when displaying: `round(x, 2)`.

**`=` vs `==`:** `=` assigns. `==` compares. We'll meet `==` in lesson 3.

---

Next: [`03-conditionals.md`](03-conditionals.md).
