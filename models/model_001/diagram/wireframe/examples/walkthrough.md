# wireframe · walkthrough — Create Quotation (standalone)

A worked example showing the full method: derive from sources → draw → badge assumptions → log for confirmation.

## Context

A change request asks to let backend staff create a **quotation without a prescription** (previously quotations were a pop-up launched from a prescription). The client also said the new quotation must carry **all the fields of their legacy paper quotation** (provided as a PDF in `input/`), but did NOT specify which fields are configurable or what some mean.

## Steps taken

1. **Identify sources**
   - SRS Figure 9/10 (the existing Create/Edit Quotation pop-up) → fields: Status, item rows (Item name / Qty / Unit price / Total), Total, Cancel/Confirm.
   - `input/quotation template.pdf` (legacy) → many more fields: Quotation No/Date/Valid Until/Remarks, Customer (Address/Contact/Email), line items with **Code, Description, Price, Qty, DISC%, Amount**, **VAT/Discount/Net**, Payment method note, T&C, Prepared/Checked By, company header.
   - Q&A answers → status enum changed to 5 values; standalone creation confirmed.

2. **Decide screen type** — NEW standalone full page (pop-up → redirect). Tag the breadcrumb `FULL PAGE — redirect (replaces the pop-up)`.

3. **Lay out sections** (form-screen pattern): Quotation details → Customer/Billing (`NEW vs SRS` flag) → Items table (with the legacy `Disc %` column) → Totals (Gross/Discount/VAT/Net) → Payment & Terms → actions.

4. **Badge every gap.** The legacy PDF showed fields but not their rules, so each became an assumption:
   - Quotation No auto-generated? ①
   - Valid Until = +7 working days? ③
   - Disc % vs an overall Discount — meaning? ④⑤
   - VAT rate fixed/configurable, prices tax-inclusive? ⑥
   - Payment note / T&C fixed or editable? ⑦⑧
   - Checked By = approval workflow? ⑩
   - …15 in total.

5. **Save** to `output/wireframes/WF-01-create-quotation-standalone.html` (self-contained HTML). Add a `context/wireframes.md` sidecar.

6. **Log assumptions** to the project Q&A workbook as a `WF Assumptions` sheet (`A-WF01-01 … A-WF01-15`, Status `Need clarification`), appended via `openpyxl` load+edit so the already-answered SRS Q&A responses were preserved.

## Lessons this example encodes

- Most assumptions come from **replicating a legacy document** whose field semantics the client never restated — exactly the place to be explicit rather than guess silently.
- The wireframe doubles as a **clarification artifact**: a client reading it sees both the proposed UI and the precise list of things to confirm.
- Keep the deliverable **client-ready** (English, self-contained, exportable).
