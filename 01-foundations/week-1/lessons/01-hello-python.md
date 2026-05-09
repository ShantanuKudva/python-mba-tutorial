# Lesson 1 — Hello, Python

## 🧠 Why this lesson exists

Before writing anything fancy, you need to be 100% sure you can:

1. Open a file.
2. Run it.
3. See the output.

That's it. This entire lesson is about making sure that loop works.

---

## Your first script

Open `lessons/hello.py` (already created next to this file). It contains:

```python
print("Hello, Python!")
print(2 + 2)
print("MBA cohort", 2026)
```

### Run it from the terminal

```bash
python 01-foundations/week-1/lessons/hello.py
```

You should see:

```
Hello, Python!
4
MBA cohort 2026
```

📍 If you don't, go back to [`00-setup/README.md`](../../../00-setup/README.md). Don't continue until this works.

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

## 🛠️ Your turn

Edit `hello.py` and add a line that prints your name. Save. Re-run. Confirm you see your name in the output.

Then commit:

```bash
git add 01-foundations/week-1/lessons/hello.py
git commit -m "week 1 lesson 1 — first script"
```

---

## Common confusions

**"It says SyntaxError."** You probably forgot a quote or a parenthesis. Python is picky. Read the line number it tells you and fix it.

**"It says command not found: python."** On macOS try `python3` instead. Or your `.venv` isn't activated.

**"Nothing happens when I run it."** You ran it but VSCode opened a new terminal. Look in the terminal panel (Ctrl+`).

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
