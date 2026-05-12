/*
Exercise 5 — HAVING on aggregates

Concepts: GROUP BY, SUM, HAVING
Lesson: 03-sql/week-5/lessons/03-aggregates-groupby.md
Difficulty: Medium

Goal: list every customer_id that bought MORE THAN 10 units total across all their
orders. Return columns `customer_id` and `total_qty`, biggest first.

Expected output:
    customer_id  total_qty
    -----------  ---------
    5            30
    3            22
    1            14
*/

-- 📦 SETUP
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, qty INTEGER, order_date TEXT);
INSERT INTO orders VALUES
    (101,1,1,10,'2024-05-02'),(102,1,3,1,'2024-05-04'),
    (103,2,2,5,'2024-05-09'),(104,3,5,20,'2024-05-12'),
    (105,4,4,2,'2024-06-01'),(106,5,1,30,'2024-06-04'),
    (107,2,4,1,'2024-06-15'),(108,1,2,3,'2024-07-01'),
    (109,6,6,4,'2024-07-12'),(110,3,3,2,'2024-07-20');

-- 🛠️ Step 1: GROUP BY customer_id, SUM(qty) AS total_qty, HAVING SUM(qty) > 10,
-- ORDER BY total_qty DESC.

SELECT customer_id, SUM(qty) AS total_qty
FROM orders
GROUP BY
HAVING
ORDER BY
