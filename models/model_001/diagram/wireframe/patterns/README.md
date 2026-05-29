# wireframe · patterns

Reusable screen patterns. Each is a layout recipe built from the [base shell](../templates/wireframe-base.html).

## Form screen (create / edit an entity)

Header/meta → main fields → (line-item table) → totals/summary → terms → actions → assumptions.

- Group fields into `<div class="sec">` sections with uppercase `<h2>` labels.
- `g2` / `g3` grids for field rows.
- Read-only/auto fields use `.ro` (dashed border) + a `.hint`.
- Required fields get a red `*`.

## List / table screen

A toolbar (filters, search) above a `<table>`, then pagination. For a brand-new list, top-right actions hold the primary "+ Create …" and an Export.

**No assumption badges on a read-only list.** List screens are overviews, not data-entry forms — the **companion `.md` carries only the component spec** (columns, filters, actions, pagination), and the `.md` header states *"List screen — no design assumptions tracked here."* Only add a badge + assumption if the list introduces a genuinely underspecified interactive decision. For "add column X to an existing list" CRs, a `NEW vs <source>` flag on the column header is enough.

## Detail screen

Read-mostly. Left = primary content, right = a side panel (status, metadata, "Created by", actions). Tag action buttons that are conditionally shown (e.g. "shown only when payment = Payable Link").

## Pop-up → full-page conversion

When a CR turns a modal into a standalone page:
- Add a breadcrumb showing the new navigation path.
- Tag it `FULL PAGE — redirect (replaces the pop-up)` so reviewers see the interaction change.
- Keep the same field set unless the CR changes it.

## Replicating a legacy document

When the client wants a legacy paper/PDF form replicated (e.g. an old quotation):
1. Read the legacy file from `input/` first.
2. Map every legacy field into the screen — even ones the new SRS omitted.
3. For each legacy field whose meaning/config the client hasn't restated, add an **assumption badge** (this is where most assumptions come from).

## Annotating change type

- `NEW vs <source>` (green flag) for sections/fields not in the original spec.
- Assumption badge ①②③ for anything underspecified.
- A short `.hint` under a field for behavior notes that are NOT open questions.
