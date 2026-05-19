# Edge label conventions

How to phrase edge labels for clarity, audit trail, and self-explanation.

## Rule 1 · Verb form for operational edges (mandatory)

**Operational / control edge labels MUST be in verb form** (solid `-->` and dashed `-.->` arrows). Never bare nouns.

The verb is conjugated for the source node: *"Surfaces …"*, *"Enables …"*, *"Writes …"*, *"Scrapes …"*.

| ❌ Bad (bare noun) | ✅ Good (verb form) |
|---|---|
| `Operational Visibility` | `Surfaces metrics pipeline` |
| `Intervention and Control` | `Enables break-glass intervention` |
| `Cache & Sessions` | `Writes cache / session` |
| `DB queries` | `Queries database` |

Parenthetical detail after the verb phrase is fine for context:
- ✅ `Surfaces metrics pipeline (Ingest · Transform · Score · Publish)`

### Bidirectional / symmetric edges

Phrase from the arrow's source side, OR use two separate edges with one verb each.

For R/W relationships with stores, `R/W <store>` is acceptable shorthand.

## Rule 2 · Noun form for data-payload edges (exception)

**Dotted purple `-.->` arrows with `stroke-dasharray:2 3`** = data payload — label with the data noun itself.

Examples:
- `User profile records`
- `Event stream`
- `Hazard overlay records`
- `Compiled bundle + manifest`

The arrow style + color already conveys "this is a data flow", so the label names the **payload**, not the **action**.

## Rule 3 · Reference-ID + characterization (mandatory when citing authorities)

When an edge label needs to point to an authoritative source — a design-decision row, compliance section, spec authority, or named rejection trigger — use this format:

**Format:** `(<reference-ID> · <1-word characterization>)`

Or chained: `(<owner/context> · <reference-ID> <characterization>)`

### Why this format

| Approach | Pros | Cons |
|---|---|---|
| Pure reference `(per <ID>)` | Compact | Forces reader to open the source doc to understand semantic |
| Pure characterization `(<long-description>)` | Self-explanatory | Loses audit trail to decision rationale |
| **Combined `(<ID> <characterization>)`** | Compact + immediate semantic clue | Slightly more verbose than pure |

### Good examples (template — replace IDs with your project's)

- `(<comms-decision-id> Network-independent)` — peer-to-peer queue edge
- `(consent-gated · <sync-decision-id> opt-in)` — sensitive sync edge
- `(<storage-decision-id> unified-store)` — container note
- `(<schema-decision-id> write-once)` — append-only collection edge
- `(§<compliance-section> cache-only)` — exception ingress edge
- `(<rejection-trigger-id> no auto-action)` — prohibited operational edge
- `(<spec-authority-id> forensic-immutable)` — log immutability edge note

### Bad — pure reference (forces lookup)

- ❌ `(per <ID>)` — what does `<ID>` say?
- ❌ `(§7 exception)` — exception of what?
- ❌ `(<SPEC-CODE>)` — what does this mandate?

### Bad — pure characterization (loses traceability)

- ❌ `(network-independent queue per vendor proposal)` — no decision-row pointer
- ❌ `(cache-only with TTL refresh)` — which mandate authorizes this exception?

### 1-word characterization rules

- A **distinguishing semantic** (what makes this relationship distinct) — not a generic descriptor
- **Hyphenated** if multi-word (`Firebase-independent`, `consent-gated`, `auto-reroute`, `write-once`) — reads as a single concept
- **Short enough** to stay scannable at a glance (≤2 hyphenated words ideal)

## Rule 4 · TRIGGER prefix on initiating edges (DFD convention)

In Data Flow Diagrams, mark edges that **initiate execution** of the destination process with the `TRIGGER:` prefix:

- `TRIGGER: user_action(payload)` — user input initiates a process
- `TRIGGER: sensor_event(data)` — sensor pulse initiates a process
- `TRIGGER: scheduled_tick` — timer initiates a process
- `TRIGGER: sibling_event` — peer event initiates a state transition

Distinguishes "what causes this process to run" from regular data-flow inputs.

## Rule 5 · Prohibited path labels (mandatory format)

Red dashed edges (`stroke:#c62828, stroke-dasharray:5 5`) for prohibited paths:

```
[X] PROHIBITED
<reason><br/>
(<spec authority or rejection-trigger ID>)
```

Examples (template — replace placeholders):
- `[X] PROHIBITED · Cloud cannot push to core · (<isolation-mandate-id>)`
- `[X] PROHIBITED · Zero outbound — core never initiates network`
- `[X] PROHIBITED · No cloud sync of telemetry · (<rejection-trigger-id>)`

## Worked example — evolving an edge label

**Iteration 1 (vague):**
```
LAYER_A <--> STORE  "R/W app data"
```
Too generic — reader doesn't know which schemas are touched.

**Iteration 2 (named schemas):**
```
LAYER_A <--> STORE  "R/W Queue"
```
Better — but doesn't capture what makes the queue distinct.

**Iteration 3 (reference only):**
```
LAYER_A <--> STORE  "R/W Queue (per <decision-id>)"
```
Has audit trail, but forces lookup to understand semantic.

**Iteration 4 (final form — combined):**
```
LAYER_A <--> STORE  "R/W app-layer queues
                     (Comms · <decision-id> Network-independent)
                     + (Reports · offline-queue-first)"
```
Verb form ✅ · reference IDs ✅ · characterizations ✅ · distinguishes use cases ✅.
