---
name: requirements
description: Analyze any project input into one consolidated requirements table — columns Req code (REQ-xxxx), Topic, Criteria, Description, Ref. Docs, Q&A, Remarks. Rows are batched by analysis-run timestamp for traceability. Saved as a .md context file plus a pilotable .xlsx. Use to elicit, consolidate, and maintain a project's requirements.
---

# requirements — consolidated requirements analysis

Turns any input — documents, notes, transcripts, spreadsheets, diagrams — into **one consolidated requirements table**. Whatever the input format, every requirement lands in the same table.

Follows the [Core Rule](../../../../core/core-rule/): input → `context.md` → the requirements table (`.md`, the source of truth) → `requirements.xlsx` in `output/`.

## When to use this skill

Invoke when the user asks to:

- **Analyze** raw project material into structured requirements
- **Build or update** the consolidated requirements table
- **Re-run** analysis on new input — appended as a new timestamped batch

## First step in any task

1. **Session setup** — per the Core Rule, the user's `input/` is ingested into `context/`.
2. **Discover conventions** — look for `<project-root>/requirements-conventions.md` per [`conventions-as-data-pattern`](../../../../core/meta/conventions-as-data-pattern/); fall back to [`conventions-defaults/`](conventions-defaults/).

## Workflow

1. **Read all input** — every file in `context/`.
2. **Extract requirements** — one requirement = one row; assign the next sequential `REQ-xxxx` code.
3. **Batch by timestamp** — group this run's rows under the timestamp the analysis was requested (see [`requirements-table/`](requirements-table/)).
4. **Cite the source** — fill `Ref. Docs` for every row; never leave it empty.
5. **Render** — write the requirements table `.md` into `context/`; generate `requirements.xlsx` into `output/` (the renderer is the pipeline's [`ba_md_to_xlsx.py`](../../business_analysis/scripts/)).

## Content modules

| Module | Purpose |
|---|---|
| [`requirements-table/`](requirements-table/) | The table structure — columns, `REQ-xxxx` codes, timestamp batching |
| [`conventions-schema/`](conventions-schema/) | What a project declares (code prefix, citation style) |
| [`conventions-defaults/`](conventions-defaults/) | Defaults |
| [`patterns/`](patterns/) | Reusable patterns |
| [`examples/`](examples/) | Worked walkthrough |
| [`scripts/`](scripts/) | `.xlsx` rendering |

## Core principles

- **Input-agnostic** — any input format reduces to the one requirements table.
- **Codes are auto-generated** — `REQ-xxxx` is sequential, never reused, never hand-assigned.
- **Timestamp traceability** — every requirement belongs to a dated analysis run.
- **Every requirement is sourced** — `Ref. Docs` is mandatory.

## Anti-patterns

- ❌ Hand-assigning `REQ-` codes.
- ❌ Leaving `Ref. Docs` empty — a requirement with no source is not traceable.
- ❌ Editing `requirements.xlsx` and expecting it to flow back to the `.md` — the `.md` is the source of truth.

## Cross-references

| Reference | Used for |
|---|---|
| [Core Rule](../../../../core/core-rule/) | Input → context `.md` → `.xlsx` in `output/` |
| [Conventions as data](../../../../core/meta/conventions-as-data-pattern/) | Code prefix + citation style in `<project>/requirements-conventions.md` |
| [`features` skill](../features/) | Features derive from this requirements table |
| [business_analysis pipeline](../../business_analysis/) | Orchestrates requirements → ERD + features |
