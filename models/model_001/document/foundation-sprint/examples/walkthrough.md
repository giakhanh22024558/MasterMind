# Walkthrough — a foundation sprint (survival-grade mobile product)

A condensed worked example showing the skill end-to-end. (Modelled on a real engagement: a Flutter offline-first product with a fixed launch gate.)

## 0. Context

- 4 client gates: **Discovery → Alpha → Beta-Ready → GA**.
- A business-feature backlog already exists (`features` skill: Epic→Feature→US).
- We need a **Sprint 0** for the cross-cutting foundation, completing before the Discovery gate.

## 1. Split (business-vs-foundation)

Per [`../patterns/business-vs-foundation-split.md`](../patterns/business-vs-foundation-split.md): navigation/SOS/messaging → `features`. Architecture, data store, auth, design system, business-rule registers, inert scaffolds, public site → **foundation**. WCAG level, battery %, prohibited-lists → **ACs**.

## 2. Concerns + Topics

Picked all 10 default concerns; grouped into 5 Topics (per [`../patterns/topic-grouping.md`](../patterns/topic-grouping.md)):

| Topic | Concerns |
|---|---|
| TOPIC-01 Architecture & Delivery Platform | Architecture · Infra/CI-CD |
| TOPIC-02 Data, Connectivity & Identity Core | Data Model · CAL · Auth/RBAC |
| TOPIC-03 Experience Foundation | Map/Overlay · Design System/UX |
| TOPIC-04 Compliance & Phase Governance | Business Rules · Phase-2 Scaffolds |
| TOPIC-05 Public Presence | Companion Website |

## 3. Tasks (register excerpt)

```
### TOPIC-02 — Data, Connectivity & Identity Core
#### Concern 3 — Foundational Data Model & Persistence  (refs: data-governance spec · architecture spec)
| Task | Reference |
|---|---|
| **FND-010 — Local-only core store** (SQLite + WAL · cloud-independent) | DataGov §3 · Arch §6 |
| **FND-011 — Cloud isolation barrier** | DataGov (isolation) |
| **FND-012 🎯 — Data classification + enforcement** — D5 deliverable | DataGov §3–4 |
```

44 tasks total · `FND-001…044` · 🎯 = committed Discovery deliverable.

## 4. ACs (separate file excerpt)

```
#### Concern 3 — Foundational Data Model & Persistence
| Task | AC ID | Acceptance Criterion (DoD) |
|---|---|---|
| FND-010 Local-only core store | AC-FND-010-01 | Store operational fully offline |
|  | AC-FND-010-02 | No cloud dependency in any core write path |
|  | AC-FND-010-03 | Crash-survivable via WAL replay |
```

~3 ACs/task · `AC-FND-{task}-{nn}` · kept in a **separate** ACs file (register stays Task+Reference).

## 5. Schedule (gate buffer + parallelisation)

Per [`../patterns/gate-buffer-and-parallelisation.md`](../patterns/gate-buffer-and-parallelisation.md):

- Discovery window was short (contract → gate ≈ 17 days) → **constrained**: foundation-complete ~5 days before the gate, with a stated mitigation (all 10 concerns parallel from day 1 across 8 tracks).
- Committed gate deliverables (the artefacts the client accepts) mapped to specific 🎯 tasks, scheduled to finish first.
- Later gates (Alpha/Beta) used the full ~15-day buffer with a dedicated stabilisation sprint each.

## Result

- One **register** (Topic→Concern→Task + Reference) — the source of truth.
- One **ACs sidecar** keyed by Task ID.
- A **Gantt** with gate milestones, freeze milestones, build sprints, buffer sprints, and one track per concern.
- Clean separation from the business-feature backlog, which builds *on top of* the foundation after Discovery.
