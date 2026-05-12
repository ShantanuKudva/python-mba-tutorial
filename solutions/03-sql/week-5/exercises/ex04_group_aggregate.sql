/*
Reference solution — Exercise 4.
*/

-- 📦 SETUP
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, region TEXT, signup_date TEXT);
INSERT INTO customers VALUES
    (1,'Acme Corp','North','2024-01-15'),(2,'Globex','East','2024-02-03'),
    (3,'Initech','West','2024-02-20'),(4,'Hooli','North','2024-03-11'),
    (5,'Pied Piper','East','2024-04-01'),(6,'Stark Industries','West','2024-04-22');

-- 🛠️ Step 1: group by region, count rows.
SELECT region, COUNT(*) AS n_customers
FROM customers
GROUP BY region
ORDER BY n_customers DESC;
