# foundation-sprint · conventions defaults

Defaults applied when `<project-root>/foundation-sprint-conventions.md` does not specify a value. (Meta-pattern: [`conventions-as-data-pattern`](../../../../../core/meta/conventions-as-data-pattern/).)

## Overridable defaults

| Item | Default |
|---|---|
| Topic code | `TOPIC-` + 2 digits, sequential from `TOPIC-01`, in build/priority order |
| Task code | `FND-` + 3 digits, sequential from `FND-001`, build order, never reused |
| AC code | `AC-FND-{task}-{nn}` (e.g. `AC-FND-001-01`) |
| AC language | `en` — Definition-of-Done criteria; set `vi` for Vietnamese |
| Register file | the project planning doc (e.g. `docs/planning.md` §Sprint-0 register) |
| ACs file | a separate sidecar (e.g. `docs/sprint-0-acs.md`) |
| Pre-gate risk buffer | **~15 days** before the first delivery gate (see [`../patterns/gate-buffer-and-parallelisation.md`](../patterns/gate-buffer-and-parallelisation.md)) |

## Default concern catalogue (10)

A sensible cross-cutting catalogue for a mobile/web product foundation. Projects pick the relevant subset, rename, or add their own. The grouping into Topics is illustrative — a project re-groups freely.

| # | Concern | Typical Tasks |
|---|---|---|
| 1 | **Architecture & Technical Design** | system/layer architecture · component boundaries · ADRs · key architecture-artefact docs |
| 2 | **Infrastructure & CI/CD** | repo + build pipeline · static-analysis/compliance CI · gate-evidence packaging · SDK/OSS audit |
| 3 | **Foundational Data Model & Persistence** | core data store · cloud-isolation barrier · data classification · sync · encryption |
| 4 | **Connectivity / Comms Abstraction** | connectivity state schema · detection/degraded-state · status indicators |
| 5 | **Authentication & RBAC** | app identity · admin auth · roles + permission matrix |
| 6 | **Rendering / Map / Media Foundation** | rendering pipeline · offline assets · provider abstraction · overlay/compositing framework |
| 7 | **Design System, App Shell & UX Guidelines** | component library · app shell/navigation chrome · placeholders · accessibility baseline · UX-guideline harness |
| 8 | **Business Rules & Compliance Baseline** | deterministic rule-set · prohibited-X registers · posture enforcement · rejection/rollback registers · phase-boundary discipline |
| 9 | **Phase-N Inert Scaffolds** | versioned inert schemas · feature flags locked off · non-executable forward pathways |
| 10 | **Public Presence** | companion/marketing website · public legal pages |

## Default Topic grouping (illustrative)

| Topic | Concerns |
|---|---|
| TOPIC-01 — Architecture & Delivery Platform | 1, 2 |
| TOPIC-02 — Data, Connectivity & Identity Core | 3, 4, 5 |
| TOPIC-03 — Experience Foundation | 6, 7 |
| TOPIC-04 — Compliance & Phase Governance | 8, 9 |
| TOPIC-05 — Public Presence | 10 |

## When defaults apply

Each item the project does not declare takes the value here. The skill **acknowledges the source** when explaining a choice ("per project conventions" / "using default").

## See also

- [`../foundation-register/foundation-register.md`](../foundation-register/foundation-register.md) — the canonical structure
- [`conventions-schema.md` is in `../conventions-schema/`](../conventions-schema/conventions-schema.md) — what a project declares
