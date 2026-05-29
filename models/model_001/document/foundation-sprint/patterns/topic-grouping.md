# Pattern — grouping concerns into Topics

How to cluster the technical **Concerns** into a handful of **Topics** (the Epic-analog level).

## Goal

A 2:1–3:1 grouping — e.g. 10 concerns → 4–5 topics. Few enough that the foundation reads at a glance; coherent enough that each topic is a real theme.

## Grouping heuristics

Group concerns that share **one of**:
- **A layer** — e.g. "Architecture + Infra/CI-CD" = the engineering platform.
- **A substrate** — e.g. "Data + Connectivity + Auth" = the backend/platform core.
- **A surface** — e.g. "Rendering + Design system/UX" = the experience foundation.
- **A governance role** — e.g. "Business rules + Phase scaffolds" = compliance & phase discipline.
- **An audience** — e.g. "Public website" = public presence.

## Reference grouping (from the default 10-concern catalogue)

| Topic | Concerns | Theme |
|---|---|---|
| TOPIC-01 — Architecture & Delivery Platform | Architecture · Infra/CI-CD | how it's structured + built/shipped |
| TOPIC-02 — Data, Connectivity & Identity Core | Data Model · Connectivity · Auth/RBAC | the platform substrate |
| TOPIC-03 — Experience Foundation | Rendering/Map · Design System/UX | the surface every screen builds on |
| TOPIC-04 — Compliance & Phase Governance | Business Rules · Phase Scaffolds | guardrails + phase discipline |
| TOPIC-05 — Public Presence | Companion Website | public-facing deliverable |

## Ordering

Order Topics in **build order** (foundational-most first), then number `TOPIC-01…NN`. The same priority-ordered-ID idea as the `features` backlog (lower ID = earlier/foundational). A single-concern Topic is fine (analog of an Epic with one Feature) when the concern is a distinct theme (e.g. public website).

## Anti-patterns

- ❌ One Topic per Concern (defeats the grouping — you just renamed concerns).
- ❌ A mega-Topic holding everything (no signal).
- ❌ Grouping by spec document rather than by engineering theme.
