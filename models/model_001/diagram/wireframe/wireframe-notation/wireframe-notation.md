# Wireframe notation — the visual language

How a wireframe in this skill looks and what its parts mean. Keep it **low-fidelity**: the goal is to communicate layout + behavior + open questions, not visual design.

## The signature: component-ID badges (no prose on the wireframe)

This is the defining technique of the skill.

- The wireframe HTML carries **no prose annotations**. Instead **every component is tagged with its component ID** as a small badge right after its label:
  ```html
  <label>Valid Until <span class="b">B3</span></label>
  ```
- IDs are **section-grouped**: `A`/`B`/`C`… = sections (top bar, details, items, totals…), the number = the component within the section. They match the companion `.md` `No./ID` column exactly.
- The badge ID ↔ `.md` component-spec row must match 1:1. Never leave a component without an ID, an ID without a spec row, or a spec row without a badge on the screen.
- **Assumptions are not badged directly.** A spec row references its assumption with `(Assumption n.)`; the assumptions are listed at the end of the `.md`. Read-only list screens carry the spec only (no assumptions).

This keeps the screen clean (a dev never mistakes a note for UI copy), while every component's full behavior + open questions are one ID lookup away in the companion `.md`. Compact tags (`NEW`, `catalog`/`custom`, required `*`) are allowed on the screen; full prose is not.

### No status / approval workflow

Dev **builds against** the assumptions; it does **not** wait for the client to approve them. So the assumptions list (in the companion `.md`) has **no status column** (`Decided / To confirm / Need clarification` etc.). It is a flat list of statements, carrying one standing note at the top:

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

1. Breadcrumb + page title (+ top-right actions for full-page; auto IDs near the title)
2. Header / meta fields
3. Main content (the entity being created/edited)
4. Line items / sub-table (if any)
5. Totals / summary
6. Secondary blocks (terms, signatures…)

(No assumptions table in the HTML — it lives in the companion `.md`. A short legend line under the title tells the reader the badges point to that companion doc.)

## Action bar placement

- **Full-page (standalone) screens:** put the primary actions in a **top-right action bar** in the header (title on the left), not at the bottom. Include an **Export PDF** action when the screen represents a document the customer receives (quotation, invoice, order). Conditional actions (e.g. *Generate Order*) live in the same bar and show/hide by state.
- **Pop-up / modal screens:** keep actions at the bottom of the modal (Cancel / Confirm), as modals are read top-to-bottom and dismissed at the bottom.

## Companion component-spec doc

Every wireframe ships with a **companion `.md`** next to the HTML — same folder, same base name (`WF-NN-<slug>.html` + `WF-NN-<slug>.md`). It carries the **dev-facing detail that the low-fi HTML deliberately omits**, so the HTML stays clean (avoids dev misreading inline notes as UI copy) while devs still get a precise spec.

Build it from [`../templates/wireframe-spec.md`](../templates/wireframe-spec.md). Contents:

1. **Header** — link back to the HTML, the source (story/CR/legacy), screen type, breadcrumb, and the build-against-assumptions note.
2. **Component specification** — one table per on-screen section (A, B, C…), using the SRS component-spec columns: `No./ID · Name / Label · Type · Attribute · Description`.
   - **Type** vocabulary: `Button · Text input · Number input · Dropdown (single/multi) · Date input · Text area · Icon button · Number (computed) · Display`.
   - **Attribute** vocabulary: `Required · Read-only · Disabled · Auto · Computed · Conditional · Default: x · > 0 · ≥ 0 · …`.
   - Cross-reference assumptions inline with `(Assumption n.)` so each component ties to its badge.
   - Add a small **Status-based locking / Conditional behavior** table when the screen has state-dependent rules.
3. **Design Assumptions** — the same flat list as the HTML (no status), with `(please flag if different)` on the least-certain rows.
4. **Linked artifacts** — user story, Q&A workbook, change tracker.

Keep the HTML and the companion `.md` in sync: badge ① on the HTML = component row referencing `(Assumption 1.)` = row #1 in the assumptions list.

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
