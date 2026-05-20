# Defer-then-promote pattern (general)

A pattern for handling **emerging architectural concerns** that may or may not warrant structural commits to a skill or project artifact. Apply when you see a recurring issue but aren't yet sure whether it deserves first-class representation.

## The principle

Don't commit to a structural change after seeing one or two cases. **Accumulate evidence locally, then promote to canonical doc + structural change once a threshold is crossed.**

## When to apply

Use whenever you encounter a recurring concern that's:

- **Real** (backed by spec, design review, or observed pattern)
- **Repeating** — same shape appears across multiple modules/features/projects
- **Not yet structural** — single occurrence wouldn't justify a top-level change

Examples (instantiated as specific tracking patterns in skills):

- **Cross-layer reads** (diagram skill) — App reads Core data via "limited surfaces"
- **Hardware access gaps** (diagram skill) — features need hardware not modeled in architecture
- **Cross-zone privileged operations** (any system) — admin actions touching protected resources
- **Compliance exceptions** (any project) — narrowly-scoped allowances to a strict default
- **Recurring code review issues** (code_review skill) — patterns of feedback across many reviews
- **Common stakeholder ask** (business_analysis skill) — same question asked by multiple stakeholders

Each instance becomes a domain-specific tracking pattern with its own ID prefix and resolution options, but follows the same lifecycle.

## The lifecycle

```
┌─────────────────────┐    ┌──────────────────────┐    ┌────────────────────┐
│ 1. Discover surface │ ─▶ │ 2. Log locally       │ ─▶ │ 3. Threshold check │
└─────────────────────┘    └──────────────────────┘    └────────────────────┘
                                                                │
                                                                ▼
                                                    ┌───────────────────────┐
                                                    │ 4. Promote (≥N) OR    │
                                                    │    keep deferred (<N) │
                                                    └───────────────────────┘
                                                                │
                                                                ▼
                                                    ┌───────────────────────┐
                                                    │ 5. Canonical doc +    │
                                                    │    structural change  │
                                                    └───────────────────────┘
```

### Step 1 · Discover surface

A spec audit, design review, or user observation reveals a concern not yet modeled. Identify:

- **What is it?** (the architectural / process fact)
- **Why is it not already modeled?** (e.g., exception to default, fine-grained, rare)
- **What's the source?** (audit trail)

### Step 2 · Log locally

Add an entry to the relevant subsystem doc's "Known <pattern> surfaces" section. Use a consistent ID scheme (e.g. `CLR-01`, `HWG-02`, `OCR-03`).

Each entry captures:
- ID
- Source identifier (spec ID, review ID, ticket, etc.)
- Description of the surface
- Resolution options (α / β / γ) with trade-offs
- Status (confirmed · pending · candidate)

### Step 3 · Threshold check

Define a numeric threshold for promotion. **Typical default: N = 3 confirmed surfaces.**

Below threshold: surfaces stay logged locally. At or above: promote.

Rationale for N=3:
- N=1 — could be a one-off exception, not a pattern
- N=2 — could still be coincidence
- N=3 — clearly recurring

Adjust N per domain · document in design-decisions table.

### Step 4 · Promote or keep deferred

If count < N: keep tracking in subsystem doc. Add new entries as more cases found.

If count ≥ N: trigger promotion.

### Step 5 · Canonical doc + structural change

Promotion actions:

1. **Create canonical doc** in `<skill>/4-cross-cutting/<pattern-name>.md` (or equivalent location) listing all known surfaces
2. **Move table** from subsystem doc to cross-cutting doc
3. **Add structural element** (architecture edge · UI component · process step · whatever the skill works with)
4. **Update design-decisions row** for this pattern: `🟡 Provisional (N/3)` → `🟢 Codified`
5. **Update README** navigation

## Pattern-specific instantiation template

Each instantiation should specify:

| Element | Example |
|---|---|
| Pattern name | Cross-Layer Reads |
| ID prefix | CLR-XX |
| Resolution options | α (direct) · β (cross-layer) · γ (skip) |
| Threshold (N) | 3 confirmed surfaces |
| Promotion target | `<skill>/4-cross-cutting/<pattern>.md` |
| Structural change format | Aggregated edge with surfaces named, OR per-surface edges |
| Design-decisions row | `V5` (visual convention category) |

## Why it works

- **Avoids premature commit** — diagrams/processes don't churn on outliers
- **Preserves audit trail** — every surface logged, never silent
- **Explicit promotion trigger** — count-based, removes subjective "is it time?"
- **Reusable across domains** — same shape applies to many concern types

## When NOT to use this pattern

- **One-off integration** — single special case, no expectation of recurrence → just document inline
- **Spec-mandated mass change** — spec says "every module must X" → apply broadly immediately
- **Critical compliance** — security/safety issue can't wait for accumulation → escalate immediately

## Introducing a new pattern instantiation

When you encounter a new emerging concern in your skill domain:

1. Pick an ID prefix (3-letter abbreviation, e.g. `OCR` for OCS-Cloud-Read)
2. Define resolution options (α/β/γ)
3. Choose threshold (typically 3)
4. Identify promotion target
5. Add tracking section to relevant subsystem doc
6. Add design-decisions row codifying the deferral policy
7. Document the new pattern in `<skill>/patterns/v1/<pattern-name>-tracking.md`

## Cross-references in skills

Different skills will reference this pattern from their domain-specific patterns. Examples:

- `diagram/architecture/patterns/v1/cross-layer-reads-tracking.md` (instantiates this pattern for CLR)
- `diagram/architecture/patterns/v1/hardware-gaps-tracking.md` (instantiates for HWG)

When writing your skill's tracking pattern, **reference back to this meta-pattern** instead of re-explaining the general lifecycle:

```markdown
This is an instantiation of the [defer-then-promote pattern](../../../meta/defer-then-promote-pattern/).
Specifics for our domain: ...
```
