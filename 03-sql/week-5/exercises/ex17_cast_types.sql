/*
Exercise 17 — CAST & Type Affinity: Fixing Mixed-Type Data

Concepts: CAST, TYPEOF, type affinity in SQLite, safe numeric conversion
Lesson: 03-sql/week-5/lessons/08-nulls-and-data-types.md
Difficulty: Hard

Goal: A raw_orders import table stores amount and qty as TEXT
      (a common real-world mess). Use CAST to:
  1. Return order id, amount cast to REAL, and qty cast to INTEGER.
  2. Compute a revenue column = CAST(qty AS INTEGER) * CAST(amount AS REAL).
  3. Filter only orders where the numeric amount exceeds 50.0
     (note: text comparison "99" > "100" is TRUE — cast first!).
  4. Show TYPEOF for the original and cast values to confirm the type change.

Expected output (partial):
    id   amount_raw  amount_num  qty_raw  qty_num  revenue   typeof_raw  typeof_cast
    ---  ----------  ----------  -------  -------  -------   ----------  -----------
    101  "99.90"     99.9        "2"      2        199.8     text        real
    103  "149.00"    149.0       "1"      1        149.0     text        real
    104  "87.50"     87.5        "3"      3        262.5     text        real
*/

-- 📦 SETUP
DROP TABLE IF EXISTS raw_orders;
CREATE TABLE raw_orders (
    id     INTEGER PRIMARY KEY,
    amount TEXT,
    qty    TEXT
);
INSERT INTO raw_orders VALUES
    (101, '99.90',  '2'),
    (102, '19.95',  '5'),
    (103, '149.00', '1'),
    (104, '87.50',  '3'),
    (105, '9.99',   '10');

-- 🛠️ Step 1: write a SELECT that shows id, amount (raw TEXT), CAST(amount AS REAL) as amount_num,
--            qty (raw TEXT), CAST(qty AS INTEGER) as qty_num.

-- 🛠️ Step 2: add a revenue column = CAST(qty AS INTEGER) * CAST(amount AS REAL).

-- 🛠️ Step 3: add WHERE CAST(amount AS REAL) > 50.0 to filter only high-value orders.

-- 🛠️ Step 4: add TYPEOF(amount) as typeof_raw and TYPEOF(CAST(amount AS REAL)) as typeof_cast
--            to confirm the type change.

SELECT
    id,
    amount                        AS amount_raw,
    CAST(          AS REAL)       AS amount_num,
    qty                           AS qty_raw,
    CAST(          AS INTEGER)    AS qty_num,
    CAST(qty AS INTEGER) * CAST(amount AS REAL) AS revenue,
    TYPEOF(amount)                AS typeof_raw,
    TYPEOF(CAST(amount AS REAL))  AS typeof_cast
FROM raw_orders
WHERE

ORDER BY id;
