/*
Reference solution — Exercise 7.
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
    (7,'Wayne Enterprises','North','2024-08-01');
INSERT INTO orders VALUES
    (101,1,1,10,'2024-05-02'),(102,1,3,1,'2024-05-04'),
    (103,2,2,5,'2024-05-09'),(104,3,5,20,'2024-05-12'),
    (105,4,4,2,'2024-06-01'),(106,5,1,30,'2024-06-04'),
    (107,2,4,1,'2024-06-15'),(108,1,2,3,'2024-07-01'),
    (109,6,6,4,'2024-07-12'),(110,3,3,2,'2024-07-20');

-- 🛠️ Step 1: order count per customer — COUNT(o.id) so missing-order rows score 0.
SELECT c.name, COUNT(o.id) AS order_count
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
GROUP BY c.id, c.name
ORDER BY order_count DESC;

-- 🛠️ Step 2: customers without orders.
SELECT c.name
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
WHERE o.id IS NULL;
