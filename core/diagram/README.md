# core/diagram — diagram-skill framework

The **invariant** part of the diagram skill: shared methodology (`_shared/`), the versioning model, and the project-conventions template. **Concrete diagram skills** (architecture, dfd...) live inside each model at `models/model_NNN/diagram/<type>/`.

## Layout

```
core/diagram/
├── SKILL.md            ← dispatcher (unversioned)
├── README.md           ← this file
├── VERSIONING.md       ← versioning model
├── _shared/            ← methodology shared across all diagram types
│   ├── conventions-discovery/v1/
│   ├── folder-structure-general/v1/
│   ├── design-decisions-format/v1/
│   ├── spec-driven-audit/v1/
│   ├── defer-then-promote-pattern/v1/
│   ├── atomic-edits-pattern/v1/
│   ├── edge-labels-general/v1/
│   └── scripts/v1/
└── _project-template/v1/   ← PROJECT-CONVENTIONS.md template
```

## Concrete diagram skills

| Model | Sub-skill | Location |
|---|---|---|
| model_001 | architecture | [`models/model_001/diagram/architecture/`](../../models/model_001/diagram/architecture/) |

## Creating a new diagram sub-skill

Create `models/model_NNN/diagram/<type>/` following the uniform structure — see [`SKILL.md`](SKILL.md), section "Adding a new diagram-type sub-skill". A sub-skill references back to `core/diagram/_shared/` for shared methodology.

## Principles

- **Conventions are data** — a project declares them in `<project>/diagram-conventions.md`; the skill reads & applies.
- **Versioning at leaf-folder grain** — see [`VERSIONING.md`](VERSIONING.md).
- Follows the [Core Rule](../core-rule/) — `.drawio` is the user layer, `.md` / Mermaid is the agent layer.

## Stack

Mermaid (text-based diagrams) · Drawio `.drawio` XML · Python scripts (atomic edits) · Markdown (narrative).
