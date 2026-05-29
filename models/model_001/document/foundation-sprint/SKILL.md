---
name: foundation-sprint
description: Decompose a project's cross-cutting / foundational work (the "Sprint 0" / foundation sprint) into a three-level register Topic → Concern → Task, with per-Task Acceptance Criteria (DoD). This is the foundation-phase companion to the `features` skill (Epic → Feature → User Story): same shape, renamed because foundation work serves every module and has no end-user stories. Produces a foundation register (tasks + references) plus a SEPARATE ACs file keyed by Task ID, organized by technical concern and scheduled to complete before the first delivery gate (with a pre-gate risk buffer). Use when a project needs a Sprint 0 / enablement / platform-foundation plan distinct from the business-feature backlog — architecture, infra/CI-CD, data model, auth, design system, UX guidelines, RBAC, business-rule baselines, scaffolds.
---

# foundation-sprint — Sprint 0 register (Topic → Concern → Task → ACs)

Decomposes the **cross-cutting foundation** of a project — the work that serves *every* module and is not tied to a single feature — into a three-level register, built first as **Sprint 0** ahead of the first delivery gate.

It is the deliberate twin of the [`features`](../features/) skill. Features carry end-user stories; foundation work does not, so the three levels are **renamed** to fit the phase:

| `features` (business backlog) | `foundation-sprint` (Sprint 0) | Meaning |
|---|---|---|
| Epic | **Topic** | A theme grouping related concerns |
| Feature | **Concern** | A technical concern (an area of foundation) |
| User Story | **Task** (`FND-`) | A buildable unit of foundation work |
| Acceptance Criteria | **ACs** | Verifiable done-criteria (DoD) per Task |

Follows the [Core Rule](../../../../core/core-rule/): the register is the source of truth; ACs live in a separate companion file (the foundation analog of the separate AC sheet).

## When to use this skill

Invoke when the user asks to:
- Plan a **Sprint 0 / foundation sprint / enablement sprint / platform sprint** — the run-up to the first delivery gate.
- Separate **cross-cutting / foundational concerns** (architecture, infra, data model, auth, design system, business rules, scaffolds) from the **business-feature backlog**.
- Organize foundation work **by technical concern** and give each task **Definition-of-Done** criteria.

Do **not** use it for business-functional features → use [`features`](../features/). Foundation tasks are enablers; features are end-user capabilities.

## First step in any task

1. **Confirm the split** — business-functional capabilities go to [`features`](../features/) (Epic→Feature→US); cross-cutting foundations come here (Topic→Concern→Task). Standards/criteria (thresholds, rules, accessibility levels) become **ACs**, never tasks. See [`patterns/business-vs-foundation-split.md`](patterns/business-vs-foundation-split.md).
2. **Discover conventions** — read `<project-root>/foundation-sprint-conventions.md` per [`conventions-as-data-pattern`](../../../../core/meta/conventions-as-data-pattern/); fall back to [`conventions-defaults/`](conventions-defaults/) (which ships a default 10-concern catalogue).

## Workflow

1. **List the concerns** — pick from the default concern catalogue ([`conventions-defaults/`](conventions-defaults/)) the ones the project needs; add project-specific concerns.
2. **Group concerns into Topics** — cluster related concerns into a handful of Topics (`TOPIC-NN`). See [`patterns/topic-grouping.md`](patterns/topic-grouping.md).
3. **Decompose each Concern into Tasks** — assign `FND-NNN`. One task = one buildable enabler. Reference the governing source doc(s) per task.
4. **Write ACs per Task** — verifiable done-criteria, in the project's AC language. Put them in the **separate ACs file** keyed by Task ID (`AC-FND-{task}-{nn}`), not inline in the register.
5. **Schedule before the first gate** — sequence the build so the foundation completes ~15 days before the gate (risk buffer), running concerns in parallel across available tracks. See [`patterns/gate-buffer-and-parallelisation.md`](patterns/gate-buffer-and-parallelisation.md).
6. **Render** — register (Topic→Concern→Task + Reference) as the source of truth; the ACs file as a sidecar; both live in the project's planning doc / `docs/`.

See [`foundation-register/`](foundation-register/) for the canonical structure spec. **Read it before producing a register.**

## Content modules

| Module | Purpose |
|---|---|
| [`foundation-register/`](foundation-register/) | The canonical Topic → Concern → Task structure, IDs, the separate-ACs rule |
| [`conventions-schema/`](conventions-schema/) | What a project declares (concern catalogue, ID formats, AC language, gate buffer) |
| [`conventions-defaults/`](conventions-defaults/) | Defaults — incl. the default 10-concern catalogue |
| [`patterns/`](patterns/) | Topic grouping · business-vs-foundation split · gate buffer & parallelisation |
| [`examples/`](examples/) | Worked walkthrough |
| [`scripts/`](scripts/) | Rendering helpers |

## Core principles

- **Topic → Concern → Task** — every concern sits in a topic; every task sits in a concern; every task carries ACs.
- **Everything has a code** — `TOPIC-NN`, `FND-NNN`, `AC-FND-{task}-{nn}` — sequential, never reused.
- **Foundation ≠ features** — enablers, not end-user capabilities. Standards become ACs, not tasks.
- **ACs live separately** — register holds Task + Reference; ACs in a companion file keyed by Task ID.
- **Foundation goes first** — Sprint 0, completing before the first gate with a pre-gate buffer; concerns run in parallel.
- **Reference by code** — each task cites its governing source doc(s) by code/section.

## Anti-patterns

- ❌ Putting a business-functional feature here (it belongs in [`features`](../features/)).
- ❌ Turning a standard / threshold / rule into a Task (it's an **AC** of a task — e.g. "WCAG 2.1 AA", "≤8%/hr battery", a prohibited-list).
- ❌ Inlining ACs in the register (keep them in the separate ACs file).
- ❌ A Concern with no Topic, or a Task with no Concern.
- ❌ Hand-assigning `FND-`/`TOPIC-` codes out of order, or reusing codes.
- ❌ Scheduling foundation tasks to finish *at* the gate (leave the risk buffer).

## Cross-references

| Reference | Used for |
|---|---|
| [`features`](../features/) | The business-feature backlog (Epic→Feature→US) — the twin skill |
| [Core Rule](../../../../core/core-rule/) | Register = source of truth; ACs sidecar |
| [Conventions as data](../../../../core/meta/conventions-as-data-pattern/) | Concern catalogue + ID formats + AC language in `<project>/foundation-sprint-conventions.md` |
| [`business_analysis` pipeline](../../business_analysis/) | Where the foundation sprint precedes the feature build |
