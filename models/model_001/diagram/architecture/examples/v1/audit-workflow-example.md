# Example · spec-driven audit walkthrough

A worked example of auditing one module's spec against the current architecture, identifying gaps, and resolving them. Uses generic placeholders — adapt to your project.

## Setup

Imagine you're working on a system with:
- A master architecture diagram (Mermaid + Drawio twin in `diagrams/1-overview/`)
- A few layers: `LAYER_A` (client app), `LAYER_B` (core / safety-critical), `LAYER_C` (cloud backend), `STORE_GROUP` (local persistence with cylinders `STORE_X`, `STORE_Y`, `STORE_Z`)
- Cross-cutting docs in `diagrams/4-cross-cutting/`: `compliance-matrix.md`, `performance-targets.md`
- Design decisions table in `research/design-decisions.md` with rows like `M0a`, `M0b`, `S1`

The user asks you to audit **MODULE-101**, a feature in `LAYER_A`, against this spec:

```
MODULE-101 is a feature in the Experience Layer that handles user-generated
records. Inputs: text payload (max N chars), location coordinates, peer
discovery via short-range radio. Outputs: local queue (write-ahead, encrypted)
with optional cloud sync. Prohibited from making outbound network calls during
core safety operations.
```

## Step 1 · extract checkable items from spec

| # | Spec item | Type |
|---|---|---|
| 1 | Text payload (max N chars) | Input · validation |
| 2 | Location coordinates | Input · hardware |
| 3 | Peer discovery via short-range radio | Input · hardware |
| 4 | Local queue write (write-ahead, encrypted) | Output · storage |
| 5 | Optional cloud sync | Output · sync |
| 6 | Prohibited outbound during core safety ops | Constraint · prohibition |

## Step 2 · build coverage table

Compare each item against current architecture state:

| # | Spec item | Current edge/element | Status |
|---|---|---|---|
| 1 | Text payload (max N chars) | Validation rule · not an edge | ✅ Out of edge scope |
| 2 | Location coordinates | Edge `HW_LOCATION → LAYER_B` exists with label "(continuous · core consumers)" — does NOT name-check `LAYER_A` | 🟡 Gap · either label or new edge |
| 3 | Peer discovery via radio | Edge `LAYER_A_TRANSPORT ↔ HW_GROUP "Drives BLE · Wi-Fi · LoRa radios"` exists | ✅ Covered |
| 4 | Local queue write-ahead encrypted | Edge `LAYER_A ↔ STORE_X "R/W app data"` exists · doesn't name-check queue schema | 🟡 Label gap |
| 5 | Optional cloud sync | Edge `LAYER_A → SYNC_LAYER "User data writes"` exists | ✅ Generic outbound covered |
| 6 | Prohibited outbound during core safety ops | Layer-level prohibited edge `LAYER_B → SYNC_LAYER [X] PROHIBITED` — covers core, doesn't specifically address `LAYER_A` during core ops | 🟡 Indirect coverage |

## Step 3 · classify gaps

- **Gap (2)** — hardware access ambiguity: spec doesn't say if `MODULE-101` reads location via direct OS API or via `LAYER_B`'s published position
- **Gap (4)** — local queue schema not visible in edge label; vendor doesn't know which schema `MODULE-101` writes to
- **Gap (6)** — partial coverage; spec emphasis "during core safety ops" suggests a finer-grained prohibition than current layer-level

## Step 4 · recommend options per gap

### Gap (2) · Location source ambiguity

| Option | Description |
|---|---|
| α — direct OS access | Add edge `HW_LOCATION → LAYER_A` |
| β — read from `LAYER_B`'s published position | Log as cross-layer-read entry; don't add edge yet |
| γ — defer + flag | Note in subsystem doc · wait for spec clarification |

**Recommend**: γ (defer). The architectural choice has long-term impact (couples or decouples `LAYER_A` from `LAYER_B`).

### Gap (4) · Queue schema not named

| Option | Description |
|---|---|
| A — expand label | Add schema name to existing edge: `"R/W app-layer queues (Comms · <decision-id> WAL-encrypted)"` |
| B — add new cell | Separate cylinder for the queue (overkill — same backing store) |
| C — skip | Generic "app data" covers it (loses traceability) |

**Recommend**: A (low-effort, high-value clarity).

### Gap (6) · Fine-grained prohibition

| Option | Description |
|---|---|
| A — add red-dashed edge | New `MODULE-101 → SYNC_LAYER [X] PROHIBITED during core ops` |
| B — document in compliance matrix only | Existing `LAYER_B → SYNC_LAYER` prohibition implicitly covers |
| C — defer | Log as compliance question for client |

**Recommend**: B (compliance matrix entry · keep master uncluttered).

## Step 5 · apply chosen options + log

### Apply Gap (4) Option A

Edit Mermaid:
```diff
- LAYER_A <-->|"R/W app data"| STORE_X
+ LAYER_A <-->|"R/W app-layer queues<br/>(Comms · <decision-id> WAL-encrypted)<br/>+ (Reports · offline-queue-first)"| STORE_X
```

Apply same change to Drawio via `update-cell-value.py` (in [`_shared/scripts`](../../../../../../core/diagram/_shared/scripts/)):
```python
CELL_ID = "e_layer_a_to_store_x"
NEW_VALUE = "&lt;b&gt;R/W app-layer queues&lt;/b&gt;..."
```
Run · verify · move on.

### Log Gap (2) for deferred resolution

In `diagrams/2-subsystems/<zone>.md`, add to the "App-side hardware access gaps" section:

```markdown
| **HWG-01** | **MODULE-101 location access** — needs lat/lon for record geotagging | `HW_LOCATION` | Edge `HW_LOCATION → LAYER_B` exists but does not name-check LAYER_A | **α** Direct OS access<br/>**β** Read from LAYER_B's published position (log as CLR)<br/>**Pending**: spec confirmation |
```

### Document Gap (6) in compliance matrix

In `diagrams/4-cross-cutting/compliance-matrix.md`, add:

```markdown
- [ ] **MODULE-101 outbound restriction during core safety ops** — MODULE-101 must NOT initiate outbound network calls while `LAYER_B`'s safety-critical operations are active. Implementation: gated by `core_active` state flag · enforced by code-level check, not by architectural edge prohibition.
```

## Step 6 · update subsystem doc with audit findings

In `diagrams/2-subsystems/<zone>.md` "Per-module audit findings":

```markdown
### `MODULE-101` — audited (YYYY-MM-DD)

- [ ] Inputs: text payload (≤N chars) · location coords · peer discovery via short-range radio
- [ ] Storage: local queue in `STORE_X` (Comms queue schema · WAL-encrypted) · optional cloud sync
- [ ] Constraint: no outbound network during core safety operations · enforced by `core_active` flag check
- [ ] **Architecture status**:
  - Gap (4) fixed · edge label expanded to name-check queue schema
  - Gap (2) deferred · logged as **HWG-01** pending spec clarification (direct OS access vs read from LAYER_B)
  - Gap (6) documented in compliance matrix (code-level enforcement, not architectural edge)
```

## Step 7 · next module

Repeat for the next module in the same layer. After ~3–4 modules audited, patterns emerge:

- Multiple HWG entries → may consolidate to single `HW_X → LAYER_A` edge once spec confirms direct OS access pattern
- Multiple cross-layer reads → may promote to dedicated cross-cutting doc when count reaches threshold
- Multiple deferred design decisions → tabulate as paired blockers for client meeting

This is how the architecture's design-decisions table grows organically.

## Recap · what went right

- ✅ Coverage table built before proposing fixes — caught Gap (2) ambiguity that would otherwise have been silently committed
- ✅ Each gap presented with options — user makes the architectural choice, not the agent
- ✅ Atomic script edit — Mermaid + Drawio stay in sync
- ✅ Non-applied gaps logged in subsystem doc — audit trail preserved
- ✅ Compliance matrix referenced for code-level enforcement — diagram stays clean

## Recap · what to avoid

- ❌ Adding all 3 gap fixes without user choice
- ❌ Generating an edge `HW_LOCATION → LAYER_A` from Gap (2) without spec confirmation — would be imaginary architecture
- ❌ Forgetting to update Mermaid AND Drawio together
- ❌ Logging the audit findings only in conversation, not in subsystem doc
