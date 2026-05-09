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

Run this and confirm the output reads `Revenue: $59,988.00`.

```python
units_sold = 1200
price_per_unit = 49.99
revenue = units_sold * price_per_unit

print(f"Revenue: ${revenue:,.2f}")
```

Try changing the numbers. What happens when `units_sold = 0`?

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

## 📚 Resources

**Official docs**
- [Built-in types (`int`, `float`, `str`, `bool`)](https://docs.python.org/3/library/stdtypes.html)
- [`type()` and `isinstance()`](https://docs.python.org/3/library/functions.html#type)

**Deep dives**
- [Real Python — Basic data types](https://realpython.com/python-data-types/)
- [Real Python — Variables in Python](https://realpython.com/python-variables/)

**Video tutorials**
- [YouTube — Variables & data types](https://www.youtube.com/results?search_query=python+variables+data+types+tutorial)


---

Next: [`03-conditionals.md`](03-conditionals.md).

---

## 🏋️ Practice

### Easy

Store your age in years, compute your approximate age in days (use 365 days/year), and print a sentence like: `A 28-year-old has lived approximately 10220 days.`

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex01_age_in_days.py)

### Medium

Given `quarter = "Q3"`, `units = 1200`, and `price = 49.99`, compute `revenue` and print one formatted line:
`Q3 sales: 1,200 units × $49.99 = $59,988.00`

Use f-strings and format specifiers like `{n:,}` and `{n:,.2f}`.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex02_sales_summary.py)

### Hard

Compute the year-on-year growth rate between two revenues (`rev_current` and `rev_prior`), then print the rate formatted as a percentage with one decimal place. Handle the edge case where `rev_prior` is zero (print `"N/A"` instead of crashing). Finally, print a verdict: `"Strong growth"` if the rate exceeds 15%, `"Moderate growth"` if it is positive, otherwise `"Decline"`.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex08_growth_rate.py)
