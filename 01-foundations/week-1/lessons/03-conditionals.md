# Lesson 3 — Conditionals

## 🧠 The big idea

Business is full of rules:

- *If revenue > target, pay bonus.*
- *If margin < 10%, flag for review.*
- *If customer is new and order > $500, send welcome gift.*

In Excel: `=IF(A1 > 1000, "ok", "review")`.
In Python: `if`, `elif`, `else`.

---

## The basic shape

```python
revenue = 120_000
target = 100_000

if revenue > target:
    print("Above target. Pay bonus.")
else:
    print("Below target. No bonus.")
```

Note the **colon** at the end of the `if` line, and the **indentation** of the next line. Python uses indentation (4 spaces) to know what's "inside" the if.

📍 **VSCode auto-indents.** Trust it. Don't mix tabs and spaces.

---

## Multiple branches

```python
margin = 8.5

if margin >= 20:
    grade = "Excellent"
elif margin >= 10:
    grade = "Healthy"
elif margin >= 0:
    grade = "Thin"
else:
    grade = "Loss-making"

print(f"Margin {margin}% → {grade}")
```

`elif` = "else if". Python checks each condition top to bottom and takes the **first one that's True**.

---

## Comparison operators

| Operator | Meaning |
|---|---|
| `==` | equal to |
| `!=` | not equal |
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal |
| `<=` | less than or equal |

⚠️ `=` assigns. `==` compares. Forgetting this is the #1 beginner bug.

---

## Combining conditions

```python
new_customer = True
order_value = 750

if new_customer and order_value > 500:
    print("Send welcome gift")

if new_customer or order_value > 1000:
    print("Send a thank-you email")

if not new_customer:
    print("Existing customer flow")
```

| Operator | Excel equivalent |
|---|---|
| `and` | `AND(...)` |
| `or` | `OR(...)` |
| `not` | `NOT(...)` |

---

## 🛠️ Try it

Run the code below, then change the numbers to see each status appear.

```python
revenue = 1_500_000
costs = 1_200_000

profit = revenue - costs
margin = profit / revenue * 100

if margin >= 20:
    status = "strong"
elif margin >= 10:
    status = "okay"
else:
    status = "weak"

print(f"Margin: {margin:.1f}% — {status}")
```

---

## Common confusions

**`IndentationError: expected an indented block`** — your `if` has no body. Indent the next line.

**Code inside the `if` runs even when condition is False** — you de-indented too early. The body must stay indented.

**`if revenue = 100`** — that's `=` (assignment). You want `==` (comparison).

---

## 📚 Resources

**Official docs**
- [Tutorial — `if` statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Boolean operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)

**Deep dives**
- [Real Python — Conditional statements](https://realpython.com/python-conditional-statements/)

**Video tutorials**
- [YouTube — Python if/elif/else explained](https://www.youtube.com/results?search_query=python+if+elif+else+tutorial)


---

Next: [`04-strings.md`](04-strings.md).

---

## 🏋️ Practice

### Easy

Given `revenue = 95_000`, `target = 100_000`, and `has_violation = False`, print `"Full bonus"`, `"Partial bonus"`, or `"No bonus"` using the following rules: full bonus requires `revenue >= target` and no violation; partial bonus requires `revenue >= 0.9 * target` and no violation; otherwise no bonus.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex04_bonus_eligibility.py)

### Medium

Compute gross margin as `(revenue - cost) / revenue * 100`. Then classify it as `"Excellent"` (≥ 20%), `"Healthy"` (≥ 10%), `"Thin"` (≥ 0%), or `"Loss-making"` (< 0%). Print the margin and grade on one line.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex03_grade_margin.py)

### Hard

A consultant earns a tip based on project size and client satisfaction. The rules involve combining `and`/`or`/`not`, multiple `elif` branches, and percent arithmetic. Given `project_value`, `satisfaction_score` (1–5), and `returning_client` (bool), decide the tip rate: 15% if satisfied returning client, 10% if satisfied new client, 5% if dissatisfied returning, 0% otherwise. Print the dollar tip.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex05_tip_calculator.py)
