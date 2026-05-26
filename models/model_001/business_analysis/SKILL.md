---
name: business_analysis
description: The end-to-end business-analysis pipeline. Orchestrates four skills — requirements, erd, features, srs — into one workflow: ingest any input, decode requirements, derive an ERD and a feature backlog, use the ERD to find business rules and edge cases for each feature, then write everything into an IEEE SRS document. Use to run a full business analysis from raw material to a finished SRS.
---

# business_analysis — the BA pipeline

This skill is a **pipeline**. It produces no artifact of its own — it **orchestrates four stage skills** into one coherent business-analysis workflow, and owns only the **sequencing and the hand-offs** between them.

```
input → decode requirements → (ERD ‖ feature backlog)
      → use the ERD to find business rules + edge cases for each feature
      → write everything into the SRS
```

| Stage | Skill | Category | Produces |
|---|---|---|---|
| 1 | [`requirements`](../document/requirements/) | document | the consolidated requirements table |
| 2a | [`erd`](../diagram/erd/) | diagram | the Entity-Relationship Diagram |
| 2b | [`features`](../document/features/) | document | the feature backlog (Epic → Feature → User Story) |
| 3 | *(uses the [`erd`](../diagram/erd/) skill)* | — | business rules + edge cases for each feature |
| 4 | [`srs`](../document/srs/) | document | the IEEE SRS document |

Each stage skill owns its own structure, conventions, and rules — read them there.

### Change-request branch

When the project **already has an SRS** and the client sends **change requests (CRs)**, the pipeline takes a side branch using the [`analysis`](../document/analysis/) skill before re-entering the main flow:

```
CRs + current SRS → gap analysis → impact analysis → user approval
                  → features (approved CRs) → back to stage 2 (erd / BR / srs updates)
                  → JIRA TASK CREATION (skill `integration/jira/`)
```

Bước cuối — skill [`integration/jira/`](../integration/jira/) đóng gói mỗi CR thành 1 main task + 3 sub-task (BA/FE/BE) để dev claim trên Jira.

## When to use this skill

Invoke when the user wants a **full business analysis** — from raw input all the way to a finished SRS. When the user sends **change requests** against an existing SRS, run the change-request branch (gap analysis → impact analysis → approval → features). For a single artifact, go straight to the relevant stage skill.

## The pipeline

See [`pipeline/`](pipeline/) for the full definition. In brief:

1. **Session setup** (Core Rule) — `input/` is ingested into `context/`.
2. **Stage 1 · requirements** — consolidate all input into the requirements table. **Always first** — it is the single source.
3. **Stages 2a + 2b · parallel** — derive the ERD and the feature backlog from the requirements table.
4. **Stage 3 · business rules + edge cases** — for **each feature**, walk the ERD to discover business rules (WHAT must always be true) and edge cases.
5. **Stage 4 · SRS** — write everything into the IEEE SRS document: epics → modules, features → detailed use-case specs, business rules + edge cases into each spec.

## Traceability

The whole chain is held together by **codes** — `REQ-xxxx` → `EPIC-xxxx` / `FEAT-xxxx` / `US-xxxx` → the SRS use-case specs. Every artifact references the previous by code, never by name, so the origin of anything is exact.

## Content modules

| Module | Purpose |
|---|---|
| [`pipeline/`](pipeline/) | The pipeline definition — stages, ordering, hand-offs |
| [`patterns/`](patterns/) | The cross-skill pattern — the requirements table as single source |
| [`examples/`](examples/) | End-to-end worked walkthrough |
| [`scripts/`](scripts/) | `ba_md_to_xlsx.py` — the shared `.xlsx` renderer for the table skills |

## Conventions

This pipeline has **no conventions of its own** — each stage skill carries its own `conventions-schema/` + `conventions-defaults/`. (A pipeline is an orchestration skill; it deliberately omits the conventions modules of the uniform structure.)

## Anti-patterns

- ❌ Running a later stage before stage 1 — the requirements table is the single source.
- ❌ Skipping stage 3 — the SRS's business rules and edge cases come from walking the ERD.
- ❌ Duplicating a stage skill's rules here — this pipeline only sequences and hands off.
- ❌ Referencing anything by name instead of by code.

## Cross-references

| Reference | Used for |
|---|---|
| [Core Rule](../../../core/core-rule/) | Input → context → agent layer → `output/` |
| [`requirements`](../document/requirements/) · [`erd`](../diagram/erd/) · [`features`](../document/features/) · [`srs`](../document/srs/) | The four orchestrated stage skills |
| [`analysis`](../document/analysis/) | The change-request branch — gap analysis → impact analysis → approval |
