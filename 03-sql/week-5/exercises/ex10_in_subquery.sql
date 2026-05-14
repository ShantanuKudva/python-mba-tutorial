/*
Exercise 10 — IN Subquery: Customers Who Ordered Software

Concepts: IN subquery, JOIN inside subquery, filtering by list
Lesson: 03-sql/week-5/lessons/06-subqueries.md
Difficulty: Medium

Goal: Return the name and region of every customer who placed at
      least one order for a Software-category product.
      Use a subquery with IN — not a direct JOIN on the outer query.

Expected output:
    name         region
    -----------  ------
    Acme Corp    North
    Globex       East
    Initech      West
*/

-- 📦 SETUP
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id     INTEGER PRIMARY KEY,
    name   TEXT,
    region TEXT
);
INSERT INTO customers VALUES
    (1,'Acme Corp','North'),
    (2,'Globex','East'),
    (3,'Initech','West'),
    (4,'Hooli','North'),
    (5,'Pied Piper','East');

CREATE TABLE products (
    id       INTEGER PRIMARY KEY,
    name     TEXT,
    category TEXT,
    price    REAL
);
INSERT INTO products VALUES
    (1,'Widget','Hardware',9.99),
    (2,'Gadget','Hardware',19.99),
    (3,'License','Software',99.00),
    (4,'Service','Service',149.00),
    (5,'Cable','Hardware',4.50),
    (6,'Plugin','Software',29.00);

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id  INTEGER,
    qty         INTEGER,
    amount      REAL
);
INSERT INTO orders VALUES
    (101,1,1,10, 99.90),
    (102,1,3,1,  99.00),
    (103,2,6,3,  87.00),
    (104,3,3,2, 198.00),
    (105,4,1,5,  49.95),
    (106,5,5,20, 90.00),
    (107,2,4,2, 298.00);

-- 🛠️ Step 1: write a subquery that returns the customer_id of every
--            order that involves a Software product (join orders to products inside the subquery).

-- 🛠️ Step 2: use that subquery in a WHERE ... IN (...) clause on the customers table
--            to return customer name and region.

SELECT

FROM

WHERE id IN (
    SELECT
    FROM
    JOIN
    WHERE
)

