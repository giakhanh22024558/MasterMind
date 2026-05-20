---
name: diagram
description: Build, audit, and maintain software diagrams across multiple diagram types. Modular sub-skills per diagram type (currently architecture only · DFD/activity/BPMN/sequence/state to be added as needed). Project conventions loaded from `<project-root>/diagram-conventions.md` rather than hardcoded. Every content module is versioned at leaf-folder grain · default = latest. Use when drafting diagrams, auditing modules against specs, refining edge labels, or setting up diagram conventions for a new project.
---

# Diagram skill (top-level dispatcher)

A modular, versioned toolkit for software diagrams. Each diagram type gets its own sub-skill. Cross-cutting methodology lives in `_shared/`. **Every content module is versioned** at the leaf-folder grain — default behavior is to use the latest version unless explicitly pinned.

**Conventions are data, not code.** Each project specifies its own colors, IDs, edge styles in a `diagram-conventions.md` file at project root. The skill **reads** project conventions and **applies** them rather than hardcoding any specifics.

## Quick dispatch

`core/diagram/` holds the **shared diagram framework** — cross-cutting methodology (`_shared/`), the versioning model, and the project-conventions template. **Concrete diagram sub-skills live inside a model** at `models/model_NNN/diagram/<type>/`.

| User asks about… | Sub-skill | Entry point (unversioned) |
|---|---|---|
| Master architecture (C4-style) · system landscape · zone boundaries · edges between components | **architecture** | [`models/model_001/diagram/architecture/SKILL.md`](../../models/model_001/diagram/architecture/SKILL.md) |
| DFD · activity · BPMN · sequence · state · ERD · … | *(not yet implemented)* | Add a new sub-skill following the **uniform folder structure** below |

Cross-cutting concerns (any diagram type) — all content modules are versioned at the leaf-folder grain:

| Concern | Leaf folder (latest version applied by default) |
|---|---|
| Versioning model — how versions work | [`VERSIONING.md`](VERSIONING.md) (unversioned · always current) |
| How does the skill load project conventions? | [`_shared/conventions-discovery/`](_shared/conventions-discovery/) |
| 4-tier folder layout for diagrams in a project | [`_shared/folder-structure-general/`](_shared/folder-structure-general/) |
| Capture an architectural decision | [`_shared/design-decisions-format/`](_shared/design-decisions-format/) |
| Run a spec-driven audit | [`_shared/spec-driven-audit/`](_shared/spec-driven-audit/) |
| Defer-then-promote tracking pattern (abstract) | [`_shared/defer-then-promote-pattern/`](_shared/defer-then-promote-pattern/) |
| Atomic edit pattern for sync-prone Drawio files | [`_shared/atomic-edits-pattern/`](_shared/atomic-edits-pattern/) |
| Generic edge-label principles | [`_shared/edge-labels-general/`](_shared/edge-labels-general/) |
| Shared scripts (cell update · cell add · revert) | [`_shared/scripts/`](_shared/scripts/) |

> **Reading a versioned leaf folder:** the convention is "use the highest `vN/` subfolder". E.g. opening [`_shared/scripts/`](_shared/scripts/) means "use whatever's in `v1/` today; when `v2/` exists, use that".

## Workflow for a new project

1. **Copy** the latest [`_project-template/`](_project-template/) PROJECT-CONVENTIONS.md → `<your-project>/diagram-conventions.md`
2. **Fill in** project-specific conventions (color palette, decision-ID prefixes, spec authority codes) — fill what applies, leave defaults for the rest
3. **Optionally pin skill module versions** if your project depends on older behavior (see [`VERSIONING.md`](VERSIONING.md) "How to pin to a specific version")
4. **Choose the diagram type** you're working on → open the corresponding sub-skill's `SKILL.md`
5. The sub-skill reads `diagram-conventions.md` · applies your conventions · resolves to latest version of each module unless pinned
6. Use [`_shared/spec-driven-audit/`](_shared/spec-driven-audit/) when auditing modules against specs

## Versioning at a glance

- Every **content module** (leaf folder · single doc concept) is versioned: `module/v1/`, `module/v2/`, …
- **Navigation docs** (SKILL.md, README.md, VERSIONING.md, sub-skill SKILL.md) are unversioned · always current
- Default: agents use the highest `vN/` subfolder
- User can pin to an older version via `diagram-conventions.md` Pinning section
- Read [`VERSIONING.md`](VERSIONING.md) for the full model

## Uniform folder structure (mandatory for every diagram-type sub-skill)

Every sub-skill folder under `models/model_NNN/diagram/<type>/` MUST follow this structure:

```
models/model_NNN/diagram/<type>/
├── SKILL.md                              ← unversioned · agent-facing entry point
├── conventions-schema/v<N>/              ← versioned content module
│   └── conventions-schema.md
├── conventions-defaults/v<N>/
│   └── conventions-defaults.md
├── <type-specific>/v<N>/                 ← e.g. edge-labels/, notation/, swimlanes/
├── patterns/v<N>/                        ← versioned content module
├── examples/v<N>/                        ← versioned content module
└── scripts/v<N>/                         ← versioned content module
```

`SKILL.md` stays unversioned (always describes current navigation). All content modules use `vN/` subfolders.

## Adding a new diagram-type sub-skill

When you encounter a diagram type not yet covered (DFD, activity, BPMN, sequence, state, ERD, etc.):

### Step 1 · Create the folder + versioned sub-folders

```
models/model_NNN/diagram/<new-type>/
├── conventions-schema/v1/
├── conventions-defaults/v1/
├── <type-specific>/v1/                   ← e.g. notation/v1/
├── patterns/v1/
├── examples/v1/
└── scripts/v1/
```

### Step 2 · Write the unversioned `SKILL.md`

Frontmatter (`name`, `description`) · when to use · workflow templates · links to versioned content modules (use leaf-folder paths, NOT `v1/`-suffixed) · anti-patterns.

### Step 3 · Write each module's v1 content

| Module | Content |
|---|---|
| `conventions-schema/v1/<schema>.md` | Checklist of conventions a project must define for this diagram type |
| `conventions-defaults/v1/<defaults>.md` | Sensible defaults applied if project doesn't specify |
| `<type-specific>/v1/<doc>.md` | Visual vocabulary + conventions (one or more docs) |
| `patterns/v1/*.md` | At least one reusable pattern |
| `examples/v1/*.md` | At least one worked walkthrough |
| `scripts/v1/*.py` + `README.md` | At least one type-specific helper |

### Step 4 · Update top-level files

| File | Update |
|---|---|
| Top-level `SKILL.md` (this file) | Add row to "Quick dispatch" table |
| Top-level `README.md` | Add section to "Folder layout" + adoption guide |
| `_project-template/v<N>/PROJECT-CONVENTIONS.md` | Add a section for project to fill in conventions for this diagram type |

### Step 5 · Validate

- All required sub-folders present with at least `v1/`
- Sub-skill SKILL.md exists (unversioned) and links to leaf folders (no hardcoded `v1` in links)
- Sub-skill is self-contained (references `_shared/` allowed)

## Core principles (across all diagram types)

1. **Conventions are data** — project specifies, skill applies
2. **Spec-driven audit** — coverage tables, not opinion
3. **Defer-then-promote** — accumulate surfaces of a pattern before structural commit
4. **Atomic script-driven edits** — survive sync races, batch related changes
5. **Reference-ID + characterization** in labels — audit trail + self-explanation
6. **Uniform folder structure** — every diagram-type sub-skill has the same shape
7. **Versioned content modules** — change one without affecting others

## Anti-patterns

- ❌ Hardcoding a project's specifics into the skill (colors, IDs, spec codes) → loses reusability
- ❌ Forgetting to load `diagram-conventions.md` before applying defaults → may use wrong palette
- ❌ Mixing diagram-type conventions in one folder → split per type for modularity
- ❌ Adding a new sub-skill with a different folder structure → breaks navigability
- ❌ Pinning hardcoded `v1` in links from SKILL.md → loses "latest" semantics
- ❌ Deleting old version subfolders → projects pinned to them break
