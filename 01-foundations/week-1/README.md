# Week 1 — Setup + Python Basics

**Goal of the week:** install everything, run your first Python script, and write your first calculator.

**Time budget:** ~6 hours total. Roughly 1 hour/day for 6 days.

---

## What you'll learn

- How to run a Python file from the terminal and from VSCode.
- Variables, types (`int`, `float`, `str`, `bool`).
- Arithmetic, string operations, f-strings.
- `if / elif / else`.
- Comparison and logical operators.

## Why it matters (MBA tie-in)

Every Excel formula is essentially: take some inputs, apply logic, return an output. Python lets you do the same thing — but reusable, version-controlled, and capable of handling **thousands of rows** instead of "the one workbook on your desktop."

By Friday this week, you will have built a CLI break-even calculator. That same logic, with two more weeks of pandas added on top, is how a real revenue forecasting tool starts.

---

## Map

| File | What's there |
|---|---|
| [`lessons/01-hello-python.md`](lessons/01-hello-python.md) | Run your first script. |
| [`lessons/02-variables-and-types.md`](lessons/02-variables-and-types.md) | The four basic types you'll use 99% of the time. |
| [`lessons/03-conditionals.md`](lessons/03-conditionals.md) | If/elif/else — the engine of every business rule. |
| [`lessons/04-strings.md`](lessons/04-strings.md) | String methods, slicing, f-strings + format spec. |
| [`exercises/`](exercises/) | 8 problems. Try them all. |
| [`project.md`](project.md) | Build the break-even CLI. |

Every lesson ends with a **📚 Resources** block — official docs, a deep-dive read, and curated YouTube searches.

---

## Suggested daily plan

| Day | What to do |
|---|---|
| 1 | Read lesson 1. Run `hello.py`. Commit. |
| 2 | Read lesson 2. Do exercises 1 and 2. |
| 3 | Read lesson 3. Do exercises 3 and 4. |
| 4 | Read lesson 4 (strings). Do exercises 5, 6, 7. |
| 5 | Exercise 8 + skim project.md. Sketch inputs/outputs on paper. |
| 6 | Build the project (first pass). |
| 7 | Polish the project. Commit. Move to week 2. |

---

## How to run a Python file

From the terminal, with `.venv` activated:

```bash
python 01-foundations/week-1/lessons/hello.py
```

Or in VSCode: open the file, press the ▶️ "Run Python File" button (top-right).

---

## Checklist before moving to Week 2

- [ ] You can run a `.py` file without thinking about it.
- [ ] You know the difference between `=` (assignment) and `==` (comparison).
- [ ] You've used an f-string at least once: `f"Hello {name}"`.
- [ ] You finished the break-even project.
- [ ] You committed your code with git at least 3 times.
