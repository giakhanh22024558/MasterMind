# business_analysis — README

The end-to-end **business-analysis pipeline**. It produces no artifact of its own — it orchestrates four stage skills, from raw input to a finished SRS.

## The pipeline

```
input → decode requirements → (ERD ‖ feature backlog)
      → use the ERD to find business rules + edge cases per feature
      → write everything into the SRS
```

| Stage | Skill | Produces |
|---|---|---|
| 1 | [`requirements`](../document/requirements/) | the requirements table |
| 2a | [`erd`](../diagram/erd/) | the ERD |
| 2b | [`features`](../document/features/) | the feature backlog (Epic → Feature → User Story) |
| 3 | *(uses `erd`)* | business rules + edge cases per feature |
| 4 | [`srs`](../document/srs/) | the IEEE SRS document |

## At a glance

1. Ingest `input/` → `context/` (Core Rule).
2. **Stage 1** — consolidate the requirements table (always first).
3. **Stages 2a + 2b parallel** — derive the ERD and the feature backlog.
4. **Stage 3** — for each feature, walk the ERD to find business rules + edge cases.
5. **Stage 4** — write everything into the SRS.

Everything is held together by **codes** (`REQ` → `EPIC`/`FEAT`/`US` → SRS specs) for exact traceability.

See [`SKILL.md`](SKILL.md) and [`pipeline/`](pipeline/) for the full definition.

## License

Internal. Adapt freely. No warranty.
