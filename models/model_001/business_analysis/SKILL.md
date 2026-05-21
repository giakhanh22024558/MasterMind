---
name: business_analysis
description: Turn any project input (documents, notes, transcripts, spreadsheets, diagrams...) into a structured business analysis — one consolidated requirements table, an ERD (entities + relationships, crow's-foot notation), and a derived feature list. Every table artifact is saved as a .md context file plus a pilotable .xlsx. Use when analyzing requirements, modeling system entities, or building a feature backlog from raw material.
---

# business_analysis — requirements → ERD + feature list

Packages the business-analysis workflow: ingest any input, consolidate it into **one requirements table**, then **in parallel** derive an **ERD** and a **feature list**.

This skill follows the [Core Rule](../../../core/core-rule/):

- **Input → Context** — the user's raw material is ingested into `context/` as `context.md` files.
- **Agent layer** — this skill's logic + the `scripts/` Python normalize content into the requirements table, the ERD, and the feature list. The `.md` artifacts are the source of truth.
- **User layer** — the pilotable `.xlsx` files and (on request) the `.drawio` ERD are written to `output/`.

## When to use this skill

Invoke when the user asks to:

- **Analyze** raw project material (specs, meeting notes, emails, existing documents, spreadsheets) into structured requirements
- **Build or update** the consolidated requirements table
- **Model** the system's entities and relationships as an ERD
- **Derive or update** the feature list / backlog
- **Re-run** analysis on new input — appended as a new timestamped batch

## First step in any task

1. **Session setup** — per the Core Rule, ensure `input/`, `context/`, `output/` exist; the user's `input/` is ingested into `context/`.
2. **Discover conventions** — look for `<project-root>/business_analysis-conventions.md` per [`conventions-as-data-pattern`](../../../core/meta/conventions-as-data-pattern/); fall back to [`conventions-defaults/`](conventions-defaults/).
3. **Acknowledge the source** when explaining choices ("per project conventions" / "using default").

## Workflow

### Step 1 — Consolidate requirements (always first)

Whatever the input format, produce **one consolidated requirements table**. Columns: `Req code`, `Topic`, `Criteria`, `Description`, `Ref. Docs`, `Q&A`, `Remarks`. Rows are grouped by **analysis-run timestamp** (the moment the user requested the analysis) for traceability. See [`requirements-table/`](requirements-table/).

### Step 2 — In parallel, from the requirements table

#### 2a · ERD

Model the system's entities and relationships with **crow's-foot notation**. Authored as **Mermaid inside a `.md`** context file; rendered to `.drawio` **only when the user explicitly asks**. The ERD is later used to spot edge cases and business rules, and to explain to the user how parts of the system affect each other. See [`erd-conventions/`](erd-conventions/).

#### 2b · Feature list

Derive features from the requirements. Columns: `Feature ID`, `Feature Name`, `Ref. Req (Feature)`, `Description (Feature)`, `User Story`, `Ref. Req (Story)`, `Description (Story)`, `Priority`, `Ready?`, `Done?`, `In Scope`. See [`feature-list/`](feature-list/).

### Output rule

Every **table** artifact (requirements, feature list) is saved twice: a `.md` in `context/` (the source of truth) **and** an `.xlsx` in `output/` for the user to pilot manually. The ERD is a Mermaid `.md`; a `.drawio` is produced in `output/` only on explicit request. Generate the `.xlsx` with [`scripts/ba_md_to_xlsx.py`](scripts/).

## Content modules

| Module | Purpose |
|---|---|
| [`requirements-table/`](requirements-table/) | The consolidated requirements table — columns, `REQ-xxxx` codes, timestamp batching |
| [`feature-list/`](feature-list/) | The feature list — columns, `FEAT-xxxx` codes, INVEST user stories |
| [`erd-conventions/`](erd-conventions/) | ERD crow's-foot conventions, Mermaid form, when to render `.drawio` |
| [`conventions-schema/`](conventions-schema/) | What a project must declare (code prefixes, Priority + In Scope value lists) |
| [`conventions-defaults/`](conventions-defaults/) | Defaults applied when the project doesn't specify |
| [`patterns/`](patterns/) | Reusable pattern — the requirements table as single source |
| [`examples/`](examples/) | Worked walkthrough — raw input to all three artifacts |
| [`scripts/`](scripts/) | `ba_md_to_xlsx.py` — generate the pilot `.xlsx` from a table `.md` |

## Core principles

- **Input-agnostic** — any input format reduces to the one requirements table.
- **Requirements first, single source** — the ERD and the feature list both derive from the requirements table.
- **Codes are auto-generated** — `REQ-xxxx` and `FEAT-xxxx` are sequential, never reused, never hand-assigned.
- **Timestamp traceability** — every requirement belongs to a dated analysis run.
- **`.md` is truth, `.xlsx` is the pilot copy** — never treat the `.xlsx` as the source.

## Anti-patterns

- ❌ Skipping the requirements table and jumping straight to features or an ERD — the table is the single source.
- ❌ Hand-assigning `REQ-`/`FEAT-` codes — they are generated sequentially.
- ❌ Rendering the ERD to `.drawio` without an explicit request — Mermaid `.md` is the default.
- ❌ Editing the `.xlsx` and expecting it to flow back to the `.md` — the `.md` is the source of truth.
- ❌ Inventing `In Scope` / `Priority` values outside the project's declared lists.

## Cross-references to meta-patterns

| Meta-pattern | This skill uses it when |
|---|---|
| [Core Rule](../../../core/core-rule/) | Input → context `.md` → agent layer → `.xlsx`/`.drawio` in `output/` |
| [Uniform skill structure](../../../core/meta/uniform-skill-structure/) | The skill follows the mandatory Shape A layout |
| [Conventions as data](../../../core/meta/conventions-as-data-pattern/) | Code prefixes + Priority/In Scope lists live in `<project>/business_analysis-conventions.md` |
| [Atomic edits](../../../core/meta/atomic-edits-pattern/) | The generator writes `.xlsx` (a sync-prone file) — close Excel before running |
