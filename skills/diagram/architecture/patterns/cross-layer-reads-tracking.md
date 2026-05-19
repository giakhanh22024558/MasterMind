# Cross-Layer Reads (CLR) tracking pattern

How to handle "Layer A reads Layer B's data" relationships when they're rare enough to not warrant master-diagram edges yet, but real enough to track for audit.

## The problem

Architecture has an **Immutable Separation Boundary** between two layers (e.g. Experience ⇎ Survival Core, or OCS ⇎ Mobile data). The boundary prohibits **writes** in one direction, but **reads** are permitted under "limited surfaces" exception (per spec authority).

Example surfaces:
- App Layer reads Core's Event Log to render a UI viewer
- App Layer reads Core's breadcrumb history for a reverse-path display
- App Layer reads Core's anchor catalogue for a search picker

Each surface is a tiny architectural exception. Adding a master-diagram edge per surface clutters the overview. Skipping them entirely hides the exception from auditors.

## The defer-then-promote pattern

### Phase 1 · Log surfaces locally (1–2 surfaces)

In the appropriate subsystem doc (e.g. `mob-application-layer.md`), add a section:

```markdown
## Cross-layer read surfaces (Application Layer reading Survival Core data)

Per `compliance-matrix.md §X`: *"Application Layer can read from Core (limited surfaces) but NEVER write."*

These read surfaces are architecturally meaningful exceptions to the default visualization. When count reaches **≥3 surfaces**, promote to dedicated cross-cutting doc `4-cross-cutting/cross-layer-reads.md` + decide whether master diagram adds an aggregated edge.

### Known surfaces

| # | App-side feature | Reads from Core | Core schema | Permission basis |
|---|---|---|---|---|
| **CLR-01** | Event Log Viewer (read-only utility per <Module-ID> spec) | D5 event_log in <Storage-ID> | event_id · component · ts · payload | compliance §X limited-surface read |

### Candidate surfaces to audit (not yet spec-confirmed)

Features that MAY become CLR-XX entries when their specs land:
- BackTrack reverse-path display (reads D2 breadcrumb_log)
- Anchor catalogue browser (reads D6 anchor_points)
- SOS log review screen (reads D4 sos_log)
```

### Phase 2 · Codify the deferral policy (design-decision row)

Add a `V5` (or similar) row to `research/design-decisions.md`:

```
| V5 | Cross-layer reads visualisation policy |
    Defer master visualisation until ≥3 read surfaces confirmed.
    Track each known surface as CLR-XX in subsystem doc.
    When count reaches 3, promote to canonical 4-cross-cutting/cross-layer-reads.md
    + decide whether master diagram adds aggregated edge
    "<source layer> → <target layer> limited-surface reads (...)" |
    [4 options] | [rationale] | [trigger] | 🟡 Provisional (N/3 surfaces confirmed) |
    [authority] |
```

### Phase 3 · Promote at ≥3 surfaces

When 3rd CLR is confirmed via spec audit:

1. **Create** `4-cross-cutting/cross-layer-reads.md` with canonical CLR-XX inventory
2. **Move** the table from subsystem doc to cross-cutting doc
3. **Add** aggregated edge to master diagram:
   ```
   <Target Layer> → <Source Layer>
   "Limited-surface reads (Event Log · Reverse Path · Anchor list)"
   ```
   Or per-surface edges if visual clutter acceptable.
4. **Update** V5 status: `🟡 Provisional` → `🟢 Codified`
5. **Update** README navigation: `📅 deferred` → `✅ filled`

## Why this pattern works

- **Avoids premature commit**: 1-2 surfaces don't justify diagram clutter; 3+ start to feel structural
- **Preserves traceability**: every surface logged with spec ID + permission basis + schema
- **Explicit trigger**: count-based promotion removes subjective "is it time yet?"
- **Mirrors how V4 storage exception evolved**: collected enough cases before codifying hybrid rule

## Anti-patterns

- ❌ Add per-surface edge as soon as discovered → diagram clutters fast
- ❌ Skip tracking entirely → silent exception, audit miss
- ❌ Promote at 2 surfaces → too early, pattern not yet established
- ❌ Wait until 10+ surfaces → too late, retrofit pain
