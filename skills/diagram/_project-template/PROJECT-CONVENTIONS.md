# Diagram conventions for `<your-project-name>`

**How to use this file:**

1. Copy this template to `<your-project-root>/diagram-conventions.md`
2. Fill in your project's specifics in each section
3. Leave sections blank to accept the skill's defaults
4. Update as your project's conventions evolve

This file is read by the [diagram skill](https://github.com/giakhanh22024558/MasterMind) before any diagram work — it tells the skill how YOUR project visualizes things, rather than imposing defaults from elsewhere.

---

## General conventions (cross-diagram-type)

### Decision-ID prefix scheme

How your project organizes design-decision row IDs in `research/design-decisions.md`:

| Prefix | Category | Examples |
|---|---|---|
| `<fill in>` | <e.g. system-wide infra> | `S1`, `S2`, … |
| `<fill in>` | <e.g. backend-specific> | `B1`, `B2`, … |
| `<fill in>` | <e.g. mobile-specific> | `M1`, `M2`, … |
| `<fill in>` | <e.g. mobile architecture sub-decisions> | `M0a`, `M0b`, … |
| `<fill in>` | <e.g. visual conventions> | `V1`, `V2`, … |

### Spec authority code format

Pattern for citing external specs / standards: `<example: PROJECT-DOMAIN-NNNN>`

Common spec authority codes used in this project:
- `<CODE>` — `<what this spec covers>`
- `<CODE>` — `<what this spec covers>`
- …

### Rejection trigger format

Pattern for named rejection triggers: `<example: RT-NN>`

Active rejection triggers in this project:
- `RT-XX` — `<description>`
- …

### Folder structure

The project uses the 4-tier layout from [`_shared/folder-structure-general.md`](https://github.com/giakhanh22024558/MasterMind/blob/main/skills/diagram/_shared/folder-structure-general.md):

- ✅ `diagrams/1-overview/`
- ✅ `diagrams/2-subsystems/`
- ✅ `diagrams/3-flows/data-flow/`
- ✅ `diagrams/3-flows/state/`
- ✅ `diagrams/4-cross-cutting/`
- ✅ `research/design-decisions.md`
- ✅ `.scripts/`

(Mark deviations from this default with ❌ + rationale.)

---

## Architecture diagram conventions

(Read by [`architecture/SKILL.md`](https://github.com/giakhanh22024558/MasterMind/blob/main/skills/diagram/architecture/SKILL.md). See [`architecture/conventions-schema.md`](https://github.com/giakhanh22024558/MasterMind/blob/main/skills/diagram/architecture/conventions-schema.md) for the full checklist.)

### Zone color palette (override or accept defaults)

| Zone purpose | Fill | Stroke | Notes |
|---|---|---|---|
| <Zone name 1> | `<#hex>` | `<#hex>` | <e.g. "Mobile · UI layer"> |
| <Zone name 2> | `<#hex>` | `<#hex>` | … |
| … | | | |

To accept all defaults, write: "Use defaults from `architecture/conventions-defaults.md`."

### Component box default style

- Fill: `<#hex or "default">`
- Stroke: `<#hex or "default">`
- Shape: `<rounded rectangle · cylinder · etc.>`

### Special node variants

- **Provisional cell** (preemptive commit pending confirmation): `<style or "default">`
- **Inert scaffold / future phase**: `<style or "default">`
- **Compliance banner**: `<style or "default">`

### Edge styles

- **Solid operational** (default): `<acceptable as-is or override>`
- **Dotted purple data payload** (default): `<acceptable or override>`
- **Red dashed prohibited** (default): `<acceptable or override>`
- **Orange dashed conditional / consent-gated** (default): `<acceptable or override>`

### Edge granularity policy

- **Default**: layer ↔ layer / sub-group ↔ sub-group
- **Storage exception enabled?** Yes / No (default: Yes)
- **Other exceptions in this project**: `<list any deviations + rationale>`

### Layout

- Mermaid layout engine: `<default: elk>`
- Diagram direction: `<LR · TB>`
- Page width: `<value>`
- Component width: `<value>`

---

## DFD conventions

(Read by [`dfd/SKILL.md`](https://github.com/giakhanh22024558/MasterMind/blob/main/skills/diagram/dfd/SKILL.md). See [`dfd/conventions-schema.md`](https://github.com/giakhanh22024558/MasterMind/blob/main/skills/diagram/dfd/conventions-schema.md) for the full checklist.)

### Canvas-overlay source

Master architecture file path that DFDs overlay on:

`<e.g. diagrams/1-overview/myproject-architecture.drawio>`

### Yourdon notation choice

- **Process shape**: `<rounded box · classical circle · …>` (default: rounded box for canvas-overlay consistency)
- **Data store shape**: `<cylinder · open rectangle · …>` (default: cylinder)
- **External entity shape**: `<rounded box · square · …>` (default: rounded box)

### Process numbering scheme

- Format: `<e.g. Yourdon N.M>` (default: Yourdon N.M)
- Convention for sub-processes: `<2.1, 2.2, …>` (default)

### Edge styles

- **Data flow**: `<accept default · override>`
- **Trigger flow**: `<same as data flow + TRIGGER: prefix>` (default)
- **Prohibited flow**: `<accept default · override>`

### Grey-out style

- Fill: `<#hex>` (default: `#f5f5f5`)
- Stroke: `<#hex>` (default: `#bdbdbd`)
- Font: `<#hex>` (default: `#bdbdbd`)

### Companion markdown structure

Each DFD `.drawio` has a `.md` companion with sections (mark which apply):

- ✅ Notation key
- ✅ Storage tech mapping
- ✅ Mermaid version
- ✅ Process catalogue table
- ✅ Trigger inventory
- ✅ Process independence/dependency map
- ✅ Architectural constraints
- ✅ Cross-references

---

## Future diagram types

(Add sections as the project adopts new diagram types — activity, BPMN, sequence, state, ERD, etc.)

### Activity diagram conventions

*(Not yet adopted. When adopting, add a sub-skill at `skills/diagram/activity/` per [`SKILL.md`](https://github.com/giakhanh22024558/MasterMind/blob/main/skills/diagram/SKILL.md) "Adding a new diagram-type sub-skill" section.)*

### BPMN conventions

*(Not yet adopted.)*

### Sequence diagram conventions

*(Not yet adopted.)*

### State diagram conventions

*(Not yet adopted.)*

### ERD conventions

*(Not yet adopted.)*

---

## Project-specific anti-patterns

Things this project particularly wants to avoid (skill should flag if it sees them):

- `<anti-pattern 1>`
- `<anti-pattern 2>`
- …

---

## Evolution log

When conventions change, record here:

| Date | Change | Rationale |
|---|---|---|
| `<YYYY-MM-DD>` | <e.g. "Adopted DFD canvas-overlay method"> | <e.g. "Vendor cross-mapping requirement"> |
| | | |
