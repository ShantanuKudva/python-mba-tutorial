/*
Exercise 7 — LEFT JOIN to find missing rows

Concepts: LEFT JOIN, IS NULL, GROUP BY, COUNT
Lesson: 03-sql/week-5/lessons/04-joins.md
Difficulty: Hard

Goal A: list every customer and how many orders they've placed.
Customers with zero orders should show up with order_count = 0.

Goal B (in the second cell): find the customer(s) who have NEVER placed an order.

Expected output A (sorted by order_count DESC):
    name              order_count
    ----------------  -----------
    Acme Corp         3
    Initech           2
    Globex            2
    Hooli             1
    Pied Piper        1
    Stark Industries  1
    (... and any customer with 0 orders, if you added one)

Expected output B: customer names with no orders. With the seed data above there
are none — the query should return zero rows. Add a test customer to verify.
*/

-- 📦 SETUP
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, region TEXT, signup_date TEXT);
CREATE TABLE orders    (id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, qty INTEGER, order_date TEXT);
INSERT INTO customers VALUES
    (1,'Acme Corp','North','2024-01-15'),(2,'Globex','East','2024-02-03'),
    (3,'Initech','West','2024-02-20'),(4,'Hooli','North','2024-03-11'),
    (5,'Pied Piper','East','2024-04-01'),(6,'Stark Industries','West','2024-04-22'),
    -- a 7th customer with no orders — to prove the LEFT JOIN keeps them
    (7,'Wayne Enterprises','North','2024-08-01');
INSERT INTO orders VALUES
    (101,1,1,10,'2024-05-02'),(102,1,3,1,'2024-05-04'),
    (103,2,2,5,'2024-05-09'),(104,3,5,20,'2024-05-12'),
    (105,4,4,2,'2024-06-01'),(106,5,1,30,'2024-06-04'),
    (107,2,4,1,'2024-06-15'),(108,1,2,3,'2024-07-01'),
    (109,6,6,4,'2024-07-12'),(110,3,3,2,'2024-07-20');

-- 🛠️ Step 1: customer name + order_count via LEFT JOIN. COUNT(o.id), not COUNT(*).
-- Why: COUNT(o.id) returns 0 for customers with no orders; COUNT(*) returns 1.

SELECT c.name, COUNT(o.id) AS order_count
FROM customers c
LEFT JOIN orders o ON
GROUP BY
ORDER BY

-- 🛠️ Step 2: who has NEVER ordered?  LEFT JOIN, then WHERE o.id IS NULL.

SELECT
FROM customers c
LEFT JOIN orders o ON
WHERE
