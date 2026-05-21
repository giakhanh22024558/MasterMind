# core/diagram — diagram-skill framework

The **invariant** part of the diagram skill: shared methodology (`_shared/`) and the project-conventions template. **Concrete diagram skills** (architecture, dfd...) live inside each model at `models/model_NNN/diagram/<type>/`.

## Layout

```
core/diagram/
├── SKILL.md            ← dispatcher
├── README.md           ← this file
├── _shared/            ← methodology shared across all diagram types
│   ├── conventions-discovery/
│   ├── folder-structure-general/
│   ├── design-decisions-format/
│   ├── spec-driven-audit/
│   ├── defer-then-promote-pattern/
│   ├── atomic-edits-pattern/
│   ├── edge-labels-general/
│   └── scripts/
└── _project-template/   ← PROJECT-CONVENTIONS.md template
```

## Concrete diagram skills

| Model | Sub-skill | Location |
|---|---|---|
| model_001 | architecture | [`models/model_001/diagram/architecture/`](../../models/model_001/diagram/architecture/) |
| model_001 | erd | [`models/model_001/diagram/erd/`](../../models/model_001/diagram/erd/) |

## Creating a new diagram sub-skill

Create `models/model_NNN/diagram/<type>/` following the uniform structure — see [`SKILL.md`](SKILL.md), section "Adding a new diagram-type sub-skill". A sub-skill references back to `core/diagram/_shared/` for shared methodology.

## Principles

- **Conventions are data** — a project declares them in `<project>/diagram-conventions.md`; the skill reads & applies.
- Follows the [Core Rule](../core-rule/) — `.drawio` is the user layer, `.md` / Mermaid is the agent layer.

## Stack

Mermaid (text-based diagrams) · Drawio `.drawio` XML · Python scripts (atomic edits) · Markdown (narrative).
