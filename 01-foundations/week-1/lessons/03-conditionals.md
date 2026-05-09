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

Change the numbers. Re-run. See the status flip.

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
