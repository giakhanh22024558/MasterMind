# The business-analysis pipeline

The full definition of how the stage skills are sequenced into one end-to-end business analysis — from raw input to a finished SRS. Each stage's internal rules live in that stage's own skill; this pipeline owns only the sequencing and the hand-offs.

## Flow

```
input/  ──ingest──▶  context/
                        │
                        ▼
            [1] requirements  ──▶  requirements table
                        │            (single source)
            ┌───────────┴───────────┐
            ▼                       ▼
      [2a] erd                [2b] features          (parallel)
            │                       │
            └───────────┬───────────┘
                        ▼
      [3] for each feature: walk the ERD
          ──▶  business rules + edge cases
                        │
                        ▼
            [4] srs  ──▶  IEEE SRS document
```

## Stages

| # | Stage | Skill | Reads | Writes |
|---|---|---|---|---|
| 1 | Requirements | [`requirements`](../../document/requirements/) | every `context.md` ingested from `input/` | requirements table `.md` in `context/`; `requirements.xlsx` in `output/` |
| 2a | ERD | [`erd`](../../diagram/erd/) | the requirements table | ERD Mermaid `.md` in `context/`; `erd.drawio` in `output/` *(only on request)* |
| 2b | Feature backlog | [`features`](../../document/features/) | the requirements table | feature list `.md` in `context/`; `features.xlsx` in `output/` |
| 3 | Business rules + edge cases | *(uses the [`erd`](../../diagram/erd/) skill)* | the ERD + the feature list | per-feature business rules + edge cases (carried into stage 4) |
| 4 | SRS | [`srs`](../../document/srs/) | feature list + the stage-3 output | the IEEE SRS `.docx` in `output/` |

## Stage 3 in detail — business rules + edge cases

For **each feature** in the feature list:

1. **Locate** the ERD entities the feature touches.
2. **Walk** those entities' relationships and cardinalities — apply the [`erd`](../../diagram/erd/) skill's "Audit an ERD for edge cases" workflow.
3. **Derive business rules** — statements of **WHAT must always be true**: declarative, one rule per rule, invariant under UI / tech / flow change. (See the Business Rule criteria in the [`srs` skill](../../document/srs/srs-structure/).)
4. **Derive edge cases** — boundary situations, especially around `zero-or-many` cardinalities and mandatory relationships.

The business rules and edge cases are attached to the feature **by its `FEAT-xxxx` code**, ready for stage 4.

## Stage 4 in detail — into the SRS

The [`srs`](../../document/srs/) skill writes the SRS document; the pipeline feeds it:

- Each SRS module **corresponds to an Epic** (`EPIC-xxxx`) from the feature list.
- Each detailed use-case spec **references a `FEAT-xxxx` code** from the feature list.
- Stage 3's **business rules** → the feature's `#### Business Rules / System Behavior` table.
- Stage 3's **edge cases** → the feature's `Luồng ngoại lệ / Xử lý lỗi` (Exception flow) field.

## Ordering rules

- **Stage 1 always first** — the ERD and the feature list both derive from the requirements table; see [`../patterns/requirements-as-single-source.md`](../patterns/requirements-as-single-source.md).
- **Stages 2a and 2b are parallel** — neither consumes the other's output.
- **Stage 3 needs both** the ERD and the feature list.
- **Stage 4 is last** — it consumes the feature list and the stage-3 output.
- **Re-runs are incremental** — new input → `requirements` appends a timestamp batch → re-derive only the ERD entities, features, rules, and SRS sections the new batch affects.

## Hand-off contract

The currency between every stage is **codes** — `REQ-xxxx`, `EPIC-xxxx`, `FEAT-xxxx`, `US-xxxx`. Each artifact references the previous **by code, never by name**. This is what keeps the full chain — input → requirement → feature → SRS spec — exactly traceable.
