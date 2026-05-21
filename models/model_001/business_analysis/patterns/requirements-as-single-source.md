# Pattern · Requirements table as the single source

The foundational pattern of `business_analysis`.

## Problem

A business analysis draws on many input forms — specs, meeting notes, emails, spreadsheets, diagrams — and must produce several artifacts (an ERD, a feature backlog). If each artifact is built straight from the raw input:

- The same requirement gets interpreted differently in the ERD and in the feature list → drift.
- There is no single place to see "what does the system need to do?".
- Traceability is lost — you cannot tell which feature answers which source.
- Re-analysis on new input means re-reading everything from scratch.

## Solution

Funnel **all** input into **one consolidated requirements table** first. Then derive every other artifact **from that table**, never from the raw input directly.

```
[any input]  ──consolidate──▶  REQUIREMENTS TABLE  ──derive──▶  ERD
                               (single source)      ──derive──▶  FEATURE LIST
```

- **Step 1 is always the requirements table.** No ERD, no features until it exists.
- The ERD's entities and the feature list's `Ref. Req` columns both point back into the table.
- New input → a new **timestamp batch** appended to the table → re-derive the affected ERD entities and features.

### Consequences

| Mechanism | Effect |
|---|---|
| `REQ-xxxx` codes | Stable anchors — every feature, every entity cites them |
| Timestamp batches | Any requirement traces to the run (and source) that produced it |
| One table | One answer to "what must the system do?" — no divergence |

## Trade-offs

**Pros**
- ERD and feature list never disagree — they share one source.
- Full traceability: source → requirement → feature, and source → requirement → entity.
- Re-analysis is incremental — append a batch, re-derive only what it touches.

**Cons**
- An upfront consolidation step before any diagram or backlog appears.
- Requires discipline: resist jumping straight to features when a stakeholder describes one.

## Worked example

See [`../examples/`](../examples/) — raw input consolidated into the requirements table, then an ERD and a feature list derived from it.

## When NOT to use

- A one-off throwaway question about a single feature — a full requirements table is overkill.
- The project already maintains an authoritative requirements register elsewhere — point at it instead of duplicating.

## Cross-references

- This is an instantiation of the [Core Rule](../../../../core/core-rule/): the requirements table is Layer-1 context, the source of truth.
- If a recurring analysis concern emerges (e.g. repeated ambiguous requirements), track it per [`defer-then-promote-pattern`](../../../../core/meta/defer-then-promote-pattern/).
