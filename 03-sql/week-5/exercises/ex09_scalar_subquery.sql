/*
Exercise 9 — Scalar Subquery: Orders Above Average

Concepts: Subquery, AVG, WHERE with scalar subquery
Lesson: 03-sql/week-5/lessons/06-subqueries.md
Difficulty: Easy

Goal: Return order id, customer_id, and amount for every order
      whose amount is above the overall average order amount.
      Also show the average itself as a column called avg_amount.

Expected output (amounts and average will depend on data):
    id   customer_id  amount  avg_amount
    ---  -----------  ------  ----------
    105  4            149.0   ~119.2
    107  2            298.0   ~119.2
    109  3            198.0   ~119.2
*/

-- 📦 SETUP
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id  INTEGER,
    amount      REAL,
    order_date  TEXT
);
INSERT INTO orders VALUES
    (101,1,1, 99.90,'2024-01-15'),
    (102,1,3, 99.00,'2024-02-04'),
    (103,2,2, 99.95,'2024-02-09'),
    (104,3,5, 90.00,'2024-02-12'),
    (105,4,4,149.00,'2024-03-01'),
    (106,5,6, 87.00,'2024-03-15'),
    (107,2,4,298.00,'2024-04-01'),
    (108,1,2, 19.99,'2024-04-10'),
    (109,3,3,198.00,'2024-05-01'),
    (110,4,1, 49.95,'2024-05-20');

-- 🛠️ Step 1: write a SELECT that returns id, customer_id, amount,
--            and the average of all amounts as avg_amount,
--            WHERE amount exceeds the average.
--            Use a scalar subquery inside WHERE and inside SELECT.

SELECT

FROM

WHERE

