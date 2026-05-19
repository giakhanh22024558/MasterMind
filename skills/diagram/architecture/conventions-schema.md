# Architecture diagram · conventions schema

The full list of conventions an architecture diagram needs. Use this as a **checklist** when reading a project's `diagram-conventions.md` or asking the user to fill in defaults.

For each item, the project should specify a value or explicitly accept the default from [`conventions-defaults.md`](conventions-defaults.md).

## 1 · Zone color palette

For each zone semantic the project uses, define the fill + stroke colors.

Zones encountered in software architecture (project picks which apply):

- Device / hardware / sensor input
- Safety-critical / offline core / kernel
- Client app — UI / Experience layer
- Client app — sub-layer (e.g. comms · features)
- Local persistence (on-device storage)
- Cloud backend (compute + DB)
- Cloud backend nested sub-groups
- Web admin / operations console
- Web admin nested sub-groups
- Sync engine / cloud DB / message bus
- External providers / 3rd-party APIs
- Public-facing site / CMS

Project should provide:

| Zone purpose | Fill (project) | Stroke (project) |
|---|---|---|
| <e.g. Client app · UI layer> | `#bbdefb` | `#0277bd` |
| … | … | … |

If unspecified, [`conventions-defaults.md`](conventions-defaults.md) palette applies.

## 2 · Component box default style

For non-container component cells (the white boxes inside zone containers):

- Fill color (default: white `#ffffff`)
- Stroke color (default: grey `#555`)
- Stroke width (default: 1px)
- Text color (default: black `#000`)
- Shape (default: rounded rectangle · cylinder for stores)

## 3 · Special node variants

Project should define styles for:

- **Constraint / warning banner**
- **Compliance / prohibition callout**
- **Inert scaffold / future-phase placeholder** (e.g. Phase 2 features in inert state)
- **Provisional cell** (preemptive structural commit pending confirmation)
- **Separation boundary marker** (e.g. between two layers with strict isolation)
- **Database / datastore** — cylinder shape · color varies by tech

## 4 · Edge styles

For each edge type the project uses:

- **Solid operational edge** — color, stroke width
- **Dashed conditional / optional edge**
- **Dotted purple data-payload edge** (stroke-dasharray, color)
- **Red dashed prohibited edge**
- **Orange dashed consent-gated / conditional edge**
- **Exception-flag styling** (when an otherwise-normal edge needs a warning)

## 5 · Edge label conventions

- **Verb form** rule for operational edges (default: enforced)
- **Noun form** rule for data-payload edges (default: enforced)
- **Reference-ID + characterization** format for citing authority sources (default: `(<ID> <characterization>)`)
- **Prohibition label format** (default: `[X] PROHIBITED <reason> (<authority>)`)

## 6 · Naming conventions

- **Component ID prefix scheme** (e.g. `MOD-1234` · `SVC-name-version` · etc.)
- **Decision-ID prefix scheme** (e.g. `M0a–M0Z` for mobile, `S<n>` for system, `O<n>` for ops, `V<n>` for visual)
- **Spec authority code format** (e.g. `<PROJECT>-<DOMAIN>-NNNN`)
- **Rejection trigger format** (e.g. `RT-NN`)
- **Cross-cutting concern naming** (e.g. `compliance-matrix.md`, `performance-targets.md`)

## 7 · Edge granularity policy

- **Default granularity** (default: layer ↔ layer / sub-group ↔ sub-group)
- **Storage exception** (default: enabled — see [`patterns/storage-exception.md`](patterns/storage-exception.md))
- **Other exceptions** (project-specific · capture in design-decisions row)

## 8 · Same-level visual consistency rule

- Default: enforced — components at the same hierarchy level share identical styling
- Project may relax or strengthen

## 9 · Layout conventions

- **Mermaid layout engine** (default: `elk` for clean orthogonal routing)
- **Diagram direction** (`graph LR` vs `graph TB`)
- **Inter-layer gap** (default: 60px)
- **Component width** (default: 165px for standard rows · varies for stores)
- **Page width** (project-specific based on layer count)

## 10 · Cross-cutting docs the project maintains

List the cross-cutting concern docs the project keeps (typical):

- `compliance-matrix.md` — all prohibitions + enforcement
- `performance-targets.md` — all numeric SLAs
- `<artifact>-lifecycle.md` — single-artifact journey across subsystems

Project may add more (e.g. `cross-layer-reads.md` when CLR pattern promotes per `patterns/cross-layer-reads-tracking.md`).

## 11 · Sub-skill exceptions / overrides

If the project deviates from a sub-skill recommended pattern (e.g. doesn't use storage exception · doesn't use V4 hybrid), document the deviation here with rationale.

## 12 · Anti-patterns to enforce

Project should list its top anti-patterns the skill should flag, e.g.:

- Smooth bezier curves (force `curve: linear` or ELK)
- Colorful inner boxes (keep inner components white)
- Single-word labels
- Crossing edges through unrelated zones
- Emoji-heavy inner nodes

## Checklist (for skill agent)

When loading a project's `diagram-conventions.md` for the first time:

- [ ] Zone color palette resolved (project or defaults)
- [ ] Edge styles resolved
- [ ] Naming conventions captured
- [ ] Edge granularity policy clear
- [ ] Cross-cutting docs identified
- [ ] Any explicit deviations noted

If any item is ambiguous or undefined, **ask the user** before proceeding rather than silently assuming.
