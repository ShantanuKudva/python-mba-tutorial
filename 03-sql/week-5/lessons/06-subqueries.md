# Lesson 6 — Subqueries

## Why this matters

Some questions can't be answered in one flat query. "Which customers placed orders above the average order value?" requires knowing the average first — and then filtering by it. Subqueries let you nest one query inside another, so you can express those two-step questions as a single statement.

## Three flavours of subqueries

| Type | Where it lives | Returns | Use case |
|---|---|---|---|
| Scalar | SELECT or WHERE | A single value | Compare a column to a computed threshold |
| IN list | WHERE … IN | A column of values | Filter rows whose ID appears in another query |
| Correlated | WHERE | One value per outer row | Row-by-row comparisons using outer table columns |

---

## Setup

```sql
-- 📦 SETUP
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id     INTEGER PRIMARY KEY,
    name   TEXT,
    region TEXT
);
INSERT INTO customers VALUES
    (1,'Acme Corp','North'),
    (2,'Globex','East'),
    (3,'Initech','West'),
    (4,'Hooli','North'),
    (5,'Pied Piper','East');

CREATE TABLE products (
    id       INTEGER PRIMARY KEY,
    name     TEXT,
    category TEXT,
    price    REAL
);
INSERT INTO products VALUES
    (1,'Widget','Hardware',9.99),
    (2,'Gadget','Hardware',19.99),
    (3,'License','Software',99.00),
    (4,'Service','Service',149.00),
    (5,'Cable','Hardware',4.50),
    (6,'Plugin','Software',29.00);

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id  INTEGER,
    qty         INTEGER,
    amount      REAL
);
INSERT INTO orders VALUES
    (101,1,1,10, 99.90),
    (102,1,3,1,  99.00),
    (103,2,2,5, 99.95),
    (104,3,5,20, 90.00),
    (105,4,4,1, 149.00),
    (106,5,6,3,  87.00),
    (107,2,4,2, 298.00),
    (108,1,2,1,  19.99),
    (109,3,3,2, 198.00),
    (110,4,1,5,  49.95);
```

---

## 1. Scalar subquery — compute a single value inline

A scalar subquery goes inside `WHERE`, `SELECT`, or `HAVING`. It must return exactly one row and one column.

```sql
-- Orders above the average order amount
SELECT id, customer_id, amount
FROM orders
WHERE amount > (SELECT AVG(amount) FROM orders);
```

The inner query `(SELECT AVG(amount) FROM orders)` runs first and produces ~119. The outer query then filters rows where amount > 119.

You can also use a scalar subquery in SELECT to show context alongside each row:

```sql
SELECT id, amount,
       (SELECT AVG(amount) FROM orders) AS avg_amount,
       amount - (SELECT AVG(amount) FROM orders) AS vs_avg
FROM orders;
```

---

## 2. IN subquery — filter by a list from another query

`WHERE x IN (subquery)` keeps only rows where `x` matches any value returned by the subquery.

```sql
-- Customers who placed at least one order
SELECT id, name
FROM customers
WHERE id IN (SELECT DISTINCT customer_id FROM orders);
```

Inverse: use `NOT IN` to find customers with NO orders:

```sql
SELECT id, name
FROM customers
WHERE id NOT IN (SELECT DISTINCT customer_id FROM orders);
```

> Watch out: if the subquery can return NULL, `NOT IN` will return no rows (NULL != anything). Use `NOT EXISTS` instead when NULLs are possible — covered in Lesson 8.

---

## 3. Correlated subquery — reference the outer query

A correlated subquery is re-evaluated for every row of the outer query. It's slower on large tables but expressive.

```sql
-- For each customer, find their highest single order amount
SELECT c.name,
       (SELECT MAX(o.amount)
        FROM orders o
        WHERE o.customer_id = c.id) AS max_order
FROM customers c;
```

The inner `WHERE o.customer_id = c.id` references `c.id` from the outer query — that's the correlation.

---

## Subqueries in FROM — inline views

You can also use a subquery as if it were a table (an "inline view" or CTE precursor):

```sql
SELECT region, total_spend
FROM (
    SELECT c.region, SUM(o.amount) AS total_spend
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    GROUP BY c.region
) AS region_summary
WHERE total_spend > 200;
```

This is especially useful when you need to filter on an aggregate (something HAVING can't always do cleanly across multiple tables).

---

## Key rules

1. Scalar subqueries must return exactly one value — if your subquery returns multiple rows, you'll get an error.
2. IN subqueries return a column — one column, any number of rows.
3. Correlated subqueries run once per outer row — avoid on millions of rows without an index.
4. Subqueries can be nested up to many levels — but readability suffers. Use CTEs (WITH clauses) for anything beyond two levels.

---

## Practice in the playground

Try these directly in the SQL playground:

1. Find all orders with amount above the average.
2. Find all customers who ordered Software products (use IN with a join to products).
3. For each customer, show their total spend alongside the overall average total spend.
