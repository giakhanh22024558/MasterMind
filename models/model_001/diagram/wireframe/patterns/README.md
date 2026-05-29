# wireframe · patterns

Reusable screen patterns. Each is a layout recipe built from the [base shell](../templates/wireframe-base.html).

## Form screen (create / edit an entity)

Top-right action bar → header/meta → main fields → (line-item table) → totals/summary → terms. (No assumptions section on the screen — that lives in the companion `.md`.)

- Group fields into `<div class="sec">` sections with uppercase `<h2>` labels.
- `g2` / `g3` grids for field rows.
- Read-only/auto fields use `.ro` (dashed border) — **no `.hint`**; behavior goes in the `.md`.
- Required fields get a red `*`.
- **Tag every component** with its component-ID badge (`A1`, `B2`…) matching the `.md` spec.

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
3. Give each field a component-ID badge + a `.md` spec row. For any legacy field whose meaning/config the client hasn't restated, **record an assumption in that spec row** (`(Assumption n.)`) and in the assumptions list (this is where most assumptions come from).

## Backend admin shell (sidebar)

Backend/admin screens of the same product should share one **left sidebar** so the set looks consistent. Layout: `.app { display:flex }` → `.nav` (fixed-width left column of menu items, the active one highlighted) + `.content` (flex:1). Reuse the **same item list** across every screen of that product; only the active item changes. (Storefront/customer screens don't use the admin sidebar.)

## Interactive state (lightweight JS)

When a screen has a state that's hard to show statically, add a tiny inline `<script>` to demo it — keep it dependency-free:

- **Lock-on-status:** a `<select>` `onchange` toggles a `locked` class on the sheet → CSS greys/disables fields, and reveals a conditional action (e.g. *Generate Order* when Accepted).
- **Mutually-exclusive panels:** radio `onclick` shows one panel, hides the other (e.g. Delivery vs Store Pickup).
- **Add/remove rows:** a button appends a blank row; a row trash icon `onclick="this.closest('tr').remove()"`.

The behavior is still written in the companion `.md` so the static read is complete.

## Marking components & change type

- **Component-ID badge** (`A1`, `B2`…) on **every** component — maps to the `.md` spec row. This is the only required marker.
- `NEW vs <source>` (green flag) for sections/fields not in the original spec.
- Compact state tags only (e.g. `catalog` / `custom`, required `*`).
- **No prose notes / `.hint` on the screen** — all behavior text lives in the companion `.md`.
- A read-only **list** screen needs **no component IDs and no assumptions** — it's a plain snapshot + (optional) a short note.
