/*
Exercise 3 — ORDER BY + LIMIT

Concepts: ORDER BY, DESC, LIMIT
Lesson: 03-sql/week-5/lessons/02-sorting-limit-distinct.md
Difficulty: Easy

Goal: return the 3 most expensive products — name and price — most expensive first.

Expected output:
    name      price
    --------  -----
    Service   149.0
    License   99.0
    Plugin    29.0
*/

-- 📦 SETUP
DROP TABLE IF EXISTS products;
CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL);
INSERT INTO products VALUES
    (1,'Widget','Hardware',9.99),(2,'Gadget','Hardware',19.99),
    (3,'License','Software',99.00),(4,'Service','Service',149.00),
    (5,'Cable','Hardware',4.50),(6,'Plugin','Software',29.00);

-- 🛠️ Step 1: select name and price, sort price descending, keep only the first 3 rows.

SELECT
FROM products
ORDER BY
LIMIT
