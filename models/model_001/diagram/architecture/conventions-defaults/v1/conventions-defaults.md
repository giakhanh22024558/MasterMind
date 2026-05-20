# Architecture diagram · conventions defaults

Default conventions applied by the architecture sub-skill when a project hasn't specified its own. **Project conventions** in `<project-root>/diagram-conventions.md` always override these defaults — see [`conventions-discovery`](../../../../../../core/diagram/_shared/conventions-discovery/) for the discovery protocol.

These defaults are sensible starting points · projects are free to redefine any of them.

## Mermaid header

```
---
config:
  layout: elk
  theme: base
  themeVariables:
    fontFamily: Arial
    fontSize: 13px
---
graph LR        # or TB depending on dominant axis
```

- Always use `layout: elk` for clean orthogonal routing
- `graph LR` when 2–3 major zones sit side-by-side
- `graph TB` when hierarchy is strictly top-down

## Macro layout

- Wrap the diagram in **2–4 large outer subgraphs** acting as colored "zones"
- Inside each zone, place **white inner boxes** (individual components)
- Use a **dashed marker node** (e.g. `{{"- - - - - BOUNDARY - - - - -"}}`) to visualize architectural separations between zones

## Color palette (by zone semantic)

Pick a color per architectural role. Apply consistently across the project. Suggested mapping:

| Zone purpose | Fill | Stroke |
|---|---|---|
| Device / hardware / sensor input | `#e3f2fd` (light blue) | `#1976d2` |
| Safety-critical / offline core / kernel | `#c8e6c9` or `#e8f5e9` (green) | `#2e7d32` |
| Client app — Experience / UI layer | `#bbdefb` (light blue) | `#0277bd` |
| Client app — sub-layer | `#e3f2fd` (lighter blue) | `#1976d2` |
| Local persistence (on-device storage) | `#f3e5f5` (lavender) | `#6a1b9a` |
| Cloud backend / compute + DB | `#d1c4e9` (light purple) | `#5e35b2` |
| Cloud backend nested sub-groups | `#ede7f6` (lighter purple) | `#5e35b2` |
| Web admin / operations console | `#b2dfdb` (teal) | `#00695c` |
| Web admin nested sub-groups | `#e0f2f1` (lighter teal) | `#00695c` |
| Sync engine / cloud DB / message bus | `#fff9c4` (light yellow) | `#f9a825` |
| External providers / 3rd-party APIs | `#ffe0b2` or `#fff3e0` (peach) | `#e65100` |
| Public-facing site / CMS | `#f5f5dc` (beige) | `#827717` |
| Data persistence — cloud cache | `#e1f5ff` | `#0277bd` |
| Data persistence — core local (dashed border) | `#f3e5f5` lavender | `#6a1b9a` |

You're free to swap colors as long as you apply consistently. The semantic role (what each color means in your project) should be documented in your project's `CLAUDE.md` or visual style guide.

## Tech-stack notes (mandatory per zone)

Each zone subgraph title MUST include a one-line tech stack note in italics:

```
<b>ZONE NAME</b><br/><i>Tech: stack details · constraints</i>
```

Examples (replace with your stack):
- `<b>CLIENT APP</b><br/><i>Tech: React Native · iOS / Android · offline-first</i>`
- `<b>OPERATIONS CONSOLE</b><br/><i>Tech: React · OIDC · RBAC</i>`
- `<b>CLOUD BACKEND</b><br/><i>Tech: AWS / GCP · Kubernetes</i>`

## Component boxes (inner nodes)

- **Default style:** white fill `#ffffff`, grey stroke `#555`, 1px width, black text `#000`
- **Bold header** on first line via `<b>...</b>`, then bulleted body lines with `<br/>- item`
- Keep boxes **text-only** — no emoji icons inside inner boxes
- Multi-line content preferred — pack 3–6 bullets per box

### Special node variants

| Variant | Style |
|---|---|
| Constraint / warning banner | `fill:#ffebee, stroke:#c62828, color:#b71c1c` |
| Compliance / prohibition callout | `fill:#fff5f5, stroke:#c62828, color:#b71c1c` |
| Inert scaffold / future-phase placeholder | `fill:#fafafa, stroke:#9e9e9e, stroke-dasharray:5 5, color:#616161` |
| **Provisional cell** (preemptive commit, pending confirmation) | `fill:#fff8e1, stroke:#f57c00, stroke-dasharray:6 3, color:#e65100` + warning badge in label |
| Separation boundary marker | hexagon shape `{{...}}`, `stroke-dasharray:6 4, color:#000` |
| Database / datastore | cylinder `[(...)]`, purple if local/core, blue if cloud |

## Edges

- **Solid arrow** `-->` = operational / control / runtime dependency
- **Dashed arrow** `-.->` = optional / conditional / metrics / surfacing
- **Dotted purple** `-.->` with `stroke-dasharray:2 3` = data payload / data-flow
  - Style via `linkStyle <idx> stroke:#6a1b9a,stroke-width:2px,stroke-dasharray:2 3`
- **Red dashed prohibited** `-.->` with `stroke:#c62828,stroke-width:2px,stroke-dasharray:5 5` labeled `<b>[X] PROHIBITED</b><br/>(reason)`
- **Orange dashed conditional** `-.->` with `stroke:#f57c00,stroke-dasharray:5 3` = consent-gated / user-optional / opt-in
- **Always label edges** with protocol, payload, or semantic
- Use `<br/>` for multi-line edge labels

### Exception-flag styling

When a data-flow edge represents an architectural exception (e.g. a normally-prohibited path allowed under specific conditions), keep the base style (purple dotted for data) but **change font color to red** (`color:#c62828` / `fontColor=#c62828` in Drawio) to flag the exception while preserving the data-flow visual identity.

In Mermaid, wrap label in `<font color='#c62828'>...</font>` AND add `linkStyle <idx> color:#c62828` for redundancy (renderers vary in `<font>` tag support).

## Subgraph titles

- All caps + bold for top-level zones
- Add a tagline as a second line if there's a defining constraint
- Title case + bold for nested subgraphs

## Mandatory inclusions

- **Legend node** explaining arrow semantics and prohibited markers
- **Standards / spec references** in box headers when applicable
- **Performance / compliance callouts** as red-styled boxes adjacent to the relevant zone, NOT embedded inside it

## Same-level visual consistency (mandatory)

- Components at the same hierarchy level MUST share identical styling
- If one sibling is a subgraph container, every sibling at the same level should also be a subgraph (even if it contains only one descriptive node)
- This trumps content-density differences — visual peer recognition matters more than minimizing nesting depth

## Anti-patterns

- Smooth bezier curves — always force `curve: linear` or ELK
- Colorful inner boxes — keep inner components white, let zone color do the work
- Single-word labels — every box should have bold title + context bullets
- Crossing edges through unrelated zones when a side-route exists
- Emoji-heavy inner nodes (reference style is text-first)
