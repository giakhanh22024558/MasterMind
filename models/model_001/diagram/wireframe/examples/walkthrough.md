# wireframe · walkthrough — Create Quotation (standalone)

A worked example of the full method: derive from sources → draw a clean screen → tag every component with its ID → put all detail (component spec + assumptions) in the companion `.md`.

## Context

A change request asks to let backend staff create a **quotation without a prescription** (previously quotations were a pop-up launched from a prescription). The client also wants the new quotation to carry **all the fields of their legacy paper quotation** (a PDF in `input/`), but did NOT specify which fields are configurable or what some mean.

## Steps taken

1. **Identify sources**
   - SRS Figure 9/10 (the existing Create/Edit Quotation pop-up) → Status, item rows (Item name / Qty / Unit price / Total), Total, Cancel/Confirm.
   - `input/quotation template.pdf` (legacy) → many more fields: Quotation No/Date/Valid Until/Remarks, Customer (Address/Contact/Email), line items with **Code, Description, Price, Qty, DISC%, Amount**, **VAT/Discount/Net**, Payment note, T&C, Prepared/Checked By, company header.
   - Q&A answers → status enum = 5 values; standalone creation confirmed; discount/VAT split confirmed.

2. **Decide screen type** — NEW standalone full page (pop-up → redirect). Breadcrumb tagged `FULL PAGE — redirect (replaces the pop-up)`; actions go **top-right** + an **Export PDF** (it's a document screen).

3. **Lay out sections** (form-screen pattern): Quotation details → Customer/Billing (`NEW vs SRS` flag) → Items (with legacy `Disc %` + `VAT %`) → Totals → Payment & Terms.

4. **Tag every component with its ID.** Section-grouped IDs that match the companion `.md` `No./ID`: `A1–A4` (top-bar actions), `B1–B6` (details, incl. Reference Prescription), `C1–C4` (customer), `D1–D9` (items), `E1–E5` (totals), `F1–F5` (payment/terms). **No prose, no `.hint`, no assumptions table on the screen** — only the ID badges + compact tags (`NEW`, required `*`).

5. **Write the companion `.md`** (`WF-01-create-quotation-standalone.md`): one component-spec table per section using those IDs, with `(Assumption n.)` on any row whose behavior the client hasn't pinned down. The legacy PDF showed fields but not their rules, so ~15 rows reference an assumption (Quotation No format, Valid Until, Disc% vs overall Discount, VAT, Payment note / T&C editability, Checked By workflow, Email default…). The assumptions are then listed at the end of the `.md` (no status — dev builds against them).

6. **Mirror assumptions** to the project Q&A workbook (`WF Assumptions` sheet, `A-WF01-01 …`), appended via `openpyxl` load+edit so the already-answered SRS Q&A responses were preserved.

7. **Interactive states in the HTML** where cheap (here: a small script locks Items + Customer/Billing + Payment & Terms and reveals *Generate Order* when Status = Accepted) — behavior still documented in the `.md` spec.

## Companion list screen

The Quotation **list** (`WF-10`) followed the list pattern: component-ID badges on toolbar/columns/pagination, **component spec only, no assumptions** (read-only overview).

## Lessons this example encodes

- Most assumptions come from **replicating a legacy document** whose field semantics the client never restated — be explicit in the `.md` spec rather than guess silently on the screen.
- Keep the **screen clean** (IDs only) and put **all detail in the companion `.md`** — devs map by ID, and never mistake a note for UI copy.
- Build **against** assumptions; client feedback becomes a change on the relevant US (no approval gate).
- Keep the deliverable **client-ready** (English, self-contained, exportable).
