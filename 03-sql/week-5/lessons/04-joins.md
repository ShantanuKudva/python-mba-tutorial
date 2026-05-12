# Lesson 4 — `JOIN`

Joins are how separate tables become one wide result row. They are the *whole point* of a relational database.

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

## Why we have separate tables

`orders` stores a tiny `customer_id` instead of repeating the customer's full name and region on every row. The `id` column in `customers` is the **primary key**; the `customer_id` column in `orders` is a **foreign key** that points to it.

A join walks that pointer to glue rows together.

## `INNER JOIN` — only matching rows on both sides

```sql
SELECT orders.id AS order_id,
       customers.name AS customer,
       orders.qty,
       orders.order_date
FROM orders
INNER JOIN customers
  ON orders.customer_id = customers.id;
```

Read top to bottom:

- `FROM orders` — start with the orders table.
- `INNER JOIN customers ON …` — match each order to the row in `customers` where the IDs line up.
- Rows in `orders` with no matching customer (orphan rows) **disappear**.
- Rows in `customers` with no orders **disappear** too.

Use table aliases to cut the noise:

```sql
SELECT o.id AS order_id, c.name AS customer, p.name AS product, o.qty, p.price * o.qty AS revenue
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN products  p ON o.product_id  = p.id
ORDER BY revenue DESC;
```

`JOIN` is shorthand for `INNER JOIN`. Three tables, two `ON` clauses, one row per order — with the customer name, product name, and computed revenue.

## `LEFT JOIN` — keep every row on the left

```sql
SELECT c.name, COUNT(o.id) AS order_count
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
GROUP BY c.id, c.name
ORDER BY order_count DESC;
```

Even customers who never ordered show up — with `order_count = 0`. Compare to an `INNER JOIN` here: customers without orders silently vanish.

When you ask *"who hasn't bought anything?"*, the answer is a `LEFT JOIN ... WHERE right.id IS NULL`:

```sql
SELECT c.name
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
WHERE o.id IS NULL;
```

## Visual cheat sheet

```text
Inner   →  rows present in BOTH tables
Left    →  every row from the LEFT  + matches from right (NULL if no match)
Right   →  mirror of left (SQLite supports it; many older DBs don't)
Full    →  every row from either side
```

Ninety percent of business queries are `INNER` or `LEFT`. Learn those cold first.

## Try it

For each **product category**, return total revenue (`qty * price`) across all orders. Use a join. Sort biggest first.

```sql
-- Edit me, then click ▶ Run.
SELECT p.category, SUM(o.qty * p.price) AS revenue
FROM orders o
JOIN products p
  ON
GROUP BY
ORDER BY
```

## Pitfalls

- Forgetting `ON` produces a **Cartesian product** — every row paired with every other row. With three tables that's millions of rows. SQLite will execute it; your laptop fan will tell you.
- `LEFT JOIN ... WHERE right_col = 'x'` quietly turns into an inner join — the `WHERE` discards the `NULL`s you just preserved. Put filters on the *right* table inside the `ON` clause: `... ON c.id = o.customer_id AND o.qty > 5`.
- Aggregating over a one-to-many join double-counts. If a customer placed 3 orders, joining to a `payments` table with 2 rows per order gives 6 rows — `SUM(qty)` is wrong by 2x. Aggregate one side first, then join.

---

## 📚 Resources

- [SQLite — joins](https://sqlite.org/lang_select.html#strange)
- [A visual explanation of SQL joins (Jeff Atwood)](https://blog.codinghorror.com/a-visual-explanation-of-sql-joins/)
- [Mode — joins tutorial](https://mode.com/sql-tutorial/sql-joins/)
- [Select Star SQL — interactive book (free)](https://selectstarsql.com/)

---

Next: [`05-python-sqlalchemy.md`](05-python-sqlalchemy.md)
