# Lesson 7 — Window Functions

## Why this matters

GROUP BY collapses rows — you lose the individual records. Window functions give you aggregate power without collapsing: each row keeps its identity while also seeing a computed value that spans a window of related rows. This is how you compute running totals, rankings, period-over-period comparisons, and "each row vs. group average" all in one query.

## Anatomy of a window function

```sql
function_name(column) OVER (
    [PARTITION BY partition_column]
    [ORDER BY order_column]
    [ROWS/RANGE frame_spec]
)
```

- `PARTITION BY` — defines the groups (like GROUP BY, but rows aren't collapsed)
- `ORDER BY` — determines order within each partition
- The frame spec — how many rows to include (defaults vary by function)

---

## Setup

```sql
-- 📦 SETUP
DROP TABLE IF EXISTS orders;
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

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date  TEXT,
    amount      REAL
);
INSERT INTO orders VALUES
    (101,1,'2024-01-15',  99.90),
    (102,1,'2024-02-04',  99.00),
    (103,2,'2024-02-09',  99.95),
    (104,3,'2024-02-12',  90.00),
    (105,4,'2024-03-01', 149.00),
    (106,5,'2024-03-15',  87.00),
    (107,2,'2024-04-01', 298.00),
    (108,1,'2024-04-10',  19.99),
    (109,3,'2024-05-01', 198.00),
    (110,4,'2024-05-20',  49.95);
```

---

## ROW_NUMBER — unique sequential rank

```sql
SELECT id, customer_id, amount,
       ROW_NUMBER() OVER (ORDER BY amount DESC) AS rn
FROM orders;
```

`ROW_NUMBER` always produces a unique integer per row — ties are broken arbitrarily.

Partition by customer to rank each customer's orders independently:

```sql
SELECT id, customer_id, amount,
       ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS rn_per_customer
FROM orders;
```

To get each customer's biggest order, wrap in a subquery:

```sql
SELECT * FROM (
    SELECT id, customer_id, amount,
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS rn
    FROM orders
)
WHERE rn = 1;
```

---

## RANK and DENSE_RANK — handles ties

When two rows have the same value:

| Function | Tie handling | Next rank after tie |
|---|---|---|
| `RANK` | Same rank | Skips (1,1,3) |
| `DENSE_RANK` | Same rank | Consecutive (1,1,2) |
| `ROW_NUMBER` | Different rank | N/A |

```sql
SELECT id, amount,
       RANK()       OVER (ORDER BY amount DESC) AS rnk,
       DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rnk
FROM orders;
```

---

## SUM OVER — running totals

```sql
SELECT id, order_date, amount,
       SUM(amount) OVER (ORDER BY order_date) AS running_total
FROM orders;
```

Each row shows the cumulative sum of all amounts up to and including that row's date. The window frame defaults to "rows from start to current row" when ORDER BY is present.

Partition to get running totals per customer:

```sql
SELECT id, customer_id, order_date, amount,
       SUM(amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS customer_running_total
FROM orders;
```

---

## LAG and LEAD — look at adjacent rows

`LAG(col, n)` returns the value from n rows before the current row. `LEAD(col, n)` returns n rows after. Both default to n=1 and accept an optional default value if the row doesn't exist.

```sql
SELECT id, order_date, amount,
       LAG(amount, 1, 0)  OVER (ORDER BY order_date) AS prev_amount,
       amount - LAG(amount, 1, 0) OVER (ORDER BY order_date) AS delta
FROM orders;
```

This gives you period-over-period change without a self-join.

Period-over-period within each customer:

```sql
SELECT id, customer_id, order_date, amount,
       LAG(amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS prev_order,
       ROUND(100.0*(amount - LAG(amount) OVER (PARTITION BY customer_id ORDER BY order_date))
             / LAG(amount) OVER (PARTITION BY customer_id ORDER BY order_date), 1) AS pct_change
FROM orders;
```

---

## AVG OVER — row vs. group average

```sql
SELECT id, customer_id, amount,
       AVG(amount) OVER (PARTITION BY customer_id) AS customer_avg,
       amount - AVG(amount) OVER (PARTITION BY customer_id) AS vs_avg
FROM orders;
```

No GROUP BY, no subquery — every row retains its identity while seeing its customer's average alongside it.

---

## SQLite note

SQLite supports window functions from version 3.25 (2018). The in-browser Pyodide runtime uses SQLite 3.39+ so all functions above work. `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` is the explicit default frame for cumulative functions when ORDER BY is specified.

---

## Practice in the playground

1. Rank all orders by amount (largest first) using DENSE_RANK.
2. Show each order with a running total of amount ordered by date.
3. Show each order alongside the previous order amount for the same customer (use LAG with PARTITION BY customer_id).
