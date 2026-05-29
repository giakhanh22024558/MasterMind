# Foundation register — canonical structure (Topic → Concern → Task → ACs)

The Sprint 0 foundation, organized as a three-level hierarchy. The foundation-phase analog of the [feature list](../../features/feature-list/feature-list.md).

## The hierarchy

| Level | What it is | Code | Analog (`features`) |
|---|---|---|---|
| **Topic** | A theme grouping related concerns | `TOPIC-NN` | Epic |
| **Concern** | A technical concern — an area of cross-cutting foundation | `Concern N` (catalogue) | Feature |
| **Task** | A buildable unit of foundation work | `FND-NNN` | User Story |
| **AC** | A verifiable done-criterion (DoD) for a Task | `AC-FND-{task}-{nn}` | Acceptance Criterion |

Every level carries a sequential, never-reused, auto-assigned code. Width of the numeric suffix is the only ID format an override may change.

## Two artifacts — register + separate ACs file

1. **Foundation register** (source of truth) — Topic → Concern → Task, each task with its **Reference** (governing source doc[s]). No ACs inline.
2. **ACs file** (sidecar) — keyed by Task ID, one row per AC (`AC-FND-{task}-{nn}`), grouped by the same Topic → Concern → Task order.

> Mirrors the `features` split: the backlog sheet holds the stories; the Acceptance-Criteria sheet (separate) holds the ACs. Keep the register tidy; depth lives in the ACs file.

## Register layout

Group by **Topic** (heading), then **Concern** (sub-heading), then a per-concern table:

```
### TOPIC-01 — <topic name>

#### Concern 1 — <concern name>  (refs: <governing docs>)
| Task | Reference |
|---|---|
| **FND-001 — <task name>** (<short scope>) | <DOC §x> · <DOC> · <path> |
| **FND-002 — …** | … |

#### Concern 2 — …
...
```

- **Task cell** = `FND-NNN — <name>` (the name carries the description; no separate Description column).
- **Reference cell** = the spec(s)/source to read first, by code + section, plus any existing project asset path.
- Optionally tag committed gate deliverables with a marker (e.g. 🎯) and a deliverable ID.

## ACs file layout

Same Topic → Concern order; one row per AC:

```
### TOPIC-01 — <topic name>
#### Concern 1 — <concern name>
| Task | AC ID | Acceptance Criterion (DoD) |
|---|---|---|
| FND-001 <task name> | AC-FND-001-01 | <verifiable criterion> |
|  | AC-FND-001-02 | <verifiable criterion> |
| FND-002 … | AC-FND-002-01 | … |
```

- ACs are **verifiable** (a reviewer can check pass/fail), in the project's declared AC language.
- A standard / threshold / rule (e.g. an accessibility level, a numeric budget, a prohibited-list) is encoded **as an AC of the relevant task**, never as its own task.

## Rules

**Non-negotiable:**
1. Every Concern belongs to exactly one Topic; every Task to exactly one Concern; every AC to exactly one Task.
2. Codes are sequential, never reused, never hand-assigned.
3. ACs live in the **separate ACs file**, keyed by Task ID — not inline in the register.
4. Foundation tasks are **enablers**, not end-user features. Business-functional capabilities belong in [`features`](../../features/).
5. Standards/criteria are **ACs**, not Tasks.

**Default (overridable per project):**
6. Concerns are drawn from the default catalogue ([`../conventions-defaults/`](../conventions-defaults/)); projects add/remove concerns.
7. Tasks numbered in build order; incremental additions append at the tail and fold into order at the next major pass.

## Cross-references

- [`../conventions-defaults/conventions-defaults.md`](../conventions-defaults/conventions-defaults.md) — default concern catalogue + ID/AC formats + gate-buffer defaults
- [`../patterns/topic-grouping.md`](../patterns/topic-grouping.md) — how to group concerns into topics
- [`../patterns/gate-buffer-and-parallelisation.md`](../patterns/gate-buffer-and-parallelisation.md) — schedule before the first gate with a risk buffer
- [`../../features/feature-list/feature-list.md`](../../features/feature-list/feature-list.md) — the twin (Epic→Feature→US)
