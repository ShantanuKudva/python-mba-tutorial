/*
Exercise 16 — COALESCE & NULLIF: Safe Calculations

Concepts: COALESCE, NULLIF, safe division, NULL-to-default
Lesson: 03-sql/week-5/lessons/08-nulls-and-data-types.md
Difficulty: Medium

Goal: From the leads table:
  1. Show each lead with score replaced by 0 when NULL (use COALESCE).
  2. Show each lead with assigned_to replaced by 'Unassigned' when NULL.
  3. Compute revenue_per_score_point = revenue_est / score,
     but use NULLIF to avoid division by zero and COALESCE to default
     NULL revenue_est to 0 before dividing.
  4. Use COALESCE to produce a combined score: if score IS NULL, use 50 as a default.

Expected output (partial):
    name        score_safe  rep          est_revenue  revenue_per_pt  score_or_default
    ----------  ----------  -----------  -----------  --------------  ----------------
    Acme Corp   85          Alice        50000.0      588.24          85
    Globex      0           Bob          0.0          NULL            50
    Initech     60          Bob          0.0          0.0             60
    Hooli       92          Alice        80000.0      869.57          92
    Pied Piper  0           Unassigned   0.0          NULL            50
    Stark       78          Carol        120000.0     1538.46         78
*/

-- 📦 SETUP
DROP TABLE IF EXISTS leads;
CREATE TABLE leads (
    id          INTEGER PRIMARY KEY,
    name        TEXT,
    score       INTEGER,
    assigned_to TEXT,
    revenue_est REAL
);
INSERT INTO leads VALUES
    (1,'Acme Corp',  85,'Alice', 50000.0),
    (2,'Globex',     NULL,'Bob',  NULL),
    (3,'Initech',    60, 'Bob',   NULL),
    (4,'Hooli',      92,'Alice', 80000.0),
    (5,'Pied Piper', NULL, NULL,  NULL),
    (6,'Stark',      78,'Carol',120000.0);

-- 🛠️ Step 1: select name, and use COALESCE(score, 0) aliased as score_safe.

-- 🛠️ Step 2: use COALESCE(assigned_to, 'Unassigned') aliased as rep.

-- 🛠️ Step 3: use COALESCE(revenue_est, 0.0) / NULLIF(score, 0) as revenue_per_pt,
--            ROUND to 2 decimal places.

-- 🛠️ Step 4: use COALESCE(score, 50) as score_or_default.

SELECT
    name,
    COALESCE(      , 0)              AS score_safe,
    COALESCE(      , 'Unassigned')   AS rep,
    COALESCE(revenue_est, 0.0)       AS est_revenue,
    ROUND(COALESCE(revenue_est, 0.0) / NULLIF(     , 0), 2) AS revenue_per_pt,
    COALESCE(      , 50)             AS score_or_default
FROM leads;

