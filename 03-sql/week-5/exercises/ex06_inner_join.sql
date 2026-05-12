/*
Exercise 6 — INNER JOIN

Concepts: JOIN, ON, aliases, computed column
Lesson: 03-sql/week-5/lessons/04-joins.md
Difficulty: Medium

Goal: for every order, return:
    order_id, customer_name, product_name, revenue  (= qty * price)
Largest revenue first.

Expected output (first 4 rows):
    order_id  customer_name  product_name  revenue
    --------  -------------  ------------  -------
    106       Pied Piper     Widget        299.7
    104       Initech        Cable         90.0
    105       Hooli          Service       298.0
    102       Acme Corp      License       99.0
    ... (order may differ if revenues tie)
*/

-- 📦 SETUP
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, region TEXT, signup_date TEXT);
CREATE TABLE products  (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL);
CREATE TABLE orders    (id INTEGER PRIMARY KEY, customer_id INTEGER, product_id INTEGER, qty INTEGER, order_date TEXT);
INSERT INTO customers VALUES
    (1,'Acme Corp','North','2024-01-15'),(2,'Globex','East','2024-02-03'),
    (3,'Initech','West','2024-02-20'),(4,'Hooli','North','2024-03-11'),
    (5,'Pied Piper','East','2024-04-01'),(6,'Stark Industries','West','2024-04-22');
INSERT INTO products VALUES
    (1,'Widget','Hardware',9.99),(2,'Gadget','Hardware',19.99),
    (3,'License','Software',99.00),(4,'Service','Service',149.00),
    (5,'Cable','Hardware',4.50),(6,'Plugin','Software',29.00);
INSERT INTO orders VALUES
    (101,1,1,10,'2024-05-02'),(102,1,3,1,'2024-05-04'),
    (103,2,2,5,'2024-05-09'),(104,3,5,20,'2024-05-12'),
    (105,4,4,2,'2024-06-01'),(106,5,1,30,'2024-06-04'),
    (107,2,4,1,'2024-06-15'),(108,1,2,3,'2024-07-01'),
    (109,6,6,4,'2024-07-12'),(110,3,3,2,'2024-07-20');

-- 🛠️ Step 1: join three tables — orders o, customers c, products p — on the right keys.
-- Compute revenue as o.qty * p.price. ORDER BY revenue DESC.

SELECT o.id AS order_id,
       c.name AS customer_name,
       p.name AS product_name,
       o.qty * p.price AS revenue
FROM orders o
JOIN customers c ON
JOIN products  p ON
ORDER BY
