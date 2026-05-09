# Lesson 3 — Errors and `try/except`

## The big idea

When something can fail, wrap it. If it fails, react instead of crashing.

```python
amount_str = "twelve"
try:
    amount = float(amount_str)
except ValueError:
    print(f"Skipping bad value: {amount_str}")
    amount = 0
```

## The shape

```python
try:
    # risky thing
except SomeError:
    # what to do if that error happens
except AnotherError as exc:
    # exc has details about the error
finally:
    # always runs, error or not (rare)
```

## Common errors you'll meet

| Exception | Meaning |
|---|---|
| `ValueError` | A value is the right type but wrong content (e.g., `int("abc")`). |
| `TypeError` | Wrong type — e.g., adding a string to a number. |
| `KeyError` | Asked a dict for a key that's not there. |
| `IndexError` | Asked a list for an index out of range. |
| `FileNotFoundError` | Path doesn't exist. |
| `ZeroDivisionError` | Divided by zero. |

## When NOT to catch errors

Don't catch them just to silence them. If you don't know how to react, **let it crash** — the traceback is information.

```python
# BAD
try:
    do_something()
except Exception:
    pass   # swallowed silently → impossible to debug
```

## Real-world pattern

```python
import csv

bad_rows = 0
total = 0.0

with open("expenses.csv", newline="") as f:
    for row in csv.DictReader(f):
        try:
            total += float(row["amount"])
        except (ValueError, KeyError):
            bad_rows += 1

print(f"Total: ${total:,.2f}   (skipped {bad_rows} bad rows)")
```

This is exactly how production scripts handle dirty data.

---

## 📚 Resources

**Official docs**
- [Tutorial — errors and exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Built-in exceptions](https://docs.python.org/3/library/exceptions.html)

**Deep dives**
- [Real Python — Exceptions](https://realpython.com/python-exceptions/)

**Video tutorials**
- [YouTube — Corey Schafer: exceptions](https://www.youtube.com/results?search_query=corey+schafer+python+exceptions)


---

Next: [`04-modules.md`](04-modules.md).
