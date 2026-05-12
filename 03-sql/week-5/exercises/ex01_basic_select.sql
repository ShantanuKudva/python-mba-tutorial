/*
Exercise 1 — Basic SELECT

Concepts: SELECT, FROM
Lesson: 03-sql/week-5/lessons/01-select-from-where.md
Difficulty: Easy

Goal: return the name and price of every product, in any order.

Expected output:
    name      price
    --------  -----
    Widget    9.99
    Gadget    19.99
    License   99.0
    Service   149.0
    Cable     4.5
    Plugin    29.0
*/

-- 📦 SETUP
DROP TABLE IF EXISTS products;
CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL);
INSERT INTO products VALUES
    (1,'Widget','Hardware',9.99),(2,'Gadget','Hardware',19.99),
    (3,'License','Software',99.00),(4,'Service','Service',149.00),
    (5,'Cable','Hardware',4.50),(6,'Plugin','Software',29.00);

-- 🛠️ Step 1: write a SELECT that returns two columns — name and price — from the products table.

SELECT
FROM
