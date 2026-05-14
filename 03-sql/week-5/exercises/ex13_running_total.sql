/*
Exercise 13 — Running Total with SUM OVER

Concepts: SUM() OVER (ORDER BY), cumulative window function, ROUND
Lesson: 03-sql/week-5/lessons/07-window-functions.md
Difficulty: Medium

Goal: Show every order in chronological order along with:
  - the order amount
  - the running total of all amounts up to and including that order
  - the running total as a percentage of the grand total (round to 1 dp)

Expected output (partial):
    id   order_date   amount  running_total  pct_of_total
    ---  ----------   ------  -------------  ------------
    101  2024-01-15    99.90          99.90           9.2
    102  2024-02-04    99.00         198.90          18.3
    ...
    107  2024-04-01   298.00        1091.74         100.0
*/

-- 📦 SETUP
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    id         INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    amount     REAL
);
INSERT INTO orders VALUES
    (101,1,'2024-01-15', 99.90),
    (102,1,'2024-02-04', 99.00),
    (103,2,'2024-02-09', 99.95),
    (104,3,'2024-02-12', 90.00),
    (105,4,'2024-03-01',149.00),
    (106,5,'2024-03-15', 87.00),
    (107,2,'2024-04-01',298.00),
    (108,1,'2024-04-10', 19.99),
    (109,3,'2024-05-01',198.00),
    (110,4,'2024-05-20', 49.90);

-- 🛠️ Step 1: add a running_total column using SUM(amount) OVER (ORDER BY order_date).

-- 🛠️ Step 2: add a pct_of_total column: running_total divided by the grand total
--            (use SUM(amount) OVER () with no ORDER BY for the grand total),
--            multiply by 100, ROUND to 1 decimal place.

SELECT
    id,
    order_date,
    amount,
    ROUND(SUM(amount) OVER (                    ), 2) AS running_total,
    ROUND(100.0 * SUM(amount) OVER (                    )
               / SUM(amount) OVER ()                   , 1) AS pct_of_total
FROM orders
ORDER BY order_date;

