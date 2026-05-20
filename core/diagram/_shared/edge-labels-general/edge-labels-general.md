# Edge labels · general principles

Cross-diagram-type principles for edge labels. Diagram-type-specific rules (verb form for operational, noun for data-payload, etc.) live in each sub-skill's own `edge-labels.md`.

## Principle 1 · Labels carry semantic information

Edge labels should answer **"what is this relationship?"** at a glance — not require the reader to consult a separate doc.

If the reader has to follow the label to a 200-page spec to understand what's happening, the label is doing its job poorly.

## Principle 2 · Reference-ID + characterization format (mandatory when citing authority)

When a label needs to point to an authoritative source — a design-decision row, compliance section, spec authority, or named rejection trigger — use:

**Format:** `(<reference-ID> · <1-word characterization>)`

Why combined form wins:

| Approach | Pros | Cons |
|---|---|---|
| Pure reference `(per <ID>)` | Compact | Forces reader to look up the source doc to understand the semantic |
| Pure characterization `(<long-description>)` | Self-explanatory | Loses audit trail to the decision/spec |
| **Combined `(<ID> <characterization>)`** | Compact + immediate semantic clue + audit trail | Slightly more verbose than pure |

### Anatomy of a good label addition

```
(<owner-context> · <reference-ID> <hyphenated-1-2-word-characterization>)
```

- **owner-context** (optional): which component owns this · "CAL Comms", "Audit log", etc.
- **reference-ID**: the design-decision row · spec authority · compliance section ID
- **characterization**: short hyphenated phrase capturing what makes this relationship distinct

Examples (using placeholder IDs):
- `(CAL Comms · <decision-id> Network-independent)` — peer-to-peer queue edge
- `(consent-gated · <decision-id> opt-in)` — sensitive sync edge
- `(<schema-decision> write-once)` — append-only collection edge
- `(§<compliance-section> cache-only)` — exception ingress edge
- `(<rejection-trigger-id> no auto-action)` — prohibited operational edge

### Anti-patterns

❌ **Pure reference** (forces lookup, no semantic):
- `(per <ID>)`
- `(§7 exception)` — exception of what?
- `(<SPEC-CODE>)` — what does this mandate?

❌ **Pure characterization** (loses traceability):
- `(network-independent queue per vendor proposal)` — no decision-row pointer
- `(cache-only with TTL refresh)` — which mandate authorizes this exception?

## Principle 3 · Characterization word choice

The 1-word (or 2-hyphenated-word) characterization should:

- Be a **distinguishing semantic** — what makes this relationship distinct from others? Not a generic descriptor.
- Be **hyphenated** if multi-word (`Firebase-independent`, `consent-gated`, `auto-reroute`, `write-once`) — reads as a single concept.
- Be **short enough** to stay scannable at a glance (≤2 hyphenated words ideal).

## Principle 4 · Multi-line labels for compound semantics

When an edge has multiple semantic dimensions (write semantics + retention + privacy class, etc.), use `<br/>` for multi-line labels:

```
R/W app-layer queues
(Comms · <decision-id> Network-independent)
+ (Reports · offline-queue-first)
```

Don't try to squeeze everything onto one line — readability suffers.

## Principle 5 · Verb form for operational edges (diagram-type-specific)

For diagram types where edges represent **operational/control** relationships (most diagram types except pure data-payload), labels should be in **verb form** describing the action one component performs on the other.

See diagram-type-specific docs:
- [`architecture/edge-labels/`](../../../../models/model_001/diagram/architecture/edge-labels/)
- DFD edge conventions (not yet implemented)

## Principle 6 · Prohibition labels (mandatory format)

Across all diagram types, prohibited paths follow the same label structure:

```
[X] PROHIBITED
<reason><br/>
(<spec authority or rejection-trigger ID>)
```

Examples:
- `[X] PROHIBITED · Cloud cannot push to core · (<isolation-mandate-id>)`
- `[X] PROHIBITED · Zero outbound — core never initiates network`
- `[X] PROHIBITED · No cloud sync of telemetry · (<rejection-trigger-id>)`

## Worked example — evolving an edge label

**Iteration 1 (vague):** `R/W app data` — Too generic. Reader doesn't know which schemas.

**Iteration 2 (named schemas):** `R/W Queue` — Better, but doesn't capture what makes the queue distinct.

**Iteration 3 (reference only):** `R/W Queue (per <decision-id>)` — Audit trail ✅, but forces lookup.

**Iteration 4 (final form):**
```
R/W app-layer queues
(Comms · <decision-id> Network-independent)
+ (Reports · offline-queue-first)
```
Reference IDs ✅ · characterizations ✅ · distinguishes use cases ✅.
