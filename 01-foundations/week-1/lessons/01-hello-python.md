# Lesson 1 — Hello, Python

## 🧠 Why this lesson exists

Before writing anything fancy, you need to be 100% sure you can:

1. Click into a code block.
2. Run it.
3. See the output.

That's it. This entire lesson is about making sure that loop works.

---

## Your first script

The code block below is already filled in and ready to run. Click the **▶ Run** button (or press Ctrl+Enter inside the editor):

```python
print("Hello, Python!")
print(2 + 2)
print("MBA cohort", 2026)
```

You should see:

```
Hello, Python!
4
MBA cohort 2026
```

📍 If you see an error instead, check for a typo — Python is picky about quotes and parentheses. Fix it in the editor and click Run again.

---

## What just happened

- **`print(...)`** is a function. It takes whatever you give it inside the parentheses and writes it to your screen.
- **Strings** ("text") are wrapped in quotes: `"Hello"`.
- **Numbers** are not: `2 + 2`.
- Python runs your file **top to bottom**, one line at a time.

---

## The Excel parallel

In Excel, you put `=2+2` in a cell and hit Enter. Excel evaluates it and shows `4`.

In Python, you put `print(2+2)` in a file and run the file. Python evaluates it and prints `4`.

Same idea. The difference: **a Python file is an Excel formula you can save, share, version, and run on a million rows of data**.

---

## 🛠️ Try it

Run the three lines below and see what happens. Then change the strings — try your name, the current year, anything.

```python
print("Hello, Python!")
print(2 + 2)
print("MBA cohort", 2026)
```

---

## Common confusions

**"It says SyntaxError."** You probably forgot a quote or a parenthesis. Python is picky. Read the line number it tells you and fix it.

**"It says `python: command not found`."** In the browser IDE, just click Run — no terminal needed.

**"Nothing happens."** Make sure you clicked Run (or pressed Shift+Enter) inside an editor cell.

---

## 📚 Resources

**Official docs**
- [Python tutorial — using the interpreter](https://docs.python.org/3/tutorial/interpreter.html)
- [`print()` reference](https://docs.python.org/3/library/functions.html#print)

**Deep dives**
- [Real Python — Your first Python program](https://realpython.com/python-first-steps/)

**Video tutorials**
- [YouTube — Corey Schafer: Python beginner setup](https://www.youtube.com/results?search_query=corey+schafer+python+beginner+getting+started)
- [YouTube — Python tutorial for beginners](https://www.youtube.com/results?search_query=python+tutorial+for+beginners+hello+world)


---

Next: [`02-variables-and-types.md`](02-variables-and-types.md).

---

## 🏋️ Practice

### Easy

Print three lines: your name, today's date as a string, and the result of `100 * 3.14`. Confirm all three appear in the output.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex01_age_in_days.py)

### Medium

Given `units_sold = 1200` and `price_per_unit = 49.99`, compute the revenue and print a formatted line that reads `Revenue: $59,988.00`. Use arithmetic and a `print()` call.

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex02_sales_summary.py)

### Hard

Print a three-line "company card" that looks like the example below — with correct spacing, a thousands separator, and a two-decimal currency amount. You will need variables, arithmetic, string concatenation, and f-string format specifiers all at once.

```
Company  : Acme Corp
Quarter  : Q3
Revenue  : $1,245,000.00
```

[▶ Open exercise](#play/01-foundations/week-1/exercises/ex08_growth_rate.py)
