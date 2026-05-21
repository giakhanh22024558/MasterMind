---
name: business_analysis
description: The end-to-end business-analysis pipeline. Orchestrates three skills — requirements (document), erd (diagram), features (document) — into one workflow: ingest any input, consolidate a requirements table, then in parallel derive an ERD and a feature list. Use to run a full business analysis from raw material to deliverables.
---

# business_analysis — the BA pipeline

This skill is a **pipeline**. It produces no artifact of its own — it **orchestrates three stage skills** into one coherent business-analysis workflow, and owns only the **sequencing and the hand-offs** between them.

| Stage | Skill | Category | Artifact |
|---|---|---|---|
| 1 | [`requirements`](../document/requirements/) | document | the consolidated requirements table |
| 2a | [`erd`](../diagram/erd/) | diagram | the Entity-Relationship Diagram |
| 2b | [`features`](../document/features/) | document | the feature list / backlog |

Each stage skill owns its own structure, conventions, and rules — read them there.

## When to use this skill

Invoke when the user wants a **full business analysis** — from raw input all the way to requirements + ERD + feature list. For a single artifact, go straight to the relevant stage skill.

## The pipeline

See [`pipeline/`](pipeline/) for the full definition. In brief:

1. **Session setup** (Core Rule) — `input/` is ingested into `context/`.
2. **Stage 1 · requirements** — run the [`requirements`](../document/requirements/) skill: consolidate all input into the requirements table. **Always first** — it is the single source for both later stages.
3. **Stages 2a + 2b · in parallel, from the requirements table:**
   - **2a · ERD** — run the [`erd`](../diagram/erd/) skill.
   - **2b · feature list** — run the [`features`](../document/features/) skill.
4. **Deliverables** — each table → `.md` (context) + `.xlsx` (`output/`); the ERD → Mermaid `.md` (+ `.drawio` on request).

## Content modules

| Module | Purpose |
|---|---|
| [`pipeline/`](pipeline/) | The pipeline definition — stages, ordering, hand-offs |
| [`patterns/`](patterns/) | The cross-skill pattern — the requirements table as single source |
| [`examples/`](examples/) | End-to-end worked walkthrough |
| [`scripts/`](scripts/) | `ba_md_to_xlsx.py` — the shared `.xlsx` renderer for both table skills |

## Conventions

This pipeline has **no conventions of its own** — each stage skill carries its own `conventions-schema/` + `conventions-defaults/`. The project's per-skill conventions files (`requirements-conventions.md`, `features-conventions.md`, `diagram-conventions.md`) are loaded by their respective stage. (A pipeline is an orchestration skill; it deliberately omits the conventions modules of the uniform structure.)

## Anti-patterns

- ❌ Running stage 2 before stage 1 — the requirements table is the single source.
- ❌ Duplicating a stage skill's rules here — this pipeline only sequences and hands off.
- ❌ Building the ERD or the feature list from raw input instead of from the requirements table.

## Cross-references

| Reference | Used for |
|---|---|
| [Core Rule](../../../core/core-rule/) | Input → context → agent layer → `output/` |
| [`requirements`](../document/requirements/) · [`erd`](../diagram/erd/) · [`features`](../document/features/) | The three orchestrated stage skills |
