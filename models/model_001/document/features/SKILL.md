---
name: features
description: Derive a feature list / backlog from a requirements table — columns Feature ID (FEAT-xxxx), Feature Name, Ref. Req, Description, User Story (INVEST, short form), Priority, Ready?, Done?, In Scope. Saved as a .md context file plus a pilotable .xlsx with dropdowns and checkboxes. Use to turn requirements into a developable feature backlog.
---

# features — feature list / backlog

Derives a **feature list** from a requirements table. Every feature is justified by one or more requirements; every feature carries one or more **user stories** (INVEST-style, short form).

Follows the [Core Rule](../../../../core/core-rule/): the requirements table → the feature list (`.md`, the source of truth) → `features.xlsx` in `output/`.

## When to use this skill

Invoke when the user asks to:

- **Derive** a feature list / backlog from analyzed requirements
- **Update** the feature list as requirements change
- **Write user stories** for features

## First step in any task

1. **Require a requirements table** — features derive from it. If none exists, run the [`requirements` skill](../requirements/) first.
2. **Discover conventions** — look for `<project-root>/features-conventions.md` per [`conventions-as-data-pattern`](../../../../core/meta/conventions-as-data-pattern/); fall back to [`conventions-defaults/`](conventions-defaults/).

## Workflow

1. **Read the requirements table** — group related requirements into candidate features.
2. **Create features** — assign the next sequential `FEAT-xxxx`; cite the `REQ-xxxx` codes in `Ref. Req`.
3. **Write user stories** — INVEST-style, **short form** `[User] can [Action]` (the requirements table is the backup context, so the full standard form is not required).
4. **Set fields** — `Priority`, `Ready?`, `Done?`, `In Scope` per the project's declared value lists.
5. **Render** — write the feature list `.md` into `context/`; generate `features.xlsx` into `output/` (the renderer is the pipeline's [`ba_md_to_xlsx.py`](../../business_analysis/scripts/)).

## Content modules

| Module | Purpose |
|---|---|
| [`feature-list/`](feature-list/) | The table structure — columns, `FEAT-xxxx` codes, the one-row-per-story model |
| [`conventions-schema/`](conventions-schema/) | What a project declares (code prefix, Priority + In Scope lists) |
| [`conventions-defaults/`](conventions-defaults/) | Defaults |
| [`patterns/`](patterns/) | Reusable patterns |
| [`examples/`](examples/) | Worked walkthrough |
| [`scripts/`](scripts/) | `.xlsx` rendering |

## Core principles

- **Every feature cites a requirement** — no feature without at least one `REQ-xxxx`.
- **Codes are auto-generated** — `FEAT-xxxx` is sequential, never reused.
- **User stories are short** — `[User] can [Action]`; detail lives in the `Description` columns and the requirements table.
- **Declared values only** — use the project's `Priority` and `In Scope` lists, never invent values.

## Anti-patterns

- ❌ Creating a feature with no `Ref. Req`.
- ❌ Hand-assigning `FEAT-` codes.
- ❌ Inventing `Priority` / `In Scope` values outside the project's declared lists.
- ❌ Editing `features.xlsx` and expecting it to flow back to the `.md`.

## Cross-references

| Reference | Used for |
|---|---|
| [Core Rule](../../../../core/core-rule/) | Requirements → feature list `.md` → `.xlsx` in `output/` |
| [Conventions as data](../../../../core/meta/conventions-as-data-pattern/) | Code prefix + Priority/In Scope lists in `<project>/features-conventions.md` |
| [`requirements` skill](../requirements/) | The requirements table features derive from |
| [business_analysis pipeline](../../business_analysis/) | Orchestrates requirements → ERD + features |
