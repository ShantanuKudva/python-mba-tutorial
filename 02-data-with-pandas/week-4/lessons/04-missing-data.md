# Lesson 4 — Missing Data

Real Excel files have blanks, typos, "N/A" strings, and stray spaces. pandas calls missing values `NaN` (Not a Number).

## Detecting

```python
df.isna()                # element-wise mask
df.isna().sum()          # count of NaNs per column
df["price"].isna().sum() # NaNs in one column
```

## Dropping

```python
df.dropna()                          # drop any row with any NaN
df.dropna(subset=["price", "stock"]) # drop only if these are NaN
```

## Filling

```python
df["price"].fillna(0)
df["category"].fillna("Unknown")
df["price"].fillna(df["price"].median())
```

## Converting "N/A" strings to real NaN

```python
df = pd.read_excel("file.xlsx", na_values=["N/A", "n/a", "?", "-"])
```

Or after the fact:

```python
df = df.replace({"N/A": pd.NA, "?": pd.NA})
```

## Strip whitespace from text columns

```python
df["category"] = df["category"].str.strip()
```

## When to fill vs drop

- **Drop** when a missing value means the row is meaningless.
- **Fill** when there's a sensible default (zero, mean, "Unknown").
- Decide deliberately. Document why.

---

Done with week 4 lessons. Move to [`exercises/`](../exercises/) and [`project.md`](../project.md).

---

## 🏋️ Practice

### Easy

Create a DataFrame that has several `NaN` values. Use `isna().sum()` to count missing values per column. Then fill the numeric column's `NaN` with the column's median and the text column's `NaN` with `"Unknown"`.

[▶ Open exercise](#play/02-data-with-pandas/week-4/exercises/ex04_missing.py)

### Medium

Read a DataFrame from `sample_pl.xlsx`. Identify columns with missing values. Drop rows where the primary numeric column is `NaN`. For remaining rows, fill text-column `NaN` values with `"Unclassified"`. Print the shape before and after cleaning.

[▶ Open exercise](#play/02-data-with-pandas/week-4/exercises/ex04_missing.py)

### Hard

Build a DataFrame with intentional gaps: some rows missing `price`, some missing `category`, some missing both. Write a cleaning function that: (a) fills `price` with the median, (b) fills `category` with `"Unknown"`, (c) logs a warning for every row where both were missing, and (d) returns the cleaned DataFrame. Call the function and print the final shape and `isna().sum()` to confirm no NaNs remain.

[▶ Open exercise](#play/02-data-with-pandas/week-4/exercises/ex04_missing.py)

---

## 📚 Resources

**Official docs**
- [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [`DataFrame.fillna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html)
- [`DataFrame.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)

**Deep dives**
- [Real Python — handling missing data](https://realpython.com/pandas-missing-data/)

**Video tutorials**
- [YouTube — pandas missing data](https://www.youtube.com/results?search_query=pandas+missing+data+fillna+dropna+tutorial)

