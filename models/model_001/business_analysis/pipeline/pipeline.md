# The business-analysis pipeline

The full definition of how the three stage skills are sequenced. This is the **only** thing the `business_analysis` skill owns — each stage's internal rules live in that stage's own skill.

## Stages and hand-offs

```
input/  ──ingest──▶  context/
                        │
                        ▼
              ┌──────────────────────┐
   Stage 1    │  requirements skill  │  ──▶  requirements table (.md + .xlsx)
              └──────────┬───────────┘
                         │  (single source)
              ┌──────────┴───────────┐
              ▼                      ▼
   ┌────────────────┐     ┌────────────────────┐
   │   erd skill    │     │   features skill   │   Stages 2a + 2b — parallel
   └───────┬────────┘     └─────────┬──────────┘
           ▼                        ▼
   ERD (Mermaid .md;        feature list (.md + .xlsx)
   .drawio on request)
```

## Stage definitions

| # | Stage | Skill | Reads | Writes |
|---|---|---|---|---|
| 1 | Requirements | [`requirements`](../../document/requirements/) | every `context.md` ingested from `input/` | requirements table `.md` in `context/`; `requirements.xlsx` in `output/` |
| 2a | ERD | [`erd`](../../diagram/erd/) | the requirements table | ERD Mermaid `.md` in `context/`; `erd.drawio` in `output/` *(only on explicit request)* |
| 2b | Feature list | [`features`](../../document/features/) | the requirements table | feature list `.md` in `context/`; `features.xlsx` in `output/` |

## Ordering rules

- **Stage 1 always runs first.** The ERD and the feature list both derive from the requirements table — see [`../patterns/requirements-as-single-source.md`](../patterns/requirements-as-single-source.md).
- **Stages 2a and 2b are independent** — run them in parallel. Neither consumes the other's output; both consume only the requirements table.
- **Re-runs are incremental.** New input → the `requirements` skill appends a new timestamp batch → re-derive only the ERD entities and features affected by the new batch.

## Hand-off contract

- The hand-off currency between stages is the **requirements table** and its `REQ-xxxx` codes.
- Stage 2a's entities and Stage 2b's `Ref. Req` columns both point back to `REQ-xxxx` codes from Stage 1 — this is what keeps the ERD and the feature list consistent with each other.

## What this pipeline does NOT do

- It does not define table columns, code formats, or notation — those belong to the stage skills.
- It does not carry conventions — each stage loads its own project conventions file.
