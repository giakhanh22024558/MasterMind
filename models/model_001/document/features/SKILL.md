---
name: features
description: Derive a feature backlog from a requirements table, organized as Epic → Feature → User Story. Produces a sheet with EXACTLY 9 LOCKED columns (Epic ID · Epic Name · Feature ID · Feature Name · Story ID · User Story · Priority · Status · Lifecycle) in a 3-row-type pattern (no merged cells, no extra columns). Every level has a code (EPIC-XX, FEAT-XXX, STORY-XXX) for exact traceability. Saved as the live sheet (Google Sheets or .xlsx) with a .md context sidecar. Use to turn requirements into a developable, traceable backlog with the same layout across every project.
---

# features — feature backlog (Epic → Feature → User Story)

Derives a **feature backlog** from a requirements table, organized as a three-level hierarchy: **Epic → Feature → User Story**. Every level carries a code so the origin of anything is exact.

Follows the [Core Rule](../../../../core/core-rule/): the requirements table → the feature list (live sheet, the source of truth) → `.md` sidecar in `context/` + optional `.xlsx` mirror in `output/`.

## 🔒 Critical rule — canonical layout (default-locked, project-extensible)

**Default:** every project produces the same 9-column sheet in the same order, with the same 3-row-type pattern. Sessions MUST NOT **silently**:
- Add columns (`SRS Feature ID`, `AC count`, `Description`, `Ref. Req`, `Owner`, `Sprint`, etc.) because they "seem useful"
- Remove, reorder, or translate canonical columns
- Merge cells across rows
- Invent hybrid layouts

**Escape hatch — explicit user request:** if the user explicitly asks to add columns (*"thêm cột X"*, *"add column Y"*), the session **does it without arguing** — appended at column J onwards, recorded in `<project>/features-conventions.md` → `extra_columns`. The change is **scoped to the current project only**.

**Promotion to model:** only when the user explicitly says *"save this to the model"* / *"lưu mẫu này vào model"* does the session edit MasterMind itself to make the extension a new global default.

See [`feature-list/feature-list.md`](feature-list/feature-list.md) for the canonical spec, full anti-pattern list, and extension/promotion mechanics. **Read it before producing any backlog.**

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
2. **Group into epics** — cluster related capability areas; assign each the next `EPIC-XX`. Write each as an **Epic row** (fill columns A+B only).
3. **Define features** under each epic — assign `FEAT-XXX`. Write each as a **Feature row** (fill columns C+D only).
4. **Write user stories** under each feature — assign `STORY-XXX`; INVEST-style, **short form** `[User] can [Action]`. Write each as a **Story row** (fill columns E–I only: Story ID, User Story, Priority, Status, Lifecycle).
5. **Use the dropdown values** declared in `<project>/features-conventions.md` (or the defaults) for Priority / Status / Lifecycle — no free-text values.
6. **Render** — the live sheet is the source of truth (Google Sheets via `integration/google_sheets` skill, or local `.xlsx`); produce a `.md` sidecar in `context/backlog.md` mirroring the 9-column markdown table.

> 🚫 **DO NOT** add columns for traceability (`Ref. Req`, `SRS Feature ID`), checklists (`Ready?`, `Done?`, `AC count`), ownership (`Owner`, `Sprint`), or descriptions. Cross-artifact links happen by **code reference inside the referencing artifact**, not by extra columns here. See [`feature-list/feature-list.md`](feature-list/feature-list.md) §"Forbidden — common deviations".

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
- **Everything has a code** — `EPIC-XX`, `FEAT-XXX`, `STORY-XXX`, all sequential, never reused, auto-generated.
- **Reference by code, never by name** — cross-artifact links cite codes (`REQ-XXXX`, `STORY-XXX`, `CR-XX`) *inside the referencing artifact* (SRS, AC sheet, Jira). Never add a `Ref. Req` column to the backlog itself.
- **User stories are short** — `[User] can [Action]`; detail belongs in the AC sheet or the SRS use-case spec, not in a backlog `Description` column.
- **Declared values only** — use the project's `Priority` / `Status` / `Lifecycle` lists.
- **9 columns, always** — layout is locked; extra fields go in a separate sheet keyed by `STORY-XXX`.

## Anti-patterns

- ❌ A feature with no epic, or a user story with no feature.
- ❌ Hand-assigning `EPIC-` / `FEAT-` / `STORY-` codes.
- ❌ **Silently** adding columns beyond the canonical 9 because they "seem useful" (silent inventions like `SRS Feature ID`, `AC count`, `Description`, `Ref. Req`, `Owner` — *unless the user explicitly asks*).
- ❌ Adding user-requested columns but **forgetting to record them in `<project>/features-conventions.md`** → next session won't reproduce them.
- ❌ Adding user-requested columns to the **model** (`MasterMind/...`) without explicit promotion intent from the user.
- ❌ **Merging cells** to span Epic Name / Feature Name across story rows — use the 3-row-type pattern instead.
- ❌ **Translating** canonical column headers (e.g. `Tên Epic` instead of `Epic Name`).
- ❌ **Reordering** canonical columns (e.g. `Status` before `Priority`) — extensions append at column J onwards.
- ❌ Editing the rendered `.xlsx` and expecting it to flow back to the live sheet / `.md` sidecar.

## Cross-references

| Reference | Used for |
|---|---|
| [Core Rule](../../../../core/core-rule/) | Requirements → feature list `.md` → `.xlsx` in `output/` |
| [Conventions as data](../../../../core/meta/conventions-as-data-pattern/) | Code prefixes + Priority/In Scope lists in `<project>/features-conventions.md` |
| [`requirements` skill](../requirements/) | The requirements table features derive from |
| [`srs` skill](../srs/) | The SRS detailed use-case specs reference `FEAT-xxxx` codes from this list |
| [business_analysis pipeline](../../business_analysis/) | Orchestrates requirements → ERD + features → BR/edge cases → SRS |
