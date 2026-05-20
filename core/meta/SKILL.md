---
name: meta
description: Meta-skill — how to create a new skill in this repo. Captures the mindset, folder-structure conventions, and design patterns that every skill in `models/` follows. Use when starting a new skill (e.g. `business_analysis`, `code_review`, `data_modeling`) or when reviewing an existing skill's structure for consistency.
---

# Meta-skill — how to create any skill

This skill is **not about a specific domain**. It captures the mindset and conventions for creating ANY skill in this repo, so future sessions (any AI model, any contributor) can start a new skill (`business_analysis`, `code_review`, `data_modeling`, etc.) without re-deriving the patterns.

## When to use this skill

Invoke when:

- A user asks to **create a new skill** for a new domain
- You're **reviewing** an existing skill for structural consistency
- You're **deciding where to put new content** in an existing skill (which sub-folder)
- You need to **explain the structure** of the repo (`core/` + `models/`) to a new contributor

## The 3 core patterns (every skill applies these)

| Pattern | What it does | Read |
|---|---|---|
| **Uniform folder structure** | Every skill / sub-skill has the same shape — `SKILL.md`, `conventions-schema/`, `conventions-defaults/`, `patterns/`, `examples/`, `scripts/`, type-specific docs | [`uniform-skill-structure/`](uniform-skill-structure/) |
| **Conventions as data** | Project specifics (colors, IDs, codes) live in `<project-root>/<skill>-conventions.md` · skills read + apply · don't hardcode | [`conventions-as-data-pattern/`](conventions-as-data-pattern/) |
| **Defer-then-promote** | Emerging structural concerns get logged locally · promoted to canonical doc + structural change only after threshold reached | [`defer-then-promote-pattern/`](defer-then-promote-pattern/) |

Plus one applicable-when-relevant pattern:

| Pattern | When to use | Read |
|---|---|---|
| **Atomic edits** | When the skill manipulates sync-prone files (cloud-synced .drawio, .docx, etc.) | [`atomic-edits-pattern/`](atomic-edits-pattern/) |

## Main workflow · creating a new skill

See [`skill-creation-guide/`](skill-creation-guide/) for the full step-by-step process. Summary:

1. **Decide single vs multi-sub-skill** structure
2. **Copy the template** (`core/template/`) as starting skeleton
3. **Place it** in a model at `models/model_NNN/<category>/<your-skill-name>/`
4. **Fill in the required top-level docs** (`SKILL.md`, `README.md`)
5. **Populate** each content module with at least one item
6. **Write your skill's `conventions-schema/`** — what conventions does a project need to define when using your skill?
7. **Write `conventions-defaults/`** — sensible defaults if project doesn't specify
8. **Reference the meta-patterns** for things you don't need to re-document (conventions-as-data, atomic edits)

## Walkthrough · how the `diagram` skill applies these patterns

See [`examples/`](examples/) for a concrete walkthrough — how the `diagram` skill instantiates the core patterns.

## Anti-patterns

- ❌ **Skipping the meta-skill** — re-deriving "how to structure a skill" wastes effort and risks inconsistency
- ❌ **Hardcoding project specifics** in skill content — use conventions-as-data instead
- ❌ **Mixing diagram-type / domain-type concerns** in one folder — split per type for modularity
- ❌ **Skipping `conventions-schema/`** — without a schema, projects don't know what they need to specify

## Sub-skill content modules

| Module | Purpose |
|---|---|
| [`skill-creation-guide/`](skill-creation-guide/) | Step-by-step process for creating a new skill |
| [`uniform-skill-structure/`](uniform-skill-structure/) | The mandatory folder structure every skill follows |
| [`conventions-as-data-pattern/`](conventions-as-data-pattern/) | How to make conventions configurable per project, not hardcoded in skill |
| [`defer-then-promote-pattern/`](defer-then-promote-pattern/) | Abstract pattern for emerging structural concerns (CLR/HWG-style tracking) |
| [`atomic-edits-pattern/`](atomic-edits-pattern/) | Script pattern for sync-prone file edits (cloud-synced Drawio, etc.) |
| [`examples/`](examples/) | Walkthroughs of existing skills applying the meta-patterns |
| [`scripts/`](scripts/) | Helper scripts (e.g. scaffold a new skill from template) |

## Relationship to other skills

- **Every concrete skill in `models/`** should reference this meta-skill in its top-level `SKILL.md`
- Patterns common across many skills (conventions-as-data, atomic-edits, defer-then-promote) live HERE — not duplicated in each skill
- Skill-specific patterns (e.g. `models/model_001/diagram/architecture/patterns/storage-exception` is specific to architecture diagrams) stay in the skill
- If a pattern starts appearing in 3+ skills, **promote it to `core/meta/`** (defer-then-promote applied to meta-patterns themselves)

## Stack assumption

Skills in this repo assume:

- **Markdown** for all docs
- **Plain text** content (no binary blobs except diagram exports)
- **Python** for scripts (atomic-edits pattern, scaffolding)
- **Git** for version history
- **No build step** — content is consumable as-is

If a skill needs a different stack (e.g. TypeScript scripts, web UI), it should document the deviation in its own `SKILL.md`.
