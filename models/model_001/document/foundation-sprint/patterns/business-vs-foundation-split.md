# Pattern — business-vs-foundation split

The decision rule for **where a piece of work goes**: the business-feature backlog ([`features`](../../features/)), the foundation register (this skill), or neither (it's an AC).

## The three buckets

| Bucket | Goes to | Test |
|---|---|---|
| **Business-functional capability** | `features` — Epic→Feature→US | Does an end user / operator *do* something with it? (navigate, submit, view, administer) |
| **Cross-cutting foundation** | `foundation-sprint` — Topic→Concern→Task | Does it serve *every* module and enable feature work? (architecture, infra, data, auth, design system, rules, scaffolds) |
| **Standard / criterion / rule** | an **AC** on the relevant task or feature | Is it a threshold, level, prohibited-list, or invariant that something must *satisfy*? (a battery %, an accessibility level, a "must not" list) |

## Worked examples

| Item | Bucket | Why |
|---|---|---|
| "User can submit a condition report" | Feature | end-user capability |
| "Local-only data store + cloud-isolation barrier" | Foundation Task | platform substrate every module uses |
| "Design system / component library" | Foundation Task | shared UI substrate |
| "Auth + role/permission matrix" | Foundation Task | cross-cutting identity |
| "WCAG 2.1 AA" | AC | a standard UI features must satisfy |
| "≤8%/hr battery in active nav" | AC | a threshold the app must meet |
| "14 prohibited data mutations" | Foundation Task (build the *register/guard*) **+** AC (assert it on the data-write feature) | the guardrail is foundation; the conformance is an AC |
| "Companion website live" | Foundation Task | public-facing enablement deliverable, not an in-app feature |

## Rule of thumb

- If removing it would **break many features at once** → foundation.
- If it's something a feature must **pass/comply with** → AC.
- If a single user-facing flow → feature.

## Anti-patterns

- ❌ A standard masquerading as a task ("Task: WCAG 2.1 AA"). Build the *baseline/harness* as a task; assert the *level* as an AC.
- ❌ Foundation tasks leaking into the feature backlog (bloats it, distorts feature priority).
- ❌ An end-user capability hidden as a "foundation task".
