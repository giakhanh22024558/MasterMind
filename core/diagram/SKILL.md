---
name: diagram
description: Build, audit, and maintain software diagrams across multiple diagram types. Modular sub-skills per diagram type (currently architecture only · DFD/activity/BPMN/sequence/state to be added as needed). Project conventions loaded from `<project-root>/diagram-conventions.md` rather than hardcoded. Use when drafting diagrams, auditing modules against specs, refining edge labels, or setting up diagram conventions for a new project.
---

# Diagram skill (top-level dispatcher)

A modular toolkit for software diagrams. Each diagram type gets its own sub-skill. Cross-cutting methodology lives in `_shared/`.

**Conventions are data, not code.** Each project specifies its own colors, IDs, edge styles in a `diagram-conventions.md` file at project root. The skill **reads** project conventions and **applies** them rather than hardcoding any specifics.

## Quick dispatch

`core/diagram/` holds the **shared diagram framework** — cross-cutting methodology (`_shared/`) and the project-conventions template. **Concrete diagram sub-skills live inside a model** at `models/model_NNN/diagram/<type>/`.

| User asks about… | Sub-skill | Entry point |
|---|---|---|
| Master architecture (C4-style) · system landscape · zone boundaries · edges between components | **architecture** | [`models/model_001/diagram/architecture/SKILL.md`](../../models/model_001/diagram/architecture/SKILL.md) |
| DFD · activity · BPMN · sequence · state · ERD · … | *(not yet implemented)* | Add a new sub-skill following the **uniform folder structure** below |

Cross-cutting concerns (any diagram type):

| Concern | Folder |
|---|---|
| How does the skill load project conventions? | [`_shared/conventions-discovery/`](_shared/conventions-discovery/) |
| 4-tier folder layout for diagrams in a project | [`_shared/folder-structure-general/`](_shared/folder-structure-general/) |
| Capture an architectural decision | [`_shared/design-decisions-format/`](_shared/design-decisions-format/) |
| Run a spec-driven audit | [`_shared/spec-driven-audit/`](_shared/spec-driven-audit/) |
| Defer-then-promote tracking pattern (abstract) | [`_shared/defer-then-promote-pattern/`](_shared/defer-then-promote-pattern/) |
| Atomic edit pattern for sync-prone Drawio files | [`_shared/atomic-edits-pattern/`](_shared/atomic-edits-pattern/) |
| Generic edge-label principles | [`_shared/edge-labels-general/`](_shared/edge-labels-general/) |
| Shared scripts (cell update · cell add · revert) | [`_shared/scripts/`](_shared/scripts/) |

## Workflow for a new project

1. **Copy** [`_project-template/`](_project-template/) PROJECT-CONVENTIONS.md → `<your-project>/diagram-conventions.md`
2. **Fill in** project-specific conventions (color palette, decision-ID prefixes, spec authority codes) — fill what applies, leave defaults for the rest
3. **Choose the diagram type** you're working on → open the corresponding sub-skill's `SKILL.md`
4. The sub-skill reads `diagram-conventions.md` and applies your conventions
5. Use [`_shared/spec-driven-audit/`](_shared/spec-driven-audit/) when auditing modules against specs

## Uniform folder structure (mandatory for every diagram-type sub-skill)

Every sub-skill folder under `models/model_NNN/diagram/<type>/` MUST follow this structure:

```
models/model_NNN/diagram/<type>/
├── SKILL.md                              ← agent-facing entry point
├── conventions-schema/
│   └── conventions-schema.md
├── conventions-defaults/
│   └── conventions-defaults.md
├── <type-specific>/                      ← e.g. edge-labels/, notation/, swimlanes/
├── patterns/                             ← reusable patterns
├── examples/                             ← worked walkthroughs
└── scripts/                              ← helper scripts
```

## Adding a new diagram-type sub-skill

When you encounter a diagram type not yet covered (DFD, activity, BPMN, sequence, state, ERD, etc.):

### Step 1 · Create the folder + sub-folders

```
models/model_NNN/diagram/<new-type>/
├── conventions-schema/
├── conventions-defaults/
├── <type-specific>/                   ← e.g. notation/
├── patterns/
├── examples/
└── scripts/
```

### Step 2 · Write the `SKILL.md`

Frontmatter (`name`, `description`) · when to use · workflow templates · links to content modules · anti-patterns.

### Step 3 · Write each module's content

| Module | Content |
|---|---|
| `conventions-schema/<schema>.md` | Checklist of conventions a project must define for this diagram type |
| `conventions-defaults/<defaults>.md` | Sensible defaults applied if project doesn't specify |
| `<type-specific>/<doc>.md` | Visual vocabulary + conventions (one or more docs) |
| `patterns/*.md` | At least one reusable pattern |
| `examples/*.md` | At least one worked walkthrough |
| `scripts/*.py` + `README.md` | At least one type-specific helper |

### Step 4 · Update top-level files

| File | Update |
|---|---|
| Top-level `SKILL.md` (this file) | Add row to "Quick dispatch" table |
| Top-level `README.md` | Add section to "Folder layout" + adoption guide |
| `_project-template/PROJECT-CONVENTIONS.md` | Add a section for project to fill in conventions for this diagram type |

### Step 5 · Validate

- All required sub-folders present
- Sub-skill `SKILL.md` exists and links to the content modules
- Sub-skill is self-contained (references `_shared/` allowed)

## Core principles (across all diagram types)

1. **Conventions are data** — project specifies, skill applies
2. **Spec-driven audit** — coverage tables, not opinion
3. **Defer-then-promote** — accumulate surfaces of a pattern before structural commit
4. **Atomic script-driven edits** — survive sync races, batch related changes
5. **Reference-ID + characterization** in labels — audit trail + self-explanation
6. **Uniform folder structure** — every diagram-type sub-skill has the same shape

## Anti-patterns

- ❌ Hardcoding a project's specifics into the skill (colors, IDs, spec codes) → loses reusability
- ❌ Forgetting to load `diagram-conventions.md` before applying defaults → may use wrong palette
- ❌ Mixing diagram-type conventions in one folder → split per type for modularity
- ❌ Adding a new sub-skill with a different folder structure → breaks navigability
