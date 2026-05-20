# Example · how the `diagram` skill applies the meta-patterns

Walks through the `diagram` skill, showing how each of the 4 core meta-patterns is instantiated. Use as a reference when creating a new skill.

> **Where it lives:** the `diagram` skill is split across the two-folder layout. The **framework** is in [`core/diagram/`](../../../diagram/) (invariant across projects). The concrete **architecture** sub-skill lives in a model at `models/model_001/diagram/architecture/`.

## The 4 patterns in `diagram`

### Pattern 1 · Uniform skill structure

`diagram` is a **Shape B (multi-domain category)** skill — it covers architecture, with future DFD/activity/BPMN to be added. The framework and the concrete sub-skills sit in different places:

```
core/diagram/                                      ← framework (invariant)
├── SKILL.md                                       unversioned dispatcher
├── README.md                                      unversioned overview
├── VERSIONING.md                                  unversioned (diagram-specific versioning doc)
├── _shared/                                       cross-sub-skill methodology
│   ├── conventions-discovery/v1/                  versioned
│   ├── folder-structure-general/v1/               versioned
│   ├── design-decisions-format/v1/                versioned
│   ├── spec-driven-audit/v1/                      versioned
│   ├── defer-then-promote-pattern/v1/             versioned
│   ├── atomic-edits-pattern/v1/                   versioned
│   ├── edge-labels-general/v1/                    versioned
│   └── scripts/v1/                                versioned (generic scripts)
└── _project-template/v1/                          starter for adopting projects
    └── PROJECT-CONVENTIONS.md

models/model_001/diagram/architecture/             ← concrete sub-skill (Shape A inside)
├── SKILL.md                                       unversioned entry point
├── conventions-schema/v1/                         versioned
├── conventions-defaults/v1/                       versioned
├── edge-labels/v1/                                versioned (type-specific docs)
├── patterns/v1/                                   versioned (3 patterns)
├── examples/v1/                                   versioned
└── scripts/v1/                                    versioned (4 scripts + README)
```

The concrete sub-skill follows the uniform Shape A structure. The dispatcher (`core/diagram/SKILL.md`) routes user requests to the appropriate sub-skill.

### Pattern 2 · Per-leaf-folder versioning

Every content module in `diagram` lives in a `vN/` subfolder:

| Module | Path |
|---|---|
| Architecture patterns | `models/model_001/diagram/architecture/patterns/v1/...` |
| Architecture scripts | `models/model_001/diagram/architecture/scripts/v1/...` |
| Architecture conventions schema | `models/model_001/diagram/architecture/conventions-schema/v1/conventions-schema.md` |
| Shared atomic-edits | `core/diagram/_shared/atomic-edits-pattern/v1/atomic-edits-pattern.md` |
| Shared scripts | `core/diagram/_shared/scripts/v1/...` |
| Project template | `core/diagram/_project-template/v1/PROJECT-CONVENTIONS.md` |

When `architecture/scripts/` evolves to v2:
- Copy `v1/` → `v2/`
- Modify v2 only
- Add `architecture/scripts/CHANGELOG.md`
- `v1/` stays untouched
- Consumers' cross-references to `architecture/scripts/` auto-resolve to latest (v2)
- Consumers needing v1 stability pin to `architecture/scripts/v1/`

### Pattern 3 · Conventions as data

Project side: each adopting project provides `<project-root>/diagram-conventions.md` (template at [`core/diagram/_project-template/v1/`](../../../diagram/_project-template/v1/PROJECT-CONVENTIONS.md)).

This file specifies:

- Color palette per zone semantic (matching the project's brand or domain convention)
- Decision-ID prefix scheme (e.g. `M0a-M0Z` for mobile, `S<n>` for system)
- Spec authority code format
- Edge granularity policy
- Layout conventions

Skill side: `core/diagram/_shared/conventions-discovery/v1/conventions-discovery.md` defines the protocol — look for the project file → fall back to the sub-skill's `conventions-defaults/v1/` for unspecified items → ask the user when ambiguous.

**Skill content has zero hardcoded project specifics.** All examples in `patterns/`, `examples/`, `scripts/` use placeholders (`LAYER_A`, `<decision-id>`, `<spec-id>`).

### Pattern 4 · Defer-then-promote

`diagram` instantiates the abstract defer-then-promote pattern (from [`defer-then-promote-pattern/`](../../defer-then-promote-pattern/)) in two domain-specific tracking patterns:

- **Cross-Layer Reads (CLR)** — App Layer reading Survival Core data via "limited surfaces"
  - ID prefix: `CLR-XX`
  - Threshold: 3 confirmed surfaces
  - Resolution options: α direct edge / β cross-layer read / γ skip
  - Doc: `models/model_001/diagram/architecture/patterns/v1/cross-layer-reads-tracking.md`

- **Hardware Access Gaps (HWG)** — features needing hardware not modeled in architecture
  - ID prefix: `HWG-XX`
  - Threshold: per-gap resolution (no count threshold)
  - Resolution options: α direct OS access / β cross-layer read from publisher / γ skip
  - Doc: `models/model_001/diagram/architecture/patterns/v1/hardware-gaps-tracking.md`

Both follow the lifecycle: discover → log locally → threshold check → promote to canonical doc + architecture edge.

### Pattern 5 (when applicable) · Atomic edits

`diagram` heavily uses atomic edits because Drawio `.drawio` files are typically synced via Google Drive / OneDrive.

Implementation:
- `core/diagram/_shared/atomic-edits-pattern/v1/atomic-edits-pattern.md` — narrative
- `core/diagram/_shared/scripts/v1/` — reusable templates (add-cell.py, update-cell-value.py, revert-edges.py)
- `models/model_001/diagram/architecture/scripts/v1/` — architecture-specific layout helpers + edge insertion

Each per-edit script in a project's `.scripts/` folder is derived from these templates.

## How a new skill would mirror this

If creating a new skill, apply the same patterns:

### Shape decision

If the skill covers multiple types (e.g. requirements analysis · stakeholder mapping · process modeling), use Shape B — a framework in `core/` plus concrete sub-skills in `models/`. Otherwise Shape A — a single concrete skill in `models/model_NNN/<category>/<skill>/`.

### Folder structure

Apply the uniform layout (see [`uniform-skill-structure/`](../../uniform-skill-structure/v1/uniform-skill-structure.md)). Same sub-folder names, same versioning.

### Conventions-as-data

- `<skill>/conventions-schema/v1/` — checklist of what projects should specify
- `<skill>/conventions-defaults/v1/` — sensible defaults
- Projects provide `<project>/<skill>-conventions.md`

### Defer-then-promote (if applicable)

If the skill discovers recurring concerns, define a tracking pattern:

- `<skill>/patterns/v1/<tracking-name>.md` — references the meta-pattern + domain specifics

### Atomic edits (if applicable)

If the skill manipulates `.docx`, `.xlsx`, `.drawio`, or other sync-prone files, build templates in `<skill>/scripts/v1/`.

## Lessons learned from building `diagram`

| Lesson | What we did right | What we'd change |
|---|---|---|
| Folder shape | Uniform structure adopted early | Should have been uniform from day one (originally was flat, refactored later) |
| Versioning | Per-leaf-folder grain works well | Could have been done from the start instead of mid-development |
| Sub-skill split | Made adding new diagram types trivial | First version mixed architecture + DFD in one folder |
| Patterns abstraction | CLR/HWG defer-then-promote codified | Pattern templates should have been more general from the start (refactored into `core/meta/`) |
| Atomic edits | Saved many sync-race headaches | Better idempotency checks needed in some scripts |
| core/models split | Framework and concrete sub-skills cleanly separated | — |

## See also

- [`skill-creation-guide/`](../../skill-creation-guide/v1/skill-creation-guide.md) — step-by-step process
- [`uniform-skill-structure/`](../../uniform-skill-structure/v1/uniform-skill-structure.md) — folder shape mandate
- [`versioning-pattern/`](../../versioning-pattern/v1/versioning-pattern.md) — versioning model
- [`conventions-as-data-pattern/`](../../conventions-as-data-pattern/v1/conventions-as-data-pattern.md) — conventions-as-data principle
