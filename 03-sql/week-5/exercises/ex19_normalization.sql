/*
Exercise 19 — Normalization: Split a Flat Table into 2NF

Concepts: 1NF, 2NF, removing repeating data, splitting tables, JOIN to reconstruct
Lesson: 03-sql/week-5/lessons/09-data-modeling.md
Difficulty: Medium

Goal: A flat orders_flat table mixes order data with customer contact info
      (violating 2NF — customer_email depends only on customer_id, not the full key).
      Your job:
  1. Create a normalised customers_norm table with id, name, email.
  2. Create a normalised orders_norm table with id, customer_id, product, amount.
  3. INSERT data from the flat table into both normalised tables.
  4. JOIN to reconstruct a view that matches the original flat table.

Expected reconstructed output:
    order_id  customer_name  email                  product    amount
    --------  -------------  ---------------------  ---------  ------
    1001      Acme Corp      acme@example.com        Widget     99.90
    1002      Globex         globex@example.com      License    99.00
    1003      Acme Corp      acme@example.com        Plugin     29.00
    1004      Initech        initech@example.com     Widget     49.95
*/

-- 📦 SETUP
DROP TABLE IF EXISTS orders_norm;
DROP TABLE IF EXISTS customers_norm;
DROP TABLE IF EXISTS orders_flat;

CREATE TABLE orders_flat (
    order_id      INTEGER,
    customer_id   INTEGER,
    customer_name TEXT,
    email         TEXT,
    product       TEXT,
    amount        REAL
);
INSERT INTO orders_flat VALUES
    (1001, 1, 'Acme Corp', 'acme@example.com',    'Widget',  99.90),
    (1002, 2, 'Globex',    'globex@example.com',  'License', 99.00),
    (1003, 1, 'Acme Corp', 'acme@example.com',    'Plugin',  29.00),
    (1004, 3, 'Initech',   'initech@example.com', 'Widget',  49.95);

-- 🛠️ Step 1: CREATE TABLE customers_norm (id, name, email) and
--            INSERT DISTINCT customer rows from orders_flat.

CREATE TABLE customers_norm (
    id    INTEGER PRIMARY KEY,
    name  TEXT,
    email TEXT
);

INSERT INTO customers_norm
SELECT DISTINCT

FROM orders_flat;

-- 🛠️ Step 2: CREATE TABLE orders_norm (id, customer_id, product, amount)
--            and INSERT from orders_flat.

CREATE TABLE orders_norm (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product     TEXT,
    amount      REAL
);

INSERT INTO orders_norm
SELECT

FROM orders_flat;

-- 🛠️ Step 3: JOIN customers_norm and orders_norm to reconstruct the flat view.
--            Return order_id, customer_name, email, product, amount.

SELECT

FROM

JOIN

ORDER BY orders_norm.id;
