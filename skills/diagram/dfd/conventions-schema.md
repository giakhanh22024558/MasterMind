# DFD · conventions schema

The full list of conventions a DFD needs. Use this as a **checklist** when reading a project's `diagram-conventions.md` or asking the user to fill in defaults.

For each item, the project should specify a value or accept the default from [`conventions-defaults.md`](conventions-defaults.md).

## 1 · Canvas-overlay source

Which master architecture file does the DFD overlay on?

- File path (e.g. `diagrams/1-overview/<project>-architecture.drawio`)
- This is the **single source of truth** — all DFDs in the project copy from this file

## 2 · Yourdon notation shapes

For each DFD element, define the visual representation:

- **Process** (circle in classical Yourdon · rounded box if matching architecture style for cross-mapping)
- **Data store** (cylinder · usually matches architecture's storage cell style)
- **External entity** (rectangle · usually matches architecture's external zone style)
- **Data flow** (arrow with payload label)

See [`yourdon-notation.md`](yourdon-notation.md) for the visual vocabulary.

## 3 · Process numbering scheme

- **Format** (default: Yourdon `N.M` — `1.0`, `2.0`, `2.1`, `2.2`, …)
- **Numbering source** — sequential? spec-aligned? hierarchical by sub-process?

## 4 · Edge styles

For each edge type the project uses on DFDs:

- **Data flow** (default: dotted purple `stroke-dasharray:2 3` · matches architecture data-payload style)
- **Trigger flow** (default: same data-flow style + `TRIGGER:` prefix on label)
- **Prohibited flow** (default: red dashed `stroke-dasharray:5 5` + `[X] PROHIBITED` label)
- **Read flow** (data flow direction `Store → Process`)
- **Write flow** (data flow direction `Process → Store`)

## 5 · Grey-out style for out-of-scope cells

When using canvas-overlay method, non-scope cells are greyed and emptied:

- **Fill color** (default: `#f5f5f5` very light grey)
- **Stroke color** (default: `#bdbdbd` light grey)
- **Stroke width** (default: 1px)
- **Font color** (default: `#bdbdbd`)
- **Value** (default: empty string)
- **Structural properties to preserve** (default: shape · container · dashed · rounded · arcSize)

## 6 · Process number prefix style

When adding `N.M` numbers to in-scope component labels:

- **Position** — before the existing component ID (default) · after · separate line
- **Format** — bold? italic? colored?

Example default: `<b>1.0</b> · <i><Component-ID></i> · <b><Component-Name></b>`

## 7 · DFD legend block

Every DFD `.drawio` should include a legend cell explaining the overlay conventions. Project should specify:

- **Position** (default: bottom of file, full-width banner)
- **Style** (default: pale fill, dashed border, distinct from architecture cells)
- **Content sections** (default: CANVAS PRINCIPLE · SCOPE OF THIS FILE · OVERLAYS ADDED · LABEL CONVENTIONS · WHEN TO USE · CROSS-REFS)

See [`canvas-overlay-method.md`](canvas-overlay-method.md) for the standard legend template.

## 8 · KEEP_IDS scope policy

The grey-out script needs to know which cells to keep colored + textual:

- **In-scope subsystem** — container + all its components
- **Direct touchpoints** — stores the subsystem reads/writes · external entities it consumes from · architecture barriers framing the subsystem
- **Always-keep** — `DFD_LEGEND` cell

Project should clarify (per DFD scope) what counts as "direct touchpoint" — usually obvious from spec but document edge cases.

## 9 · TRIGGER prefix convention

- **Format** (default: `TRIGGER: <event description>`)
- **When to use** — only on edges that initiate execution of the destination process (not for every data-flow edge)

## 10 · Companion markdown structure

For the `.md` companion to each `.drawio`:

- Required sections (default list):
  - Notation key
  - Mermaid version of DFD
  - Process catalogue table
  - Trigger inventory
  - Storage tech mapping
  - Process independence/dependency map
  - Architectural constraints
  - Cross-references

## Checklist (for skill agent)

When loading a project's `diagram-conventions.md` for DFD work:

- [ ] Canvas-overlay source file identified
- [ ] Yourdon notation choices clear
- [ ] Process numbering scheme defined
- [ ] Edge styles resolved (or accept defaults)
- [ ] Grey-out style resolved
- [ ] KEEP_IDS scope policy clear for this specific DFD's subsystem
- [ ] Legend block content sections agreed

If any item is ambiguous, **ask the user** before proceeding.
