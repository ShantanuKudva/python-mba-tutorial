# Excel Datasets

Three sample workbooks are pre-loaded in the embedded spreadsheet blocks throughout the Excel phase. Each file is stored as a base64-encoded JSON (e.g. `sales.xlsx.json`) so it can be bundled into `site_data.js` without a server.

## Workbooks

### `sales.xlsx` — Quarterly Sales by Product & Region

Two sheets: **Q1** and **Q2**.

| Column | Description |
|---|---|
| Product | Widget, Gadget, License, Service, Cable, Plugin |
| Region | North, East, West |
| Jan / Feb / Mar (or Apr / May / Jun) | Monthly unit revenue |
| Q1 Total / Q2 Total | `=SUM(...)` formula across the three months |

Used in: Lesson 01 (SUM/AVG), Lesson 02 (absolute references), Lesson 04 (pivot thinking), exercises ex01–ex04.

### `pnl.xlsx` — P&L Statement

One sheet: **P&L** — a simplified income statement with formulas linking revenue, COGS, gross profit, and EBITDA rows.

| Section | Rows |
|---|---|
| Revenue | Product Sales, Services, Total Revenue |
| COGS | Materials, Labor, Total COGS |
| Gross Profit | Formula: Revenue − COGS |
| Gross Margin % | Formula: Gross Profit / Revenue |
| OpEx | Sales & Marketing, R&D, G&A, Total OpEx |
| EBITDA | Gross Profit − Total OpEx |

Used in: Lesson 01 (nested formulas), Lesson 02 (absolute references for margin %), exercises ex02, ex06.

### `customers.xlsx` — Customer List for Lookups

Two sheets: **Customers** (master list) and **Pricing** (lookup demo).

Customers columns: CustomerID, CompanyName, Region, Segment, AnnualRevenue, Discount.
Pricing columns: ProductID, ProductName, ListPrice, CustomerID, DiscountedPrice (uses `VLOOKUP`).

Used in: Lesson 03 (VLOOKUP / INDEX-MATCH), exercises ex03, ex05.

## How the base64 encoding works

Each `.xlsx.json` file contains a JSON object `{"filename": "...", "data": "<base64>"}`.

The spreadsheet enhancer in `playground.js` reads `window.FILES["02-excel/datasets/sales.xlsx.json"]`, parses the JSON, decodes the base64 string to a `Uint8Array`, then hands it to SheetJS (`XLSX.read(bytes, {type:'array'})`) and x-spreadsheet (`xs.loadData(...)`).

To regenerate the dataset files (if you update the data):

```bash
# From the repo root:
python3 -c "
import openpyxl, base64, json, io
# ... build wb, save to buf, then:
encoded = base64.b64encode(buf.read()).decode('ascii')
with open('02-excel/datasets/sales.xlsx.json', 'w') as f:
    json.dump({'filename': 'sales.xlsx', 'data': encoded}, f)
"
python3 build_site.py   # re-bundle
```
