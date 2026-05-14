/*
Exercise 18 — Primary Keys & Foreign Keys: Building the Mini-Store Schema

Concepts: PRIMARY KEY, FOREIGN KEY, referential integrity, schema design
Lesson: 03-sql/week-5/lessons/09-data-modeling.md
Difficulty: Easy

Goal: Write the CREATE TABLE statements for a three-table mini-store
      (customers, products, orders) with proper primary and foreign keys.
      Then insert sample rows and write a query that proves the
      relationships hold by joining all three tables.

Expected output:
    customer       product    qty  amount
    -------------  ---------  ---  ------
    Acme Corp      Widget     10   99.90
    Globex         License     1   99.00
    Initech        Plugin      3   87.00

Note: the SETUP block below creates the tables — your task is to write
      the INSERT statements and the three-table JOIN query.
*/

-- 📦 SETUP
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id     INTEGER PRIMARY KEY,
    name   TEXT    NOT NULL,
    region TEXT
);

CREATE TABLE products (
    id       INTEGER PRIMARY KEY,
    name     TEXT    NOT NULL,
    category TEXT,
    price    REAL    NOT NULL
);

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    product_id  INTEGER NOT NULL REFERENCES products(id),
    qty         INTEGER NOT NULL,
    amount      REAL    NOT NULL
);

-- 🛠️ Step 1: insert at least 3 customers, 3 products, and 3 orders
--            using the ids that link them together.

INSERT INTO customers VALUES
    (1, 'Acme Corp', 'North'),
    (2, 'Globex',    'East'),
    (3, 'Initech',   'West');

INSERT INTO products VALUES
    (1, 'Widget',  'Hardware', 9.99),
    (2, 'License', 'Software', 99.00),
    (3, 'Plugin',  'Software', 29.00);

INSERT INTO orders VALUES

;

-- 🛠️ Step 2: write a three-table JOIN (customers, orders, products)
--            that returns customer name, product name, qty, and amount.

SELECT

FROM

JOIN

JOIN

ORDER BY customers.id;
