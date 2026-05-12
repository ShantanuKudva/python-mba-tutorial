# Lesson 2 — Cell References: Relative, Absolute, and Named Ranges

## Why this matters

You've built a gross-margin formula in cell G2. You copy it down to G3, G4, G5 — and suddenly the numbers look wrong. That's a relative reference moving when it shouldn't. Understanding the difference between `C2`, `$C2`, `C$2`, and `$C$2` is the single most common Excel skill gap in MBA classrooms, and fixing it takes 30 seconds once you know the rule.

## The preloaded sheet (P&L)

The P&L sheet below has revenue, COGS, and gross profit rows. Cells that use formulas reference other cells — and the type of reference matters when you copy a formula.

```sheet
src: 02-excel/datasets/pnl.xlsx.json
sheet: P&L
height: 420
```

## Relative references — `C2`

A relative reference shifts when you copy a formula. If `G2 = C2 - C8` and you copy G2 to G3, it becomes `C3 - C9`. The row number moves by the same offset you moved.

**When to use:** most ordinary formulas where you want each row to refer to its own data.

## Absolute references — `$C$2`

The `$` locks the row, the column, or both. `$C$2` always refers to column C, row 2 — no matter where you paste the formula.

```sheet
src: 02-excel/datasets/pnl.xlsx.json
sheet: P&L
```

```
=$C$4 - $C$8     ← Gross profit formula: always row 4 minus row 8
=$C$4 / $G$4     ← Gross margin %: absolute reference to the "Full Year" total
```

**When to use:** when the formula must always point at the same cell — a tax rate, a target margin, a total row.

## Mixed references — `$C2` and `C$2`

`$C2` locks the column but not the row (moves down as you copy down).  
`C$2` locks the row but not the column (moves right as you copy right).

These appear in multiplication tables and lookup helpers. You'll see them more in Lesson 3.

## Keyboard shortcut

Press **F4** while your cursor is inside a cell reference in the formula bar to cycle through `C2` → `$C$2` → `C$2` → `$C2` → `C2`.

---

## Named ranges

Instead of `$C$4`, you can name that cell `TotalRevenue` and write `=TotalRevenue - $C$8`. This makes formulas self-documenting.

To name a cell or range:
1. Select the cell(s).
2. Click the **Name Box** (the small field at the top-left that shows the cell address).
3. Type the name and press Enter.

In this embedded sheet, you can reference a named range in a formula once you've created it — try naming cell C4 `Q1Revenue` and referencing it in a formula below the table.

---

## Tasks — do these in the sheet above

```sheet
src: 02-excel/datasets/pnl.xlsx.json
sheet: P&L
```

1. Click on **cell C10** (Gross Profit row). Confirm the formula is `=C4-C8`. Now look at D10 — does it say `=D4-D8`? If you see a raw number instead of a formula, type `=D4-D8` in D10 and press Enter.

2. **Cell C11** (Gross Margin %): enter `=C10/C4`. Copy this formula to D11, E11, F11. Do the denominators shift correctly (D4, E4, F4)?

3. Now add a **target margin** in a standalone cell (say, row 20, column A: label it "Target Margin %", column B: value `0.35`). Then in C12 (a new row), write a formula `=IF(C11>=$B$20,"Above target","Below target")`. Copy it across to D12, E12, F12. The `$B$20` must stay locked — confirm by checking the formula in E12.

4. In the Name Box (top-left of the sheet), name cell G4 `FullYearRevenue`. Then write `=FullYearRevenue * 0.10` in any empty cell to compute a 10% revenue target.

---

## Try it

In the P&L sheet above, find the Gross Margin % row. The formula in column C should be `=C10/C4`. Change the revenue figure in C2 (Product Sales, Q1 Actual). Watch how the margin percentage in C11 updates automatically — that's the power of cell references.

---

## Common mistakes

- **Locking both when you only need one:** `$C$2` when copying across columns should probably be `$C2` (lock column, let row move).
- **Named range typos:** names are case-insensitive but must start with a letter and contain no spaces. Use underscores: `Total_Revenue`.
- **Circular reference:** if a formula refers to itself (directly or indirectly), Excel will warn you. Check for a loop in your reference chain.

---

Next: [Lesson 3 — Lookups](03-lookups.md)

---

## Resources

- [Microsoft — relative and absolute references](https://support.microsoft.com/en-us/office/switch-between-relative-absolute-and-mixed-references-dfec08cd-ae65-4f56-839e-5f0d8d0baca9)
- [Chandoo.org — named ranges explained](https://chandoo.org/wp/named-ranges-in-excel/)
