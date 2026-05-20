# Example · how the `diagram` skill applies the meta-patterns

Walks through the `diagram` skill, showing how each core meta-pattern is instantiated. Use as a reference when creating a new skill.

> **Where it lives:** the `diagram` skill is split across the two-folder layout. The **framework** is in [`core/diagram/`](../../diagram/) (invariant across projects). The concrete **architecture** sub-skill lives in a model at `models/model_001/diagram/architecture/`.

## The patterns in `diagram`

### Pattern 1 · Uniform skill structure

`diagram` is a **Shape B (multi-domain category)** skill — it covers architecture, with future DFD/activity/BPMN to be added. The framework and the concrete sub-skills sit in different places:

```
core/diagram/                                      ← framework (invariant)
├── SKILL.md                                       dispatcher
├── README.md                                      overview
├── _shared/                                       cross-sub-skill methodology
│   ├── conventions-discovery/
│   ├── folder-structure-general/
│   ├── design-decisions-format/
│   ├── spec-driven-audit/
│   ├── defer-then-promote-pattern/
│   ├── atomic-edits-pattern/
│   ├── edge-labels-general/
│   └── scripts/                                   generic scripts
└── _project-template/
    └── PROJECT-CONVENTIONS.md

models/model_001/diagram/architecture/             ← concrete sub-skill (Shape A inside)
├── SKILL.md                                       entry point
├── conventions-schema/
├── conventions-defaults/
├── edge-labels/                                   type-specific docs
├── patterns/                                      3 patterns
├── examples/
└── scripts/                                       4 scripts + README
```

The concrete sub-skill follows the uniform Shape A structure. The dispatcher (`core/diagram/SKILL.md`) routes user requests to the appropriate sub-skill.

### Pattern 2 · Conventions as data

Project side: each adopting project provides `<project-root>/diagram-conventions.md` (template at [`core/diagram/_project-template/`](../../diagram/_project-template/PROJECT-CONVENTIONS.md)).

This file specifies:

- Color palette per zone semantic (matching the project's brand or domain convention)
- Decision-ID prefix scheme (e.g. `M0a-M0Z` for mobile, `S<n>` for system)
- Spec authority code format
- Edge granularity policy
- Layout conventions

Skill side: `core/diagram/_shared/conventions-discovery/conventions-discovery.md` defines the protocol — look for the project file → fall back to the sub-skill's `conventions-defaults/` for unspecified items → ask the user when ambiguous.

**Skill content has zero hardcoded project specifics.** All examples in `patterns/`, `examples/`, `scripts/` use placeholders (`LAYER_A`, `<decision-id>`, `<spec-id>`).

### Pattern 3 · Defer-then-promote

`diagram` instantiates the abstract defer-then-promote pattern (from [`defer-then-promote-pattern/`](../defer-then-promote-pattern/)) in two domain-specific tracking patterns:

- **Cross-Layer Reads (CLR)** — App Layer reading Survival Core data via "limited surfaces"
  - ID prefix: `CLR-XX`
  - Threshold: 3 confirmed surfaces
  - Resolution options: α direct edge / β cross-layer read / γ skip
  - Doc: `models/model_001/diagram/architecture/patterns/cross-layer-reads-tracking.md`

- **Hardware Access Gaps (HWG)** — features needing hardware not modeled in architecture
  - ID prefix: `HWG-XX`
  - Threshold: per-gap resolution (no count threshold)
  - Resolution options: α direct OS access / β cross-layer read from publisher / γ skip
  - Doc: `models/model_001/diagram/architecture/patterns/hardware-gaps-tracking.md`

Both follow the lifecycle: discover → log locally → threshold check → promote to canonical doc + architecture edge.

### Pattern 4 (when applicable) · Atomic edits

`diagram` heavily uses atomic edits because Drawio `.drawio` files are typically synced via Google Drive / OneDrive.

Implementation:
- `core/diagram/_shared/atomic-edits-pattern/atomic-edits-pattern.md` — narrative
- `core/diagram/_shared/scripts/` — reusable templates (add-cell.py, update-cell-value.py, revert-edges.py)
- `models/model_001/diagram/architecture/scripts/` — architecture-specific layout helpers + edge insertion

Each per-edit script in a project's `.scripts/` folder is derived from these templates.

## How a new skill would mirror this

If creating a new skill, apply the same patterns:

### Shape decision

If the skill covers multiple types (e.g. requirements analysis · stakeholder mapping · process modeling), use Shape B — a framework in `core/` plus concrete sub-skills in `models/`. Otherwise Shape A — a single concrete skill in `models/model_NNN/<category>/<skill>/`.

### Folder structure

Apply the uniform layout (see [`uniform-skill-structure/`](../uniform-skill-structure/uniform-skill-structure.md)). Same sub-folder names throughout.

### Conventions-as-data

- `<skill>/conventions-schema/` — checklist of what projects should specify
- `<skill>/conventions-defaults/` — sensible defaults
- Projects provide `<project>/<skill>-conventions.md`

### Defer-then-promote (if applicable)

If the skill discovers recurring concerns, define a tracking pattern:

- `<skill>/patterns/<tracking-name>.md` — references the meta-pattern + domain specifics

### Atomic edits (if applicable)

If the skill manipulates `.docx`, `.xlsx`, `.drawio`, or other sync-prone files, build templates in `<skill>/scripts/`.

## Lessons learned from building `diagram`

| Lesson | What we did right | What we'd change |
|---|---|---|
| Folder shape | Uniform structure adopted early | Should have been uniform from day one (originally was flat, refactored later) |
| Sub-skill split | Made adding new diagram types trivial | First version mixed architecture + DFD in one folder |
| Patterns abstraction | CLR/HWG defer-then-promote codified | Pattern templates should have been more general from the start (refactored into `core/meta/`) |
| Atomic edits | Saved many sync-race headaches | Better idempotency checks needed in some scripts |
| core/models split | Framework and concrete sub-skills cleanly separated | — |

## See also

- [`skill-creation-guide/`](../skill-creation-guide/skill-creation-guide.md) — step-by-step process
- [`uniform-skill-structure/`](../uniform-skill-structure/uniform-skill-structure.md) — folder shape mandate
- [`conventions-as-data-pattern/`](../conventions-as-data-pattern/conventions-as-data-pattern.md) — conventions-as-data principle
