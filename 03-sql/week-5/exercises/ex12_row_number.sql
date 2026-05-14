/*
Exercise 12 — ROW_NUMBER: Top Order per Customer

Concepts: ROW_NUMBER(), OVER, PARTITION BY, subquery to filter on window result
Lesson: 03-sql/week-5/lessons/07-window-functions.md
Difficulty: Easy

Goal: Use ROW_NUMBER() partitioned by customer_id to rank each customer's
      orders by amount (largest first), then return only rank 1 per customer —
      i.e. each customer's single highest-value order.

Expected output (one row per customer):
    customer_id  id   amount  rn
    -----------  ---  ------  --
    1            101  99.90   1
    2            105  298.00  1
    3            109  198.00  1
    4            105  149.00  1
    5            106  87.00   1
*/

-- 📦 SETUP
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount      REAL,
    order_date  TEXT
);
INSERT INTO orders VALUES
    (101,1, 99.90,'2024-01-15'),
    (102,1, 99.00,'2024-02-04'),
    (103,1, 19.99,'2024-04-10'),
    (104,2, 99.95,'2024-02-09'),
    (105,2,298.00,'2024-04-01'),
    (106,3, 90.00,'2024-02-12'),
    (107,3, 87.00,'2024-03-15'),
    (108,3,198.00,'2024-05-01'),
    (109,4,149.00,'2024-03-01'),
    (110,4, 49.95,'2024-05-20'),
    (111,5, 87.00,'2024-03-15');

-- 🛠️ Step 1: write an inner SELECT that adds a ROW_NUMBER() column
--            partitioned by customer_id, ordered by amount DESC.
--            Call it rn.

-- 🛠️ Step 2: wrap that SELECT in a subquery and filter WHERE rn = 1.

SELECT *
FROM (
    SELECT
        customer_id, id, amount,
        ROW_NUMBER() OVER (               ) AS rn
    FROM orders
)
WHERE rn = 1
ORDER BY customer_id;

