# Lesson 2 — `ORDER BY`, `LIMIT`, `DISTINCT`

Three additions that turn a raw query into a *report*: sort it, cap it, dedupe it.

```sql
-- 📦 SETUP
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id INTEGER PRIMARY KEY, name TEXT, region TEXT, signup_date TEXT
);
INSERT INTO customers VALUES
    (1, 'Acme Corp', 'North', '2024-01-15'),
    (2, 'Globex',    'East',  '2024-02-03'),
    (3, 'Initech',   'West',  '2024-02-20'),
    (4, 'Hooli',     'North', '2024-03-11'),
    (5, 'Pied Piper','East',  '2024-04-01'),
    (6, 'Stark Industries','West','2024-04-22');

CREATE TABLE products (
    id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL
);
INSERT INTO products VALUES
    (1,'Widget','Hardware',9.99),(2,'Gadget','Hardware',19.99),
    (3,'License','Software',99.00),(4,'Service','Service',149.00),
    (5,'Cable','Hardware',4.50),(6,'Plugin','Software',29.00);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, qty INTEGER, order_date TEXT
);
INSERT INTO orders VALUES
    (101,1,1,10,'2024-05-02'),(102,1,3,1,'2024-05-04'),
    (103,2,2,5,'2024-05-09'),(104,3,5,20,'2024-05-12'),
    (105,4,4,2,'2024-06-01'),(106,5,1,30,'2024-06-04'),
    (107,2,4,1,'2024-06-15'),(108,1,2,3,'2024-07-01'),
    (109,6,6,4,'2024-07-12'),(110,3,3,2,'2024-07-20');
```

## `ORDER BY` — sort rows

```sql
SELECT name, price
FROM products
ORDER BY price DESC;
```

`ASC` is ascending (default), `DESC` is descending. Sort by multiple columns by comma-separating them — the second key only matters when the first is tied.

```sql
SELECT name, category, price
FROM products
ORDER BY category ASC, price DESC;
```

## `LIMIT` — cap the row count

```sql
SELECT name, price
FROM products
ORDER BY price DESC
LIMIT 3;
```

The top-3 query. Without `ORDER BY`, `LIMIT` returns *whichever* three rows the engine felt like — useless for reports. Always sort before you limit.

`OFFSET` skips rows — `LIMIT 3 OFFSET 3` returns the 4th–6th most expensive.

## `DISTINCT` — drop duplicates

```sql
SELECT DISTINCT region FROM customers;
```

Returns each region exactly once. `DISTINCT` operates on the **combined row**, not just one column:

```sql
SELECT DISTINCT region, signup_date FROM customers;
```

If two customers signed up the same day from the same region you'd see one row. Otherwise you see all of them.

## Common pattern: top-N by group (preview)

```sql
SELECT product_id, qty
FROM orders
ORDER BY qty DESC
LIMIT 5;
```

This is the "5 biggest orders" query. To get the biggest order *per customer* you need window functions — a Phase 5+ topic. For now, `ORDER BY + LIMIT` is the workhorse.

## Try it

Return the **3 most recent orders** (id, order_date, qty), newest first.

```sql
-- Edit me, then click ▶ Run.
SELECT id, order_date, qty
FROM orders
ORDER BY
LIMIT
```

## Pitfalls

- `ORDER BY` runs **after** `WHERE` but **before** `LIMIT`. Sorting the limited set gives wrong answers.
- Dates as `TEXT` only sort correctly if formatted as `YYYY-MM-DD`. Always use ISO format.
- `DISTINCT col1, col2` is not the same as `DISTINCT col1` — it dedupes the *combination*.

---

## 📚 Resources

- [SQLite `ORDER BY`](https://sqlite.org/lang_select.html#orderby)
- [SQL Bolt — interactive lessons](https://sqlbolt.com/)
- [Use The Index, Luke — sorting performance](https://use-the-index-luke.com/sql/sorting-grouping)

---

Next: [`03-aggregates-groupby.md`](03-aggregates-groupby.md)
