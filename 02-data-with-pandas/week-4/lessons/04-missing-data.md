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
