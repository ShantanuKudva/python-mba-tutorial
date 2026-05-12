# Lesson 3 — Aggregates, `GROUP BY`, `HAVING`

This is the moment SQL stops being a fancier "find" command and starts being analytics.

```sql
-- 📦 SETUP
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, region TEXT, signup_date TEXT);
INSERT INTO customers VALUES
    (1,'Acme Corp','North','2024-01-15'),(2,'Globex','East','2024-02-03'),
    (3,'Initech','West','2024-02-20'),(4,'Hooli','North','2024-03-11'),
    (5,'Pied Piper','East','2024-04-01'),(6,'Stark Industries','West','2024-04-22');
CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL);
INSERT INTO products VALUES
    (1,'Widget','Hardware',9.99),(2,'Gadget','Hardware',19.99),
    (3,'License','Software',99.00),(4,'Service','Service',149.00),
    (5,'Cable','Hardware',4.50),(6,'Plugin','Software',29.00);
CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, qty INTEGER, order_date TEXT);
INSERT INTO orders VALUES
    (101,1,1,10,'2024-05-02'),(102,1,3,1,'2024-05-04'),
    (103,2,2,5,'2024-05-09'),(104,3,5,20,'2024-05-12'),
    (105,4,4,2,'2024-06-01'),(106,5,1,30,'2024-06-04'),
    (107,2,4,1,'2024-06-15'),(108,1,2,3,'2024-07-01'),
    (109,6,6,4,'2024-07-12'),(110,3,3,2,'2024-07-20');
```

## The five aggregates you'll use forever

| Function | Returns |
|---|---|
| `COUNT(*)` | how many rows |
| `COUNT(col)` | how many non-NULL values in that column |
| `SUM(col)`  | total |
| `AVG(col)`  | average |
| `MIN(col)`, `MAX(col)` | extremes |

```sql
SELECT COUNT(*) AS total_orders,
       SUM(qty) AS total_units,
       AVG(qty) AS avg_units,
       MAX(qty) AS biggest_order
FROM orders;
```

`AS` renames a column in the output — purely cosmetic, but reports without aliases look amateurish.

## `GROUP BY` — collapse rows into buckets

Without `GROUP BY` an aggregate returns one row for the whole table. With it, you get one row **per group**.

```sql
SELECT category, COUNT(*) AS n_products, AVG(price) AS avg_price
FROM products
GROUP BY category;
```

Read it as: "for each distinct `category`, count rows and average price".

**Rule:** every column in `SELECT` must either appear in `GROUP BY` *or* be wrapped in an aggregate. SQLite is loose about this; PostgreSQL will reject you. Get the habit right from day one.

## `HAVING` — filter on aggregates

`WHERE` filters rows **before** grouping. `HAVING` filters groups **after** aggregating.

```sql
SELECT customer_id, SUM(qty) AS total_units
FROM orders
GROUP BY customer_id
HAVING SUM(qty) > 10;
```

Customers who bought more than 10 units total. You can't put `SUM(qty) > 10` in `WHERE` — the sum doesn't exist yet at that point.

## Combine them — the canonical query shape

The full ordering of clauses (memorize this):

```text
SELECT   columns + aggregates
FROM     table(s)
WHERE    row-level filter
GROUP BY grouping keys
HAVING   group-level filter
ORDER BY sort keys
LIMIT    cap
```

Top to bottom. Same on every query. Different databases, same shape.

## Try it

For each `product_id`, count how many orders it appears in and sum the total `qty`. Only keep products with **more than 1 order**. Sort by total qty descending.

```sql
-- Edit me, then click ▶ Run.
SELECT product_id, COUNT(*) AS order_count, SUM(qty) AS total_qty
FROM orders
GROUP BY
HAVING
ORDER BY
```

## Pitfalls

- `COUNT(col)` skips `NULL`. `COUNT(*)` counts every row. Use the one you actually mean.
- `AVG` on an empty set returns `NULL`, not `0`. Wrap with `COALESCE(AVG(x), 0)` if a number is expected downstream.
- Forgetting `GROUP BY` and then aggregating: you'll get one row total, which is rarely what you wanted.

---

## 📚 Resources

- [SQLite — aggregate functions](https://sqlite.org/lang_aggfunc.html)
- [Mode — GROUP BY tutorial](https://mode.com/sql-tutorial/sql-group-by/)
- [PostgreSQL — `GROUP BY` semantics](https://www.postgresql.org/docs/current/sql-select.html#SQL-GROUPBY) (stricter than SQLite)

---

Next: [`04-joins.md`](04-joins.md)
