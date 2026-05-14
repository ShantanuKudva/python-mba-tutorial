/*
Exercise 11 — Correlated Subquery: Each Customer's Max Order

Concepts: Correlated subquery, MAX, reference outer table in subquery
Lesson: 03-sql/week-5/lessons/06-subqueries.md
Difficulty: Hard

Goal: For every customer, show their name and the amount of their
      single largest order. Use a correlated subquery in the SELECT
      clause (not a JOIN or GROUP BY).

Expected output:
    name          max_order
    ------------  ---------
    Acme Corp     99.90
    Globex        298.00
    Initech       198.00
    Hooli         149.00
    Pied Piper    87.00
*/

-- 📦 SETUP
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id   INTEGER PRIMARY KEY,
    name TEXT
);
INSERT INTO customers VALUES
    (1,'Acme Corp'),
    (2,'Globex'),
    (3,'Initech'),
    (4,'Hooli'),
    (5,'Pied Piper');

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount      REAL
);
INSERT INTO orders VALUES
    (101,1, 99.90),
    (102,1, 99.00),
    (103,1, 19.99),
    (104,2, 87.00),
    (105,2,298.00),
    (106,3,198.00),
    (107,4,149.00),
    (108,4, 49.95),
    (109,5, 87.00);

-- 🛠️ Step 1: in the SELECT clause, write a correlated subquery that finds
--            MAX(amount) from orders WHERE customer_id matches the outer customer row.
--            Alias it as max_order.

-- 🛠️ Step 2: the outer query selects from customers c —
--            reference c.id inside the subquery's WHERE clause.

SELECT
    c.name,
    (SELECT
     FROM
     WHERE ) AS max_order
FROM customers c
ORDER BY c.name;

