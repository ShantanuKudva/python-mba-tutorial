/*
Exercise 20 — Denormalize for Analytics: Build a Flat Reporting View

Concepts: Denormalization, analytics flat table, GROUP BY on joined data,
          when to denormalize
Lesson: 03-sql/week-5/lessons/09-data-modeling.md
Difficulty: Hard

Goal: Starting from a normalised schema (customers, products, orders),
      build a denormalized analytics summary that a BI tool or pivot table
      can consume directly:
  1. For each customer + product category, show total revenue and order count.
  2. Add a customer_tier column: "VIP" if total revenue > 200, else "Standard".
  3. Order by total_revenue DESC.

Expected output:
    customer     region  category   order_count  total_revenue  customer_tier
    -----------  ------  ---------  -----------  -------------  -------------
    Acme Corp    North   Software            2         198.00   Standard
    Globex       East    Hardware            2         189.85   Standard
    Initech      West    Software            1         149.00   Standard
    Acme Corp    North   Hardware            1          99.90   Standard
    Globex       East    Software            1          87.00   Standard
    Hooli        North   Hardware            2         239.85   VIP
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
    (2,'Globex',   'East'),
    (3,'Initech',  'West'),
    (4,'Hooli',    'North');

CREATE TABLE products (
    id       INTEGER PRIMARY KEY,
    name     TEXT,
    category TEXT,
    price    REAL
);
INSERT INTO products VALUES
    (1,'Widget',  'Hardware',  9.99),
    (2,'Gadget',  'Hardware', 19.99),
    (3,'License', 'Software', 99.00),
    (4,'Service', 'Software',149.00),
    (5,'Plugin',  'Software', 29.00);

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id  INTEGER,
    qty         INTEGER,
    amount      REAL
);
INSERT INTO orders VALUES
    (101,1,1,10,  99.90),
    (102,1,3, 1,  99.00),
    (103,1,5, 3,  99.00),
    (104,2,1, 5,  49.95),
    (105,2,2, 7, 139.90),
    (106,2,5, 3,  87.00),
    (107,3,4, 1, 149.00),
    (108,4,1,10,  99.90),
    (109,4,2, 7, 139.95);

-- 🛠️ Step 1: JOIN customers, orders, and products.
--            GROUP BY customer name, region, and product category.
--            Compute COUNT(*) as order_count and SUM(amount) as total_revenue.

-- 🛠️ Step 2: wrap that query in a subquery and add a customer_tier column
--            using CASE WHEN total_revenue > 200 THEN 'VIP' ELSE 'Standard' END.

-- 🛠️ Step 3: ORDER BY total_revenue DESC.

SELECT
    customer,
    region,
    category,
    order_count,
    ROUND(total_revenue, 2) AS total_revenue,
    CASE WHEN total_revenue > 200 THEN 'VIP' ELSE 'Standard' END AS customer_tier
FROM (
    SELECT
        c.name       AS customer,
        c.region,
        p.category,
        COUNT(*)     AS order_count,
        SUM(o.amount) AS total_revenue
    FROM

    JOIN

    JOIN

    GROUP BY
)
ORDER BY total_revenue DESC;
