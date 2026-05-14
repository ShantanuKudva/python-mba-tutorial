# Lesson 8 — NULLs & Data Types

## Why this matters

NULL is not zero. NULL is not an empty string. NULL is "unknown" — and it follows three-valued logic that breaks most intuitions about filtering and arithmetic. Mishandling NULLs is one of the top sources of silent data quality bugs in analyst SQL. This lesson makes NULL predictable.

---

## What is NULL?

NULL means "no value" or "unknown". It is not a value itself, so:

- `NULL = NULL` is **not TRUE** — it evaluates to NULL (unknown)
- `NULL != NULL` is also **not TRUE** — also NULL
- `1 + NULL` is **NULL** — any arithmetic with NULL produces NULL
- `COUNT(column)` skips NULLs; `COUNT(*)` counts all rows

---

## Setup

```sql
-- 📦 SETUP
DROP TABLE IF EXISTS leads;
CREATE TABLE leads (
    id          INTEGER PRIMARY KEY,
    name        TEXT,
    region      TEXT,
    score       INTEGER,
    assigned_to TEXT,
    revenue_est REAL
);
INSERT INTO leads VALUES
    (1,'Acme Corp','North',  85,'Alice',  50000.0),
    (2,'Globex',  'East',   NULL,'Bob',    NULL),
    (3,'Initech', 'West',    60, NULL,   30000.0),
    (4,'Hooli',   'North',   92,'Alice',  80000.0),
    (5,'Pied Piper','East',  NULL,NULL,    NULL),
    (6,'Stark',   'West',    78,'Carol', 120000.0);
```

---

## IS NULL and IS NOT NULL

Because `= NULL` never evaluates to TRUE, you must use `IS NULL` and `IS NOT NULL`:

```sql
-- Find unscored leads
SELECT id, name
FROM leads
WHERE score IS NULL;

-- Find leads with an assigned rep
SELECT id, name, assigned_to
FROM leads
WHERE assigned_to IS NOT NULL;
```

Never write `WHERE score = NULL` — it returns zero rows even when NULLs exist.

---

## COALESCE — the NULL-to-default converter

`COALESCE(val1, val2, ..., valN)` returns the first non-NULL value in its argument list. Use it wherever you want a fallback.

```sql
-- Treat NULL score as 0 for calculation purposes
SELECT id, name,
       COALESCE(score, 0) AS score_safe,
       COALESCE(assigned_to, 'Unassigned') AS rep,
       COALESCE(revenue_est, 0.0) AS est_revenue
FROM leads;
```

Business use: `COALESCE(discount, 0)` so that rows with no discount don't make calculations explode.

Chaining: `COALESCE(col1, col2, 'default')` — tries col1, falls back to col2, then to the literal string.

---

## NULLIF — produce NULL on a condition

`NULLIF(val1, val2)` returns NULL if the two values are equal, otherwise returns val1. The classic use: prevent divide-by-zero.

```sql
-- Avoid division by zero: treat 0 denominator as NULL
SELECT id, name,
       revenue_est / NULLIF(score, 0) AS revenue_per_score_point
FROM leads;
```

If score is 0, `NULLIF(score, 0)` returns NULL, so the division returns NULL instead of an error.

---

## NULL in aggregates — critical gotcha

```sql
SELECT COUNT(*) AS total_rows,
       COUNT(score) AS scored_leads,
       AVG(score) AS avg_score,
       SUM(revenue_est) AS total_est
FROM leads;
```

- `COUNT(*)` → 6 (counts all rows including NULLs)
- `COUNT(score)` → 4 (skips the two NULL scores)
- `AVG(score)` → average of the 4 non-NULL values only (not divided by 6!)
- `SUM(revenue_est)` → sum of non-NULL values (NULL rows contribute 0)

This means your average can be misleading if you have many NULLs. Always check `COUNT(*)` vs `COUNT(column)` to understand how much data is missing.

---

## NULL in WHERE — the IN / NOT IN trap

```sql
-- Dangerous: if subquery can return NULL, NOT IN returns 0 rows
SELECT name FROM leads
WHERE assigned_to NOT IN ('Alice', NULL);  -- returns nothing!
```

Any comparison with NULL in an IN list poisons the result. Safe alternative:

```sql
SELECT name FROM leads
WHERE assigned_to IS NOT NULL
  AND assigned_to NOT IN ('Alice');
```

---

## Data types in SQLite — type affinity

SQLite uses "type affinity" rather than strict types. Every column has an affinity, but you can store any value type in any column.

| Affinity | Column declared as | Storage |
|---|---|---|
| INTEGER | INT, INTEGER, BIGINT | Whole numbers |
| REAL | REAL, FLOAT, DOUBLE | Floating-point |
| TEXT | TEXT, VARCHAR, CHAR | Strings |
| BLOB | BLOB, none | Raw bytes |
| NUMERIC | NUMERIC, DECIMAL | Int if possible, else REAL |

```sql
-- SQLite allows this (other DBs would reject it):
DROP TABLE IF EXISTS demo;
CREATE TABLE demo (val TEXT);
INSERT INTO demo VALUES (42);     -- stores integer 42 in a TEXT column
SELECT typeof(val) FROM demo;     -- returns 'integer'
```

---

## CAST — explicit type conversion

```sql
SELECT CAST('3.14' AS REAL),         -- text → real
       CAST(3.99 AS INTEGER),         -- real → int (truncates to 3)
       CAST(99 AS TEXT);              -- int → text
```

Use CAST when importing data where columns come in as TEXT but you need numeric operations:

```sql
SELECT id, CAST(revenue_est AS INTEGER) AS revenue_rounded
FROM leads
WHERE revenue_est IS NOT NULL;
```

---

## Key rules to remember

1. Use `IS NULL` / `IS NOT NULL` — never `= NULL`
2. Wrap nullable columns in `COALESCE` before arithmetic
3. Use `NULLIF(x, 0)` to prevent divide-by-zero
4. `COUNT(*)` ≠ `COUNT(col)` when NULLs exist
5. `NOT IN` with a subquery that may return NULL is a trap — always filter NULLs first

---

## Practice in the playground

1. Find leads where score IS NULL.
2. Show all leads, replacing NULL scores with 0 and NULL rep with "Unassigned".
3. Calculate the average score, treating NULL as 0 (use COALESCE inside AVG).
4. Count the difference between COUNT(*) and COUNT(score) to see how many NULLs exist.
