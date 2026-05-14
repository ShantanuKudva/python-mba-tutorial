# Exercise 16 — DATEDIF: Employee Tenure Calculator 🔴

**Scenario:** HR needs a tenure report for the six employees in the system. They want: years of service, months in the current year, a human-readable label ("5 yrs 3 mo"), and a salary-band flag based on tenure. DATEDIF is Excel's hidden gem for this.

## The sheet

```sheet
src: 02-excel/datasets/dates_data.xlsx.json
sheet: Employees
height: 260
```

Columns: A = EmpID, B = Name, C = HireDate, D = Department, E = Salary.

## Tasks

**Task 1 — Years of service (column F):**  
In F1, type `YearsService`. In F2:
```
=DATEDIF(C2, TODAY(), "Y")
```
Copy to F3:F8. Who is the most senior employee?

**Task 2 — Months in current year (column G):**  
In G1, type `MonthsThisYear`. In G2:
```
=DATEDIF(C2, TODAY(), "YM")
```
This returns the number of complete months beyond the last full year. So "5 years and 3 months" would return 3 here.

**Task 3 — Human-readable tenure label (column H):**  
In H1, type `TenureLabel`. In H2, concatenate the results of the two DATEDIF calls:
```
=DATEDIF(C2,TODAY(),"Y")&" yrs, "&DATEDIF(C2,TODAY(),"YM")&" mo"
```

**Task 4 — Tenure salary band (column I):**  
HR uses three bands based on years of service. In I1, type `SalaryBand`. In I2, use IFS:
- 5+ years → "Senior"
- 3+ years → "Mid-Level"
- Less than 3 → "Junior"

```
=IFS(F2>=5,"Senior", F2>=3,"Mid-Level", TRUE,"Junior")
```

**Task 5 — Total salary by band:**  
Below the data, use SUMIF to calculate total salary for each band. First, ensure column I is filled (copy down), then:
```
=SUMIF(I2:I7, "Senior", E2:E7)
=SUMIF(I2:I7, "Mid-Level", E2:E7)
=SUMIF(I2:I7, "Junior", E2:E7)
```

## Expected results (as of 2026)

| Name | HireDate | YearsService | SalaryBand |
|---|---|---|---|
| Alice Johnson | 2019-03-15 | ~7 | Senior |
| Bob Smith | 2021-07-01 | ~5 | Senior |
| Carol Lee | 2018-01-20 | ~8 | Senior |
| David Kumar | 2022-11-05 | ~3 | Mid-Level |
| Erin Walsh | 2020-06-30 | ~6 | Senior |
| Frank O'Brien | 2023-02-14 | ~3 | Mid-Level |

(Exact years depend on today's date when you run this.)

## Solution

<details>
<summary>Reveal solution</summary>

F2: `=DATEDIF(C2,TODAY(),"Y")` — copy to F3:F7

G2: `=DATEDIF(C2,TODAY(),"YM")` — copy to G3:G7

H2: `=DATEDIF(C2,TODAY(),"Y")&" yrs, "&DATEDIF(C2,TODAY(),"YM")&" mo"` — copy down

I2: `=IFS(F2>=5,"Senior",F2>=3,"Mid-Level",TRUE,"Junior")` — copy to I3:I7

Total salaries:
- Senior: `=SUMIF(I2:I7,"Senior",E2:E7)`
- Mid-Level: `=SUMIF(I2:I7,"Mid-Level",E2:E7)`
- Junior: `=SUMIF(I2:I7,"Junior",E2:E7)`

Key note: DATEDIF is undocumented in Excel's function wizard but works reliably. Always put start_date before end_date or you get an error.

</details>
