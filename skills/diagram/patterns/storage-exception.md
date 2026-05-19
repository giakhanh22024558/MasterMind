# Storage exception · hybrid edge granularity

How to decide when to use **layer-level** vs **component-level** edges on the master architecture diagram.

## The default rule

**Layer ↔ Layer / Sub-group ↔ Sub-group only.** No component-level edges on the master diagram.

Component-level data flow lives in dedicated DFD docs (`3-flows/data-flow/`).

## The storage exception

**Any edge where one endpoint is in a storage zone is rendered at component level.**

Covers:
- Layer ↔ individual storage cells
- Sync engine ↔ individual storage cells
- Any direction: read · write · bidirectional

## Why the exception exists

The questions auditors most often need answered:

| Question | Answer visible at master level |
|---|---|
| Which layer can write to which store? | ✅ via per-store edges |
| Which store accepts cloud ingress? | ✅ via specific sync edges |
| Which stores are local-only (no cloud sync)? | ✅ via absence of sync edges |
| Where does sensitive data live? | ✅ via sensitivity badges on store cells + specific edges |
| Does Layer X have access to Store Y's content? | ✅ per-store edge direction |

These questions are **architecturally consequential** for compliance audit. Hiding them in DFD docs forces auditors to consult multiple files. Showing at master = single-glance answer.

## When NOT to extend the exception

Tempting cases where extension would *seem* useful but creates more clutter than value:

- ❌ Component-level edges for compute pipelines (Stage A → Stage B → Stage C) — belongs in subsystem DFD
- ❌ Component-level edges for sibling reads within a layer — DFD scope
- ❌ Component-level edges for UI interaction — sequence diagram scope

**Default is layer-level.** Extend only when the question being answered is "which fine-grained X touches which fine-grained Y" AND the answer matters for compliance/audit.

## Worked example

### Before applying the exception (generic shapes)

```
LAYER_APP <--> DATA_GROUP   "R/W app data"
LAYER_CORE <--> DATA_GROUP  "R/W core data"
```

Generic — vendor can't tell *which* store has *which* sensitivity class.

### After applying the exception (per-store edges)

```
LAYER_APP  <--> STORE_CACHE   "R/W app data (profiles · preferences · drafts)"
LAYER_APP  <--> STORE_QUEUE   "R/W app-layer queues
                               (Comms · <decision-id> Network-independent)
                               + (Reports · offline-queue-first)"
LAYER_APP  <--> STORE_SENS    "R/W sensitive records (<privacy-class>)"

LAYER_CORE <--> STORE_QUEUE   "R/W core data (...)"
LAYER_CORE <--> STORE_TILES   "R/W tile bundles (Bundle writes · Renderer reads)"
STORE_HAZ   --> LAYER_CORE    "Reads overlays (runtime · local-only)"
```

Now the data-integrity story is visible:
- App can write to cache, queue (queue only — shared with core), sensitive store
- Core can write to queue (core data only), tiles; reads hazards
- Queue shared between App + Core but with **different schemas** per design-decision

## When to add a new architecture cylinder vs use existing

When a new schema/store is mandated by a spec audit and not already represented:

### Decision tree

```
New schema/store mandated by spec
├── Same tech as existing store? (e.g. same SQL engine, same cloud DB)
│   ├── Yes → can it share the existing cylinder via label expansion?
│   │   ├── Yes (same sensitivity class) → expand label, no new cell
│   │   └── No (different sensitivity / lifecycle) → add new cylinder
│   └── No (different tech) → add new cylinder
```

### Provisional cylinder treatment

When you add a new cylinder **preemptively** (before client/vendor confirms), use the **provisional style**:

- `fillColor=#fff8e1` (pale amber)
- `strokeColor=#f57c00` (orange · warning)
- `strokeWidth=1.5`
- `dashed=1; dashPattern=6 3` (distinct dash pattern)
- `fontColor=#e65100`
- Label includes badge: `PROVISIONAL · <design-decision-ID> PENDING`

This makes the preemptive nature obvious and triggers client review on the next read.

## Codifying the exception as a design decision

Capture the policy as a design-decision row (typically a visual-convention category, e.g. `V4`):

```
| V4 | Edge granularity in master | Layer ↔ Layer / Sub-group ↔ Sub-group by default.
    EXCEPTION — storage relationships: edges from/to individual storage components
    rendered at component level. Covers (a) Layer ↔ stores, (b) Sub-group ↔ stores,
    (c) Sync engine ↔ stores. Other component-level flow lives in DFD docs. |
    [A/B/C alternatives] | [rationale] | [revisit trigger] | 🟡 Provisional | [authority] |
```

Make sure the exception scope is **explicit and bounded** — without bound, every audit pushes "just one more exception" and the diagram becomes cluttered.
