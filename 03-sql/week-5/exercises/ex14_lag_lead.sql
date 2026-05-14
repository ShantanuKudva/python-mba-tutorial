/*
Exercise 14 — LAG & LEAD: Month-over-Month Revenue

Concepts: LAG(), LEAD(), OVER (ORDER BY), period-over-period delta
Lesson: 03-sql/week-5/lessons/07-window-functions.md
Difficulty: Hard

Goal: You have a monthly_revenue table. For each month, show:
  - the month and revenue
  - the previous month's revenue (lag_revenue)
  - the next month's revenue (lead_revenue)
  - the month-over-month change (revenue - lag, NULL for the first month)
  - the month-over-month % change, rounded to 1 decimal place

Expected output:
    month    revenue  lag_rev  lead_rev  mom_delta  mom_pct
    -------  -------  -------  --------  ---------  -------
    2024-01  45000    NULL     52000     NULL        NULL
    2024-02  52000    45000    38000     7000        15.6
    2024-03  38000    52000    61000    -14000       -26.9
    2024-04  61000    38000    55000    23000        60.5
    2024-05  55000    61000    72000    -6000        -9.8
    2024-06  72000    55000    NULL     17000        30.9
*/

-- 📦 SETUP
DROP TABLE IF EXISTS monthly_revenue;
CREATE TABLE monthly_revenue (
    month   TEXT PRIMARY KEY,
    revenue REAL
);
INSERT INTO monthly_revenue VALUES
    ('2024-01', 45000),
    ('2024-02', 52000),
    ('2024-03', 38000),
    ('2024-04', 61000),
    ('2024-05', 55000),
    ('2024-06', 72000);

-- 🛠️ Step 1: add a lag_rev column using LAG(revenue, 1) OVER (ORDER BY month).
--            Default to NULL for the first row.

-- 🛠️ Step 2: add a lead_rev column using LEAD(revenue, 1) OVER (ORDER BY month).

-- 🛠️ Step 3: compute mom_delta = revenue - lag_rev (will be NULL for first row).

-- 🛠️ Step 4: compute mom_pct = ROUND(100.0 * mom_delta / lag_rev, 1).
--            Use a subquery or CTE so you can reference lag_rev by name in the division.

SELECT
    month,
    revenue,
    LAG(revenue, 1)  OVER (ORDER BY month) AS lag_rev,
    LEAD(revenue, 1) OVER (ORDER BY month) AS lead_rev,
    revenue - LAG(revenue, 1) OVER (ORDER BY month) AS mom_delta,
    ROUND(
        100.0 * (revenue - LAG(revenue, 1) OVER (ORDER BY month))
              /  LAG(revenue, 1) OVER (ORDER BY month)
    , 1) AS mom_pct
FROM monthly_revenue
ORDER BY month;

