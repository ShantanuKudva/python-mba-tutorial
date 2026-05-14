/*
Exercise 15 — NULL Filtering: Find Incomplete Leads

Concepts: IS NULL, IS NOT NULL, WHERE, NULL semantics
Lesson: 03-sql/week-5/lessons/08-nulls-and-data-types.md
Difficulty: Easy

Goal: From a leads table, write two queries:
  1. Return name and region of all leads where score IS NULL (unscored leads).
  2. Return name and assigned_to for all leads that have been assigned
     (assigned_to IS NOT NULL) but have no revenue estimate (revenue_est IS NULL).

Expected output for query 1 (unscored leads):
    name        region
    ----------  ------
    Globex      East
    Pied Piper  East

Expected output for query 2 (assigned but no revenue estimate):
    name     assigned_to
    -------  -----------
    Initech  Bob
*/

-- 📦 SETUP
DROP TABLE IF EXISTS leads;
CREATE TABLE leads (
    id          INTEGER PRIMARY KEY,
    name        TEXT,
    region      TEXT,
    score       INTEGER,
    assigned_to TEXT,
    revenue_est REAL
);
INSERT INTO leads VALUES
    (1,'Acme Corp',  'North', 85,'Alice', 50000.0),
    (2,'Globex',     'East',  NULL,'Bob',   NULL),
    (3,'Initech',    'West',  60, 'Bob',    NULL),
    (4,'Hooli',      'North', 92,'Alice',  80000.0),
    (5,'Pied Piper', 'East',  NULL, NULL,   NULL),
    (6,'Stark',      'West',  78,'Carol', 120000.0);

-- 🛠️ Step 1: query 1 — return name and region where score IS NULL.

SELECT
FROM leads
WHERE ;

-- 🛠️ Step 2: query 2 — return name and assigned_to where assigned_to IS NOT NULL
--            AND revenue_est IS NULL.

SELECT
FROM leads
WHERE
  AND ;

