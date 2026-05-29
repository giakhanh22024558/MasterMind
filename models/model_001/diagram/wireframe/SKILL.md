---
name: diagram/wireframe
description: Draw low-fidelity UI wireframes (screen mockups) as self-contained annotated HTML, for new or changed screens derived from requirements / change requests / Q&A. Each interactive element is numbered with a badge that maps to a "Design Assumptions" table, so any field the client has not fully specified is designed against an explicit assumption and logged for confirmation. Use when the user asks to draw/mock up a screen, visualize a UI change from a CR, or produce client-facing wireframes for sign-off. Not for data ERDs (use diagram/erd) or system architecture (use diagram/architecture).
---

# Wireframe diagram sub-skill

For **low-fidelity UI wireframes** — screen mockups that show layout, fields, and behavior for a new or changed screen, rendered as a **single self-contained HTML file** (grayscale, no external assets) that opens in any browser and exports cleanly to PDF/screenshot for client review.

The signature of this skill: the wireframe HTML carries **no prose annotations** — instead **every component is tagged with its component ID** (`A1`, `B2`, `C3`…) as a small badge. Each ID maps 1:1 to a row in the **component spec table** in the companion `.md`, and that row references a **Design Assumption** if the component has one. So the screen stays clean (no notes/hints a dev could mistake for UI copy), and anyone can look up a component's full behavior + open questions by its ID.

- IDs are section-grouped: `A`/`B`/`C`… = the screen's sections (top bar, details, items, totals…); the number is the component within that section. They match the companion `.md` `No./ID` column exactly.
- **No `.hint`, no inline note sentences** in the HTML. Compact tags (`NEW`, `catalog`/`custom`, `required *`) are allowed; full prose belongs in the `.md`.
- Assumptions are **not** badged directly — they are reached via the component spec row (`(Assumption n.)`), and listed at the end of the `.md`. (Read-only list screens carry the spec only, no assumptions.)

## Build-against-assumptions (do NOT block on client sign-off)

The dev team **proceeds to implement the user stories against the assumptions** — it does **not** wait for the client to approve them first (waiting wastes time). Assumptions are recorded purely so the client is **aware** of what was assumed and can give feedback.

- The wireframe carries a standing note: *"Dev builds against these assumptions; flag anything that should differ and we'll record the change on the relevant user story."*
- If the client later disagrees with an assumption, it's handled as a **change on the corresponding US** (update the AC) — build-and-adjust, mid-development. No separate approval gate.
- Therefore the Design Assumptions list (in the companion `.md`) has **no status/approval column** (no "Decided / To confirm / Need clarification" workflow). It's a flat list of statements the build was made against. Optionally mark the least-certain ones with a short *"(please flag if different)"* hint — but never a blocking status.

## When to use this sub-skill

Invoke when the user asks you to:

- **Draw / mock up a screen** ("vẽ wireframe", "draw the X screen", "mockup màn X")
- **Visualize a UI change** from a change request, SRS feature, or Q&A clarification
- **Produce client-facing wireframes** for confirmation/sign-off
- **Show a screen the client asked to see** (e.g. "client wants to see the rider portal UI")

For data models use [`../erd/`](../erd/); for system/component architecture use [`../architecture/`](../architecture/).

## First step in any wireframe work

1. **Discover conventions** — read `<project-root>/wireframe-conventions.md` per [`meta/conventions-as-data-pattern/`](../../../../core/meta/conventions-as-data-pattern/); fall back to [`conventions-defaults/`](conventions-defaults/).
2. **Work from a source** — a wireframe is **derived** from a requirement / SRS figure / CR / Q&A answer, not invented. Identify the source screen (existing wireframe to update, or a new screen) and the exact change.
3. **Gather reference material** — existing screenshots in `input/`, the SRS figures, and any legacy template (e.g. an old document the client wants replicated). Read them first.
4. **Mark every gap as an assumption** — if the source does not specify a field's meaning / configurability / behavior, design against a reasonable assumption, badge it, and log it (see [`wireframe-notation/`](wireframe-notation/)).

## Content modules

| Module | Purpose |
|---|---|
| [`conventions-schema/`](conventions-schema/) | What a project must define (format, file naming, output dir, assumption tracker location) |
| [`conventions-defaults/`](conventions-defaults/) | Defaults: self-contained HTML, grayscale low-fi, `output/wireframes/WF-NN-<slug>.html` |
| [`wireframe-notation/`](wireframe-notation/) | The visual language: badge annotations, Design Assumptions table, section/field patterns, the base HTML shell |
| [`templates/`](templates/) | `wireframe-base.html` (HTML shell) + `wireframe-spec.md` (companion component-spec doc) |
| [`patterns/`](patterns/) | Reusable screen patterns (form screen, list/table screen, detail screen, pop-up→full-page) |
| [`examples/`](examples/) | Worked walkthrough (Create Quotation standalone) |
| [`scripts/`](scripts/) | Helper scripts (if applicable) |

## Workflow

### Workflow A · Draw a new screen

1. **Identify the source** (CR / SRS figure / Q&A) and confirm it's a NEW screen vs an update.
2. **Copy the base shell** from [`templates/wireframe-base.html`](templates/) — gives you the CSS, badge styles, and the Design Assumptions table.
3. **Lay out sections** top-to-bottom (header/meta → main content → totals/summary → actions). Use the patterns in [`patterns/`](patterns/).
4. **Tag every component** with its component ID badge `<span class="b">B2</span>` (matching the `.md` `No./ID`). **No prose annotations** in the HTML; **no assumptions table** in the HTML. For a field the source doesn't fully specify, record the assumption in the `.md` spec row + assumptions list (the badge is the component ID, not the assumption number).
5. **Save** to `output/wireframes/WF-NN-<slug>.html` (per conventions). Add a `.md` sidecar in `context/` per the Core Rule.
6. **Write the companion component-spec doc** `output/wireframes/WF-NN-<slug>.md` (same folder, same base name) from [`templates/wireframe-spec.md`](templates/wireframe-spec.md): a component-specification table per on-screen section + the Design Assumptions list (`badge ① ↔ Assumption 1`). This is where the assumptions live and the dev-facing detail the low-fi HTML omits — see [`wireframe-notation/`](wireframe-notation/#companion-component-spec-doc).
7. **Log assumptions** to the project tracker (e.g. a "WF Assumptions" sheet in the Q&A workbook, or `docs/wireframe-changes.md`) so the client is aware — see [`wireframe-notation/`](wireframe-notation/#logging-assumptions). Dev does **not** wait for sign-off; changes are absorbed on the relevant US.

### Workflow B · Update an existing screen

1. Locate the source screen (SRS figure / existing wireframe / screenshot in `input/`).
2. Reproduce the **relevant** part of the layout — annotate only what changes (tag changed areas, e.g. `NEW vs SRS`).
3. Same assumption-badge discipline for anything underspecified.

### Workflow C · Client language

Wireframes meant for client sign-off must be in the **client's language** (default English unless the project says otherwise). Internal hints may be bilingual, but field labels, the Design Assumptions table, and annotations on a client-facing wireframe should match the language the client confirms in.

## Anti-patterns

- ❌ **Prose annotations / `.hint` notes in the HTML** — the wireframe carries component-ID badges only; all behavior text lives in the companion `.md`. (Compact tags like `NEW` are fine.)
- ❌ A component on the screen with **no ID badge**, or an ID badge with **no matching `.md` spec row** — keep them 1:1.
- ❌ Inventing field behavior silently — if the source doesn't specify it, record it as an explicit assumption in the `.md` spec row, never a hidden decision.
- ❌ **Blocking development on client sign-off of assumptions** — dev builds against them; changes are absorbed on the US. Do not add a status/approval workflow to the assumptions.
- ❌ High-fidelity / pixel-perfect styling — this skill is **low-fi**; color is for structure (sections) and annotations only.
- ❌ External dependencies (web fonts, CDN CSS, images) — wireframes must be **single self-contained HTML** so they open offline and export cleanly.
- ❌ Losing assumptions — record each in the companion `.md` (spec row ref + list) AND the project tracker.
- ❌ Re-running a generator that overwrites a hand-maintained client file (e.g. a Q&A workbook with filled answers) — append via load+edit instead.
- ❌ Mixing languages on a client-facing wireframe.

## Cross-references

| Reference | Used for |
|---|---|
| [Core Rule](../../../../core/core-rule/) | HTML wireframe = user-layer deliverable in `output/`; `.md` sidecar in `context/` |
| [`../../document/features/`](../../document/features/) | Stories/AC are the source a wireframe visualizes |
| [`../../document/analysis/`](../../document/analysis/) | CR Q&A produces the changes a wireframe renders |
| [meta/conventions-as-data](../../../../core/meta/conventions-as-data-pattern/) | Project conventions live in `<project>/wireframe-conventions.md` |
| [meta/uniform-skill-structure](../../../../core/meta/uniform-skill-structure/) | This skill follows the mandatory layout |
