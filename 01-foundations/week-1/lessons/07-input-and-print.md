# Lesson 7 — Input, Print & Comments

## 🧠 The big idea

So far, every value in your scripts has been hard-coded. Real tools ask the user for input and show clear output. This lesson covers the three most-used "communication" tools in Python: `input()`, `print()`, and `#` comments.

---

## `input()` — ask the user for a value

`input()` pauses the program, shows a prompt, and returns whatever the user types as a **string**. In this browser playground, it pops up a small dialog box.

```python
company = input("Enter company name: ")
revenue = float(input("Enter annual revenue ($): "))

margin_target = 0.15
profit = revenue * margin_target

print(f"{company} needs ${profit:,.0f} profit to hit a 15% margin.")
```

Key points:
- `input()` **always returns a string**. Convert with `int()` or `float()` when you need a number.
- The string inside `input(...)` is the prompt text — make it clear so the user knows what to type.

---

## `print()` — control your output

`print()` does more than dump a line. A few options you'll use regularly:

```python
# Multiple values — separated by a space by default
print("Q1", "Q2", "Q3", "Q4")
# Q1 Q2 Q3 Q4

# Custom separator (great for CSV-style output)
print("North", 120_000, 0.183, sep=",")
# North,120000,0.183

# Stay on the same line (no newline at the end)
for label in ["Revenue", "Cost", "Profit"]:
    print(label, end=" | ")
print()   # move to the next line

# Print nothing (a blank spacer line)
print()
```

Use f-strings (from Lesson 4) for formatted numbers inside print:

```python
revenue = 1_245_000
print(f"Revenue: ${revenue:>12,.0f}")
```

---

## `#` Comments — notes for humans

Anything after `#` on a line is ignored by Python. Comments explain *why* code does what it does.

```python
# Company snapshot — Q3 2026
revenue  = 1_245_000   # gross revenue before returns
returns  = 18_500      # customer returns this quarter
net_rev  = revenue - returns

# Gross margin uses net revenue, not gross — per CFO note 2026-03-12
cogs     = 820_000
margin   = (net_rev - cogs) / net_rev * 100
print(f"Net margin: {margin:.1f}%")
```

Good comments:
- Explain *why*, not *what* (the code already shows *what*).
- Note assumptions, data sources, or decisions that aren't obvious.
- Keep them short and current — stale comments are worse than no comments.

---

## Basic debugging with `print()`

When something goes wrong, `print()` is your first diagnostic tool.

```python
units = 1_200
price = 49.99

subtotal = units * price
print(f"[DEBUG] subtotal = {subtotal}")   # check intermediate value

discount = 0.10
total = subtotal - (subtotal - discount)  # bug: wrong formula
print(f"[DEBUG] total = {total}")         # prints 0.1 — spot the bug!

# Fix:
total = subtotal * (1 - discount)
print(f"Total after 10% discount: ${total:,.2f}")
```

**Pattern:** add `[DEBUG]` or `# temp` to print calls you plan to remove — easy to search for later.

---

## 🛠️ Try it

Run this interactive break-even calculator. Enter different values to see the results change.

```python
product  = input("Product name: ")
price    = float(input("Selling price per unit ($): "))
variable = float(input("Variable cost per unit ($): "))
fixed    = float(input("Monthly fixed costs ($): "))

contribution = price - variable
break_even   = fixed / contribution

print()
print(f"--- Break-even for {product} ---")
print(f"Contribution margin : ${contribution:.2f} per unit")
print(f"Break-even volume   : {break_even:,.0f} units/month")
```

---

## Common confusions

**`input()` returns a string** — `age = input("Age: ")` then `age + 1` raises `TypeError`. Always convert: `age = int(input("Age: "))`.

**`float("1,200")`** — fails because of the comma. Strip commas first: `float(revenue_str.replace(",", ""))`.

**Forgetting `end=""`** — if you use `print(..., end="")` in a loop, remember to print a final newline (`print()`) afterwards, or the next output will appear on the same line.

**Comment placement** — comments go *above* the code they describe, or inline at the end of the line. Never below (too easy to miss the connection).

---

## 📚 Resources

**Official docs**
- [`input()` built-in](https://docs.python.org/3/library/functions.html#input)
- [`print()` built-in](https://docs.python.org/3/library/functions.html#print)
- [Comments — PEP 8 style guide](https://peps.python.org/pep-0008/#comments)

**Deep dives**
- [Real Python — Reading user input with `input()`](https://realpython.com/python-input-output/)

---

Next: that's all of week 1's lessons. Head to the [exercises](../exercises/) and [project](../project.md).

---

## 🏋️ Practice

### Easy

Use `input()` to ask for a product name and a unit price. Print a one-line summary: `"Widget A costs $24.99 per unit."` Remember to convert the price to a float before formatting.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex16_product_prompt.py)

### Medium

Ask the user for company name, revenue, and costs. Compute gross margin and print a four-line company snapshot with labels left-aligned in 14 characters and values right-aligned. Add at least two meaningful inline comments in your code.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex17_company_snapshot.py)

### Hard

Build a mini invoice generator. Ask the user for customer name, product name, quantity, and unit price. Apply a 10% bulk discount if quantity >= 100. Use `print()` with `sep` and alignment to print a formatted invoice with line item, subtotal, discount, and total due. Guard against non-numeric input by converting inside a `try/except ValueError`.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex18_invoice_generator.py)
