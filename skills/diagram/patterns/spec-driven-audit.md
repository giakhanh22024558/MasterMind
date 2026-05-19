# Spec-driven audit

The workflow for verifying that an architecture diagram matches what a module spec mandates. Apply per-module as specs land.

## Why "spec-driven"

Architecture without spec backing is opinion. Spec without diagram coverage is invisible. The audit closes the gap by **systematically checking each spec mandate against the diagram** and capturing gaps as tracked design decisions.

## The 5-step workflow

### 1. Read spec carefully · extract checkable items

Open the spec (provided by user or read from a project file). List every:
- **Input** (where data comes from)
- **Output** (where data goes)
- **Storage target** (where state persists)
- **Constraint** (prohibition, mandate, invariant)
- **Performance target** (numeric SLA)
- **Compliance reference** (RT codes, spec section, mandate ID)
- **Hardware dependency** (sensor, camera, radio, etc.)
- **External entity** (3rd-party API, user actor, peer system)

Aim for a flat list of ~10–20 items. Anything not on the list won't be audited.

### 2. Build coverage table

3-column table per spec item:

```markdown
| Spec item | Current edge/element | Status |
|---|---|---|
| Input X from sensor | `HW_X → CORE_LAYER` (named in label) | ✅ Covered |
| Output Y to local store | No edge from this module to STORE_Y | 🔴 Missing |
| Constraint Z (no auto-action) | Compliance matrix §N mentions it | ✅ Content |
| Performance ≤200ms | Not in performance-targets.md | 🟡 Partial (missing PT row) |
| ... | ... | ... |
```

### 3. Classify each gap

| Symbol | Meaning | Action |
|---|---|---|
| ✅ Covered | Spec item already represented | None |
| 🟡 Partial | Architecture covers it but label/content needs refinement | Apply minor label expansion or content addition |
| 🔴 Missing | Spec item not represented anywhere | Apply new edge / cell / cylinder OR escalate to design decision |

### 4. Recommend options per gap

For each 🟡/🔴 gap, present options A/B/C/D with trade-offs:

- **Option A** — Apply minimal change (label refinement)
- **Option B** — Apply structural change (new edge / cell)
- **Option C** — Defer · log as deferred design decision pending client/spec confirmation
- **Option D** — Skip · rationale documented

Each option should have explicit pros/cons. Let the user choose.

### 5. Apply chosen options + log non-applied gaps

For applied options:
- Update Mermaid + Drawio atomically (via script — see [`scripts/`](../scripts/))
- Update relevant cross-cutting docs (compliance-matrix · performance-targets · subsystem deep-dive)
- Add or revise design-decisions rows

For non-applied gaps:
- Log in subsystem doc's "Per-module audit findings" section
- Cross-reference any design-decisions rows created
- Note revisit trigger explicitly

## Coverage table example (template)

```markdown
| Spec item | Current edge/element | Status |
|---|---|---|
| **Input · sensor X feed** | Layer-level edge `HW_X → CORE` named-checks this module | ✅ Covered |
| **Input · external auth feed** | `EXT → SERVICE_LAYER` covers ingest path | ✅ Covered (group-level) |
| **Output · primary local store** | Storage exception edge `MODULE_LAYER ↔ STORE` named-checks module's schema | ✅ Covered |
| **Output · cloud sync** | Generic outbound edge to sync engine | ✅ Covered |
| **Constraint · zero outbound** | Layer-level prohibited edge to sync engine | ✅ Covered |
| **Constraint · forensic immutability** | Cross-cutting compliance matrix entry | ✅ Content |
| **Performance · ≤Ns latency** | Not yet in `performance-targets.md` | 🟡 Missing perf row |
| **Hardware · gnss-equivalent** | Edge exists for related sibling but not named for this module | 🟡 Label gap (or HWG entry) |
```

## Pattern-matched outcomes from audit

When auditing a Mobile/Core-style module, common findings:

| Finding type | Typical resolution |
|---|---|
| All touchpoints covered | No action · note "✅ fully covered" in subsystem doc |
| Missing edge label name-check | Label expansion to mention this module's data |
| Missing performance target | Add row to `performance-targets.md` |
| Hardware ambiguity | Log as HWG entry (see [hardware-gaps-tracking.md](hardware-gaps-tracking.md)) |
| Cross-layer read needed | Log as CLR entry (see [cross-layer-reads-tracking.md](cross-layer-reads-tracking.md)) |
| Storage backend conflict | Escalate to design-decisions row (Status 🔴 Blocker) |
| New mandated schema not in arch | Add cylinder (use provisional style if backend pending) |
| Prohibition not yet visible | Add red-dashed `[X] PROHIBITED` edge OR document in compliance matrix |

## Output: per-module entry in subsystem doc

After audit, append findings to `2-subsystems/<zone>-<feature>.md`:

```markdown
## Per-module audit findings

### `<Spec-ID>` <Module Name> — audited (YYYY-MM-DD)

- [ ] Inputs: <list>
- [ ] Outputs: <list>
- [ ] Capability: <read-only · write · break-glass intervention · etc.>
- [ ] Access controls: <roles · permissions>
- [ ] **Compliance constraints**: <key mandates · cross-ref to compliance matrix>
- [ ] **Architecture status** — <gap dispositions>: Gap #1 <applied via X>; Gap #2 <deferred to design-decision Y>; Gap #3 <skipped because Z>
```

## Pacing tips

- **One module per audit pass**. Don't batch.
- **Coverage table first**, options second. Resist proposing fixes before complete coverage check.
- **Pause for user decisions**. Each option set should be presented + user picks before applying.
- **Track all gaps**, even ones decided to skip. Audit trail > silent omission.
- **Repeat**: when 4+ modules in same layer have been audited, patterns become visible — may trigger new design-decision rows (e.g. defer-then-promote thresholds reached).

## Anti-patterns

- ❌ Skipping the coverage table → some spec items go unchecked silently
- ❌ Applying multiple gap fixes without user choice → bypasses architectural review
- ❌ Adding edges from spec wording without confirming the destination component exists → imaginary architecture
- ❌ Treating audit as one-shot → audits are iterative · revisit when spec amended or new module audited
