# Lesson 1 — `SELECT … FROM … WHERE`

Three keywords. Eighty percent of all SQL you will ever write.

| Keyword | Job |
|---|---|
| `FROM`  | which table to read |
| `SELECT`| which columns to keep |
| `WHERE` | which rows to keep |

You **read** a query in that order too: pick the source, filter rows, then pick columns.

## The mini-store schema (re-seeded on every lesson page)

```sql
-- 📦 SETUP
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    region      TEXT,
    signup_date TEXT
);
INSERT INTO customers VALUES
    (1, 'Acme Corp',         'North', '2024-01-15'),
    (2, 'Globex',            'East',  '2024-02-03'),
    (3, 'Initech',           'West',  '2024-02-20'),
    (4, 'Hooli',             'North', '2024-03-11'),
    (5, 'Pied Piper',        'East',  '2024-04-01'),
    (6, 'Stark Industries',  'West',  '2024-04-22');

CREATE TABLE products (
    id       INTEGER PRIMARY KEY,
    name     TEXT,
    category TEXT,
    price    REAL
);
INSERT INTO products VALUES
    (1, 'Widget',   'Hardware', 9.99),
    (2, 'Gadget',   'Hardware', 19.99),
    (3, 'License',  'Software', 99.00),
    (4, 'Service',  'Service',  149.00),
    (5, 'Cable',    'Hardware', 4.50),
    (6, 'Plugin',   'Software', 29.00);

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id  INTEGER,
    qty         INTEGER,
    order_date  TEXT
);
INSERT INTO orders VALUES
    (101, 1, 1, 10, '2024-05-02'),
    (102, 1, 3, 1,  '2024-05-04'),
    (103, 2, 2, 5,  '2024-05-09'),
    (104, 3, 5, 20, '2024-05-12'),
    (105, 4, 4, 2,  '2024-06-01'),
    (106, 5, 1, 30, '2024-06-04'),
    (107, 2, 4, 1,  '2024-06-15'),
    (108, 1, 2, 3,  '2024-07-01'),
    (109, 6, 6, 4,  '2024-07-12'),
    (110, 3, 3, 2,  '2024-07-20');
```

## Everything from one table

```sql
SELECT * FROM customers;
```

`*` means "all columns". Convenient in the playground, but in real code always name the columns you want — schemas drift and `SELECT *` breaks silently.

## Pick specific columns

```sql
SELECT name, region FROM customers;
```

Output has the columns in the order you listed.

## Filter rows with `WHERE`

```sql
SELECT name, region
FROM customers
WHERE region = 'North';
```

`=` (single equals), not `==`. Strings go in single quotes.

## Combine conditions

```sql
SELECT name, category, price
FROM products
WHERE category = 'Hardware'
  AND price < 15;
```

Use `AND`, `OR`, `NOT`. Parentheses for grouping when mixing them.

## Pattern matching

```sql
SELECT name
FROM customers
WHERE name LIKE '%Corp%';
```

`%` matches any number of characters, `_` matches one. SQLite is case-insensitive for ASCII by default with `LIKE` — try changing the pattern.

## Try it: your turn

Write a query that returns the **name and price** of every product that costs more than 20.

```sql
-- Edit me, then click ▶ Run.
SELECT
FROM products
WHERE
```

## Pitfalls

- `WHERE region = NULL` returns nothing — `NULL` is not equal to anything, including itself. Use `IS NULL` / `IS NOT NULL`.
- `WHERE qty = '10'` (string) silently differs from `WHERE qty = 10` (number) in some databases. SQLite is permissive; PostgreSQL is not.
- Comments: `-- single line` or `/* block */`.

---

## 📚 Resources

**Official docs**
- [SQLite — language reference](https://sqlite.org/lang.html)
- [SQLite — `SELECT`](https://sqlite.org/lang_select.html)

**Deep dives**
- [SQL Murder Mystery (free, browser-based)](https://mystery.knightlab.com/) — learn by solving a fake crime
- [Mode Analytics — SQL tutorial](https://mode.com/sql-tutorial/)

**Video**
- [freeCodeCamp — 4 hour SQL course](https://www.youtube.com/watch?v=HXV3zeQKqGY)

---

Next: [`02-sorting-limit-distinct.md`](02-sorting-limit-distinct.md)
