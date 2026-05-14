# Lesson 5 — Loops

## 🧠 The big idea

In Excel, summing a column means typing `=SUM(B2:B13)`. What happens when your data has 10,000 rows — or you need to do something *different* for each row? That's where loops come in.

A loop lets Python **repeat a block of code** — once per item, or until a condition stops it.

---

## `for` loops — iterate over a sequence

The most common loop: do something **for each item** in a list (or a range of numbers).

```python
monthly_revenue = [82_000, 91_500, 78_000, 105_000, 98_000, 112_000]

total = 0
for rev in monthly_revenue:
    total += rev

print(f"Total revenue: ${total:,}")
# Total revenue: $567,500
```

Use `range(n)` when you need to repeat something `n` times, or loop by index:

```python
# Print week numbers
for week in range(1, 5):
    print(f"Week {week}")
```

Use `enumerate` to get both the index and the value — perfect for ranked output:

```python
products = ["Laptop Bag", "Keyboard", "Monitor Stand"]
revenue  = [18_400, 9_200, 6_750]

for rank, (name, rev) in enumerate(zip(products, revenue), start=1):
    print(f"#{rank}  {name:<16}  ${rev:>7,}")
```

---

## `while` loops — repeat until a condition is False

Use `while` when you don't know in advance how many iterations you need.

```python
budget = 50_000
spend  = 0
month  = 1

while spend < budget:
    spend += 8_500        # monthly operating cost
    month += 1

print(f"Budget runs out in month {month}")
```

---

## `break` and `continue`

`break` exits the loop immediately. `continue` skips the rest of the current iteration and moves to the next.

```python
monthly_profit = [12_000, -3_500, 8_200, -1_100, 5_500]

# Find the first loss-making month
for i, profit in enumerate(monthly_profit, start=1):
    if profit < 0:
        print(f"First loss: month {i}  (${profit:,})")
        break

# Sum only the profitable months
total_profit = 0
for profit in monthly_profit:
    if profit < 0:
        continue          # skip losses
    total_profit += profit

print(f"Total profit (profitable months only): ${total_profit:,}")
```

---

## The `else` clause on a loop

A loop can have an `else` block that runs **only if the loop finished without hitting `break`**. Handy for "not found" logic.

```python
target_sku = "WIDGET-C"
inventory  = ["WIDGET-A", "WIDGET-B", "WIDGET-D"]

for sku in inventory:
    if sku == target_sku:
        print(f"Found {target_sku} in inventory.")
        break
else:
    print(f"{target_sku} is out of stock — reorder needed.")
# WIDGET-C is out of stock — reorder needed.
```

---

## 🛠️ Try it

Run this to compute total and average revenue, then adapt it to find the highest and lowest months.

```python
monthly_revenue = [82_000, 91_500, 78_000, 105_000, 98_000, 112_000]

total = 0
for rev in monthly_revenue:
    total += rev

average = total / len(monthly_revenue)
print(f"Total  : ${total:,}")
print(f"Average: ${average:,.0f}")
```

---

## Common confusions

**Infinite `while` loop** — if the condition never becomes `False`, the loop runs forever. Always make sure something in the loop changes the condition variable.

**Off-by-one with `range`** — `range(1, 7)` gives `1, 2, 3, 4, 5, 6` — the end is *excluded*.

**`continue` vs `break`** — `continue` skips one iteration; `break` exits the whole loop.

---

## 📚 Resources

**Official docs**
- [Tutorial — `for` statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Tutorial — `while` and `break`](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)
- [`range()` built-in](https://docs.python.org/3/library/stdtypes.html#range)
- [`enumerate()` built-in](https://docs.python.org/3/library/functions.html#enumerate)

---

Next: [`06-operators-and-math.md`](06-operators-and-math.md).

---

## 🏋️ Practice

### Easy

Given a list of six monthly revenue figures, use a `for` loop to compute the total and then print it. Then use `range()` to print "Month 1 through Month 6" on separate lines.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex10_sum_revenue.py)

### Medium

Given a list of monthly profits (some negative), use a `for` loop with `continue` to sum only the profitable months, count them, and compute the average profit per profitable month. Print a three-line summary.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex11_profitable_months.py)

### Hard

Use a `while` loop and `break` to simulate drawing down a marketing budget month by month. Each month has a known spend. Stop when the budget would go negative, then report which month caused the shortfall and how much remained at the end of the last fully-funded month.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex12_budget_burndown.py)
