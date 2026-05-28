# Wireframe notation — the visual language

How a wireframe in this skill looks and what its parts mean. Keep it **low-fidelity**: the goal is to communicate layout + behavior + open questions, not visual design.

## The signature: assumption badges + Design Assumptions table

This is the defining technique of the skill.

- Every interactive element whose **meaning, configurability, or behavior** the source does NOT fully specify gets a small numbered badge right after its label:
  ```html
  <label>Valid Until <span class="b">3</span></label>
  ```
- At the bottom of the screen, a **Design Assumptions** table lists each number as a **plain statement** of what the wireframe (and the build) was drawn against.
- The badge number ↔ table row number must match 1:1. Never leave a badge without a row, or a row without a badge.

This lets a client read the screen and immediately see "what did you assume" — and lets dev start building immediately.

### No status / approval workflow

Dev **builds against** the assumptions; it does **not** wait for the client to approve them. So the table has **no status column** (`Decided / To confirm / Need clarification` etc.). It is a flat list of statements. The screen carries one standing note near the table:

> *The dev team builds against these assumptions — no pre-approval needed. Flag anything that should differ and we'll record the change on the relevant user story.*

Optionally append a short *"(please flag if different)"* hint to the least-certain rows — but never a blocking status. When the client does flag something, absorb it as a **change on the corresponding US** (update its AC), mid-development.

## Visual rules

| Element | Rule |
|---|---|
| Palette | Grayscale only. The single accent (amber `#b8860b`) is reserved for assumption badges + the assumptions panel. Optional green flag for "NEW vs <source>". |
| Background | White sheet on a gray page; max-width ~1180px, centered. |
| Typography | System sans-serif. Bold large page title. Uppercase muted section headers. |
| Inputs | 1.5px solid black border, slight radius. Dashed border = read-only/auto. Placeholder text in gray. |
| Required | red asterisk `*`. |
| Sections | Separated by thin top borders + an uppercase muted `<h2>` label. |
| Tables | Header row underlined; thin row separators; tabular-aligned amounts. |
| Buttons | Bordered outline; the primary action filled black. |
| Breadcrumb | Show navigation context. If a former pop-up becomes a full page, tag it (e.g. `FULL PAGE — redirect (replaces the pop-up)`). |

## Section order (typical form screen)

1. Breadcrumb + page title (+ auto IDs on the right)
2. Header / meta fields
3. Main content (the entity being created/edited)
4. Line items / sub-table (if any)
5. Totals / summary
6. Secondary blocks (terms, signatures…)
7. Footer actions (Cancel / Save / Confirm …)
8. **Design Assumptions** table

## Logging assumptions

A badge in the HTML is not enough — assumptions must be **recorded** so the client is aware and any later feedback has a home. Log every assumption to a project tracker:

- Preferred: a **`WF Assumptions` sheet** in the project's Q&A workbook with columns `ID · Wireframe · Field/Area · Assumption (dev builds against this) · Client feedback`. **No status column** — dev does not wait for sign-off.
- Or a section in `docs/wireframe-changes.md`.
- ID format: `A-WF<NN>-<nn>` (e.g. `A-WF01-04`).
- ⚠️ If the Q&A workbook is **hand-maintained** (already contains filled answers), append the sheet via `openpyxl` load+edit — never re-run a generator that rebuilds it from scratch.

When the client gives feedback on an assumption: record it (Client feedback), then revise the wireframe **and** update the affected user story's AC — build-and-adjust, no approval gate.

## Why HTML (not an image format)

- Opens in any browser, zero dependencies → easy to share, export to PDF, screenshot.
- Diff-able in git (it's text).
- Fast to iterate (edit text, refresh).
- Annotations + assumption tables are just HTML — no design tool needed.

The `.html` is the **user-layer deliverable** in `output/wireframes/`; a token-cheap `.md` sidecar in `context/` describes it per the Core Rule.
