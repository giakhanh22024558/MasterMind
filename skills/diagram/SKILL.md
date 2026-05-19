---
name: diagram
description: Build, audit, and maintain software diagrams across multiple diagram types (architecture, DFD, and future types like activity, BPMN, sequence). Modular sub-skills per diagram type · project conventions loaded from `<project-root>/diagram-conventions.md` rather than hardcoded. Use when drafting diagrams, auditing modules against specs, designing DFDs overlaid on architecture, refining edge labels, or setting up diagram conventions for a new project.
---

# Diagram skill (top-level dispatcher)

A modular toolkit for software diagrams. Each diagram type gets its own sub-skill with type-specific conventions, patterns, and scripts. Cross-cutting methodology (folder structure, design-decisions format, audit workflow, atomic edits) lives in `_shared/` and is reused across all sub-skills.

**Conventions are data, not code.** Each project specifies its own colors, IDs, edge styles, etc. in a `diagram-conventions.md` file at project root. The skill **reads** project conventions and **applies** them rather than hardcoding any specifics.

## Quick dispatch

| User asks about… | Sub-skill | Entry point |
|---|---|---|
| Master architecture (C4-style) · system landscape · zone boundaries | **architecture** | [`architecture/SKILL.md`](architecture/SKILL.md) |
| Data Flow Diagram · process triggers · data lifecycle inside a subsystem | **dfd** | [`dfd/SKILL.md`](dfd/SKILL.md) |
| Activity diagram, BPMN, sequence, state, ERD, … | *(not yet implemented)* | Add sub-skill following same pattern (see "Adding a new diagram-type sub-skill" below) |

Cross-cutting concerns (any diagram type):
| Concern | Doc |
|---|---|
| How does the skill load project conventions? | [`_shared/conventions-discovery.md`](_shared/conventions-discovery.md) |
| 4-tier folder layout for diagrams | [`_shared/folder-structure-general.md`](_shared/folder-structure-general.md) |
| Capture an architectural decision | [`_shared/design-decisions-format.md`](_shared/design-decisions-format.md) |
| Run a spec-driven audit | [`_shared/spec-driven-audit.md`](_shared/spec-driven-audit.md) |
| Defer-then-promote tracking pattern | [`_shared/defer-then-promote-pattern.md`](_shared/defer-then-promote-pattern.md) |
| Atomic edit pattern for sync-prone files | [`_shared/atomic-edits-pattern.md`](_shared/atomic-edits-pattern.md) |
| Generic edge-label principles | [`_shared/edge-labels-general.md`](_shared/edge-labels-general.md) |
| Shared scripts (cell update · cell add · revert) | [`_shared/scripts/`](_shared/scripts/) |

## Workflow for a new project

1. **Copy** [`_project-template/PROJECT-CONVENTIONS.md`](_project-template/PROJECT-CONVENTIONS.md) → `<your-project>/diagram-conventions.md`
2. **Fill in** project-specific conventions (color palette, decision-ID prefixes, spec authority codes, etc.) — fill what applies, leave defaults for the rest
3. **Choose the diagram type** you're working on → open the corresponding sub-skill's `SKILL.md`
4. The sub-skill reads `diagram-conventions.md` from your project · applies your conventions · falls back to its built-in defaults for anything not specified
5. Use [`_shared/spec-driven-audit.md`](_shared/spec-driven-audit.md) workflow when auditing modules against specs

## Workflow for an existing project that already has diagrams

1. Look for `diagram-conventions.md` at project root · if absent, infer from existing diagrams (or ask the user to confirm)
2. Open the sub-skill matching the diagram type you're adding/editing
3. Apply the project's conventions

See [`_shared/conventions-discovery.md`](_shared/conventions-discovery.md) for the discovery protocol.

## Adding a new diagram-type sub-skill

When you encounter a diagram type not yet covered (activity, BPMN, sequence, state, ERD, etc.):

1. Create `skills/diagram/<type>/` folder
2. Add `SKILL.md` describing when to use this sub-skill
3. Add `conventions-schema.md` listing what conventions a project must define for this diagram type
4. Add `conventions-defaults.md` with sensible defaults
5. Add `notation.md` (or equivalent) describing the visual vocabulary
6. Add type-specific patterns and scripts as discovered
7. Update this file's "Quick dispatch" table
8. Update `_project-template/PROJECT-CONVENTIONS.md` to add a section for the new diagram type

Each sub-skill is **self-contained** — it can reference `_shared/` but shouldn't depend on another sub-skill.

## Core principles (across all diagram types)

1. **Conventions are data** — project specifies, skill applies
2. **Spec-driven audit** — coverage tables, not opinion
3. **Defer-then-promote** — accumulate surfaces of a pattern before structural commit
4. **Atomic script-driven edits** — survive sync races, batch related changes
5. **Reference-ID + characterization** in labels — audit trail + self-explanation

## Anti-patterns

- ❌ Hardcoding a project's specifics into the skill (colors, IDs, spec codes) → loses reusability
- ❌ Forgetting to load `diagram-conventions.md` before applying defaults → may use wrong palette
- ❌ Mixing diagram-type conventions in one folder → split per type for modularity
- ❌ Adding a 5th sub-skill without updating the dispatch table here → discoverability drops
