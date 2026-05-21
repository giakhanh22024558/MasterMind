# business_analysis — README

The end-to-end **business-analysis pipeline**. It produces no artifact of its own — it orchestrates three stage skills into one workflow.

## The three stages

| Stage | Skill | Produces |
|---|---|---|
| 1 | [`requirements`](../document/requirements/) | the requirements table |
| 2a | [`erd`](../diagram/erd/) | the ERD |
| 2b | [`features`](../document/features/) | the feature list |

## Pipeline at a glance

1. Ingest `input/` → `context/` (Core Rule).
2. **Stage 1** — consolidate the requirements table (always first).
3. **Stages 2a + 2b in parallel** — derive the ERD and the feature list from the requirements table.
4. Deliverables written to `output/`.

See [`SKILL.md`](SKILL.md) for the agent-facing entry and [`pipeline/`](pipeline/) for the full definition.

## License

Internal. Adapt freely. No warranty.
