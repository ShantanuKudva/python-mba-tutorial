/*
Exercise 4 — GROUP BY + aggregate

Concepts: GROUP BY, COUNT, SUM, AS
Lesson: 03-sql/week-5/lessons/03-aggregates-groupby.md
Difficulty: Medium

Goal: for each region, count the customers in that region.
Return two columns aliased as `region` and `n_customers`. Sort biggest first.

Expected output:
    region   n_customers
    -------  -----------
    North    2
    East     2
    West     2
*/

-- 📦 SETUP
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, region TEXT, signup_date TEXT);
INSERT INTO customers VALUES
    (1,'Acme Corp','North','2024-01-15'),(2,'Globex','East','2024-02-03'),
    (3,'Initech','West','2024-02-20'),(4,'Hooli','North','2024-03-11'),
    (5,'Pied Piper','East','2024-04-01'),(6,'Stark Industries','West','2024-04-22');

-- 🛠️ Step 1: GROUP BY region, COUNT(*) renamed to n_customers, ORDER BY the count.

SELECT
FROM customers
GROUP BY
ORDER BY
