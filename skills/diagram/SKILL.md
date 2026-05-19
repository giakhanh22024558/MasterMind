---
name: diagram
description: Build, audit, and maintain software diagrams across multiple diagram types. Modular sub-skills per diagram type (currently architecture only · DFD/activity/BPMN/sequence/state to be added as needed). Project conventions loaded from `<project-root>/diagram-conventions.md` rather than hardcoded. Use when drafting diagrams, auditing modules against specs, refining edge labels, or setting up diagram conventions for a new project.
---

# Diagram skill (top-level dispatcher)

A modular toolkit for software diagrams. Each diagram type gets its own sub-skill with type-specific conventions, patterns, scripts, and examples. Cross-cutting methodology (folder structure, design-decisions format, audit workflow, atomic edits) lives in `_shared/` and is reused across all sub-skills.

**Conventions are data, not code.** Each project specifies its own colors, IDs, edge styles in a `diagram-conventions.md` file at project root. The skill **reads** project conventions and **applies** them rather than hardcoding any specifics.

## Quick dispatch

| User asks about… | Sub-skill | Entry point |
|---|---|---|
| Master architecture (C4-style) · system landscape · zone boundaries · edges between components | **architecture** | [`architecture/SKILL.md`](architecture/SKILL.md) |
| DFD · activity · BPMN · sequence · state · ERD · … | *(not yet implemented)* | Add a new sub-skill following the **uniform folder structure** below |

Cross-cutting concerns (any diagram type):
| Concern | Doc |
|---|---|
| How does the skill load project conventions? | [`_shared/conventions-discovery.md`](_shared/conventions-discovery.md) |
| 4-tier folder layout for diagrams in a project | [`_shared/folder-structure-general.md`](_shared/folder-structure-general.md) |
| Capture an architectural decision | [`_shared/design-decisions-format.md`](_shared/design-decisions-format.md) |
| Run a spec-driven audit | [`_shared/spec-driven-audit.md`](_shared/spec-driven-audit.md) |
| Defer-then-promote tracking pattern (abstract) | [`_shared/defer-then-promote-pattern.md`](_shared/defer-then-promote-pattern.md) |
| Atomic edit pattern for sync-prone Drawio files | [`_shared/atomic-edits-pattern.md`](_shared/atomic-edits-pattern.md) |
| Generic edge-label principles | [`_shared/edge-labels-general.md`](_shared/edge-labels-general.md) |
| Shared scripts (cell update · cell add · revert) | [`_shared/scripts/`](_shared/scripts/) |

## Workflow for a new project

1. **Copy** [`_project-template/PROJECT-CONVENTIONS.md`](_project-template/PROJECT-CONVENTIONS.md) → `<your-project>/diagram-conventions.md`
2. **Fill in** project-specific conventions (color palette, decision-ID prefixes, spec authority codes) — fill what applies, leave defaults for the rest
3. **Choose the diagram type** you're working on → open the corresponding sub-skill's `SKILL.md`
4. The sub-skill reads `diagram-conventions.md` · applies your conventions · falls back to its built-in defaults for anything not specified
5. Use [`_shared/spec-driven-audit.md`](_shared/spec-driven-audit.md) when auditing modules against specs

## Uniform folder structure (mandatory for every diagram-type sub-skill)

Every sub-skill folder under `skills/diagram/<type>/` MUST follow this structure:

```
skills/diagram/<type>/
├── SKILL.md                    ← agent-facing entry point · when to use this sub-skill
├── conventions-schema.md       ← checklist of what conventions the project must define
├── conventions-defaults.md     ← sensible defaults applied when project doesn't specify
├── <type-specific docs>        ← e.g. edge-labels.md (arch), notation.md (DFD), swimlanes.md (activity)
├── patterns/                   ← type-specific reusable patterns (1+ .md files)
├── examples/                   ← worked walkthrough(s) (1+ .md files)
└── scripts/                    ← type-specific layout/edit helpers (Python templates + README.md)
```

This uniform structure means anyone navigating sub-skills knows where to look — `patterns/` always holds patterns, `scripts/` always holds scripts, etc.

## Adding a new diagram-type sub-skill

When you encounter a diagram type not yet covered (DFD, activity, BPMN, sequence, state, ERD, etc.):

### Step 1 · Create the folder

```
skills/diagram/<new-type>/
├── patterns/
├── examples/
└── scripts/
```

### Step 2 · Write the 4 required top-level docs

| File | Content |
|---|---|
| `SKILL.md` | Frontmatter (`name`, `description`) · when to use · workflow templates · anti-patterns |
| `conventions-schema.md` | Checklist of conventions a project must define for this diagram type |
| `conventions-defaults.md` | Sensible defaults applied if project doesn't specify |
| `<type-specific docs>` | One or more docs covering the type's visual vocabulary + conventions (e.g. `edge-labels.md`, `notation.md`, `swimlanes.md`) |

### Step 3 · Populate sub-folders

| Sub-folder | Initial content |
|---|---|
| `patterns/` | Start with at least one `<pattern-name>.md` (e.g. defer-then-promote instantiations specific to this diagram type) |
| `examples/` | At least one worked walkthrough using generic placeholders |
| `scripts/` | At least one type-specific helper + `README.md` listing all scripts |

### Step 4 · Update top-level files

| File | Update |
|---|---|
| Top-level `SKILL.md` (this file) | Add row to "Quick dispatch" table |
| Top-level `README.md` | Add section to "Folder layout" + adoption guide |
| `_project-template/PROJECT-CONVENTIONS.md` | Add a section for project to fill in conventions for this diagram type |

### Step 5 · Validate

- All 4 required top-level docs present
- All 3 sub-folders present (even if `examples/` and `scripts/` initially hold only a README or placeholder)
- Sub-skill is self-contained (references `_shared/` allowed, references to other sub-skills allowed but should be rare)

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
- ❌ Adding a sub-skill without updating top-level dispatch + project template → discoverability drops
