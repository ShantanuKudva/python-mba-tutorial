# Lesson 1 — Reading and Writing Files

## Reading a text file

```python
with open("notes.txt") as f:
    contents = f.read()

print(contents)
```

`with open(...) as f:` is the safe pattern. Python automatically closes the file when the block ends.

Read line by line (better for large files):

```python
with open("notes.txt") as f:
    for line in f:
        print(line.rstrip())   # rstrip removes the trailing newline
```

## Writing a text file

```python
with open("output.txt", "w") as f:
    f.write("Hello, file!\n")
    f.write("Line two.\n")
```

The `"w"` mode **overwrites**. Use `"a"` to append.

## File paths

```python
from pathlib import Path

data_dir = Path("datasets")
file_path = data_dir / "expenses.csv"

print(file_path.exists())   # True / False
```

🧠 Use `pathlib` rather than string concatenation. It works on Windows and macOS without you thinking about slashes.

## Common confusions

**`FileNotFoundError`** — the path is wrong, or you're running from the wrong directory. Check `Path.cwd()` to see where Python thinks you are.

**File contents look like `\n`** — that's a newline character. `print()` interprets it. `f.write()` requires you to add it explicitly.

---

## 📚 Resources

**Official docs**
- [Tutorial — reading & writing files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [`open()` reference](https://docs.python.org/3/library/functions.html#open)

**Deep dives**
- [Real Python — working with files](https://realpython.com/working-with-files-in-python/)
- [Real Python — read & write files](https://realpython.com/read-write-files-python/)

**Video tutorials**
- [YouTube — Corey Schafer: file objects](https://www.youtube.com/results?search_query=corey+schafer+python+file+objects)


---

Next: [`02-csv.md`](02-csv.md).

---

## 🏋️ Practice

### Easy

Open the sample text file at `exercises/sample_expenses.csv` using the `with open(...)` pattern. Read all the lines into a list. Print the total line count and the first three lines.

[▶ Open exercise](#play/01-foundations/week-3/exercises/ex01_read_text.py)

### Medium

Read a text file line by line. Count the total number of lines and the number of non-blank lines. Write the line count to a new file called `line_count.txt`. Use `pathlib.Path` for the file path so the code works on both Windows and macOS.

[▶ Open exercise](#play/01-foundations/week-3/exercises/ex02_count_lines.py)

### Hard

Given a folder path, walk it recursively using `Path.rglob("*")` and build a dict that maps each file extension to its count (e.g. `{".csv": 3, ".py": 12}`). Sort by count descending and print a formatted table. Handle cases where a file has no extension gracefully.

[▶ Open exercise](#play/01-foundations/week-3/exercises/ex06_path_walk.py)
