# Hardware Access Gaps (HWG) tracking pattern

How to handle architectural ambiguity when an app-side feature needs device hardware (GNSS, camera, BLE, etc.) but the source spec doesn't explicitly specify how the access happens.

## The problem

Architecture has clear edges modeling hardware access for some consumers (e.g. `HW_GNSS → CORE_LAYER "(continuous · NAV/BT/SOS)"`). When auditing an App Layer feature that *also* needs the same hardware (e.g. TrackMate location sharing needs GNSS), one of three things might be true:

1. **Pattern α — Direct OS access**: feature uses Platform API directly (Flutter plugin, native binding) → needs new edge `HW_X → APP_LAYER`
2. **Pattern β — Cross-layer read**: feature reads from another layer's published state (e.g. NAV's position fix) → log as CLR entry instead
3. **Pattern γ — Implicit OS-level**: feature uses standard OS capability not modeled in architecture (e.g. clock, system time) → no edge needed

Spec is often **ambiguous** between these patterns. Architecture can't commit without knowing.

## The defer-then-resolve pattern

### Phase 1 · Log gap with resolution options

In subsystem doc (e.g. `mob-application-layer.md`), add a section:

```markdown
## App-side hardware access gaps (pending spec clarification)

Application Layer features sometimes need on-device hardware (GNSS · camera · accelerometer · etc.) — but master architecture currently only renders `HW_X → CORE` edges. When an App-side feature has a documented hardware dependency without a matching architecture edge, track as HWG-XX entry here until spec resolution.

### Known gaps

| # | App-side feature | Hardware needed | Current architecture | Resolution options |
|---|---|---|---|---|
| **HWG-01** | <Feature> (<spec-ID>) — <what it needs hardware for> | `HW_X` (<HW-spec-ID>) | Edge `HW_X → CORE` exists with label "(continuous · NAV/BT/SOS)" — does NOT name-check App. No `HW_X → APP_LAYER` edge | **α** Direct OS access → add edge `HW_X → APP_LAYER`<br/>**β** Read from Core's published state → log as CLR-XX (contributes to V5 trigger)<br/>**γ** Pure UI (no hardware) → skip<br/>**Pending:** spec confirmation |
```

### Phase 2 · Consolidation observation

After 2+ HWG entries land that share the same hardware:

```markdown
> **Consolidation observation:** if HWG-01 and HWG-02 both resolve to Pattern α (direct OS access),
> they share the same target hardware and would be served by a **single consolidated edge**
> `HW_X → APP_LAYER` rather than per-feature edges. Defer the consolidation decision until
> spec resolution.
```

### Phase 3 · Resolve per gap

When each gap's source spec lands or vendor confirms:

| Resolution | Action |
|---|---|
| **α** (direct OS) | Add edge `HW_X → APP_LAYER` to master diagram. If multiple HWGs resolve α with same HW, add single consolidated edge |
| **β** (cross-layer read) | Move entry to CLR section · contributes to V5 trigger count |
| **γ** (implicit) | Strike entry · mark resolved · document rationale |

## Candidate gap list maintenance

Maintain a separate "candidate gaps to audit" sub-section listing features whose specs haven't landed yet:

```markdown
### Candidate gaps to audit (when other features are spec'd in detail)

These features MAY have hardware dependencies — re-audit when their specs land:
- ~~**Feature A**~~ → **RESOLVED:** spec confirms NO hardware needs
- ~~**Feature B**~~ → **RESOLVED:** camera prohibited per spec · location elevated to HWG-02
- **Feature C** — does it need <hardware>?
```

Strike resolved entries with rationale. New entries added as more features are audited.

## Why this pattern works

- **Avoids premature edge addition** to architecture before spec confirms
- **Preserves audit trail** of which features need which hardware
- **Surfaces consolidation opportunity** before adding redundant edges
- **Parallels CLR pattern** — same "defer-then-resolve" structure, predictable to apply

## Worked example sequence

Project audits TrackMate (TM) module:
- TM spec says "Structured data containing WGS84 coordinates" but doesn't say *how* TM gets the coordinates
- → Log **HWG-01** with 3 resolution options (α / β / γ)

Project audits PCR Framework module:
- PCR spec says "User-confirmed coordinates on the map" — ambiguous between map-tap (no GNSS), GNSS-propose-then-confirm, or read-from-NAV
- → Log **HWG-02** with 3 resolution options
- → Add consolidation observation: if both resolve to α, single consolidated edge

Both pending spec confirmation. Architecture stays clean. Audit trail intact. When client/vendor responds, resolve each per the documented pattern.

## Anti-patterns

- ❌ Add `HW_X → APP_LAYER` edge speculatively → may prove wrong, hard to remove later
- ❌ Skip tracking → silent dependency, audit miss
- ❌ Consolidate prematurely (before all gaps confirmed) → may need to split again
