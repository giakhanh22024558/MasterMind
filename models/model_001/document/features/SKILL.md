---
name: features
description: Derive a feature backlog from a requirements table, organized as Epic → Feature → User Story. Every level has a code (EPIC-xxxx, FEAT-xxxx, US-xxxx) for exact traceability. Columns include Ref. Req, Description, Priority, Ready?, Done?, In Scope. Saved as a .md context file plus a pilotable .xlsx. Use to turn requirements into a developable, traceable backlog.
---

# features — feature backlog (Epic → Feature → User Story)

Derives a **feature backlog** from a requirements table, organized as a three-level hierarchy: **Epic → Feature → User Story**. Every level carries a code so the origin of anything is exact.

Follows the [Core Rule](../../../../core/core-rule/): the requirements table → the feature list (`.md`, the source of truth) → `features.xlsx` in `output/`.

## When to use this skill

Invoke when the user asks to:

- **Derive** a feature backlog from analyzed requirements
- **Organize** features under epics, with user stories under features
- **Update** the backlog as requirements change

## First step in any task

1. **Require a requirements table** — features derive from it. If none exists, run the [`requirements` skill](../requirements/) first.
2. **Discover conventions** — look for `<project-root>/features-conventions.md` per [`conventions-as-data-pattern`](../../../../core/meta/conventions-as-data-pattern/); fall back to [`conventions-defaults/`](conventions-defaults/).

## Workflow

1. **Read the requirements table.**
2. **Group into epics** — cluster related capability areas; assign each the next `EPIC-xxxx`.
3. **Define features** under each epic — assign `FEAT-xxxx`; cite the `REQ-xxxx` codes in `Ref. Req (Feature)`.
4. **Write user stories** under each feature — assign `US-xxxx`; INVEST-style, **short form** `[User] can [Action]`; cite `REQ-xxxx` in `Ref. Req (Story)`.
5. **Set fields** — `Priority` (story-level), `Ready?` / `Done?` / `In Scope` (feature-level), using the project's declared value lists.
6. **Render** — write the feature list `.md` into `context/`; generate `features.xlsx` into `output/` (the renderer is the pipeline's [`ba_md_to_xlsx.py`](../../business_analysis/scripts/)).

## Content modules

| Module | Purpose |
|---|---|
| [`feature-list/`](feature-list/) | The table structure — the Epic → Feature → User Story hierarchy, codes, the one-row-per-story model |
| [`conventions-schema/`](conventions-schema/) | What a project declares (code prefixes, Priority + In Scope lists) |
| [`conventions-defaults/`](conventions-defaults/) | Defaults |
| [`patterns/`](patterns/) | Reusable patterns |
| [`examples/`](examples/) | Worked walkthrough |
| [`scripts/`](scripts/) | `.xlsx` rendering |

## Core principles

- **Epic → Feature → User Story** — every feature sits in an epic; every story sits in a feature.
- **Everything has a code** — `EPIC-xxxx`, `FEAT-xxxx`, `US-xxxx`, all sequential, never reused, auto-generated.
- **Reference by code, never by name** — `Ref. Req` columns cite `REQ-xxxx`; this is what keeps traceability exact.
- **Every feature cites a requirement** — no feature without at least one `REQ-xxxx`.
- **User stories are short** — `[User] can [Action]`; detail lives in `Description` and the requirements table.
- **Declared values only** — use the project's `Priority` and `In Scope` lists.

## Anti-patterns

- ❌ A feature with no epic, or a user story with no feature.
- ❌ A feature with no `Ref. Req`.
- ❌ Hand-assigning `EPIC-` / `FEAT-` / `US-` codes.
- ❌ Referencing requirements by description instead of by `REQ-xxxx` code.
- ❌ Editing `features.xlsx` and expecting it to flow back to the `.md`.

## Cross-references

| Reference | Used for |
|---|---|
| [Core Rule](../../../../core/core-rule/) | Requirements → feature list `.md` → `.xlsx` in `output/` |
| [Conventions as data](../../../../core/meta/conventions-as-data-pattern/) | Code prefixes + Priority/In Scope lists in `<project>/features-conventions.md` |
| [`requirements` skill](../requirements/) | The requirements table features derive from |
| [`srs` skill](../srs/) | The SRS detailed use-case specs reference `FEAT-xxxx` codes from this list |
| [business_analysis pipeline](../../business_analysis/) | Orchestrates requirements → ERD + features → BR/edge cases → SRS |
