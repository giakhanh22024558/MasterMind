# Defer-then-promote pattern (abstract)

A general structural tracking pattern for emerging architectural concerns. **Don't commit to a structural change after seeing one or two cases. Accumulate evidence, then promote to canonical doc + diagram once a threshold is crossed.**

## When to apply

Use this pattern whenever you encounter a recurring architectural concern that's:
- **Real** (not speculation) — backed by spec or design audit
- **Repeating** — same shape appears across multiple modules/features
- **Not yet structural** — single occurrence wouldn't justify a top-level diagram change

Examples (instantiated in specific tracking patterns):
- **Cross-layer reads** — Layer A reads Layer B's published data via "limited surfaces" exception
- **Hardware access gaps** — features that need hardware not yet modeled in architecture
- **Cross-zone privileged operations** — admin actions touching protected stores
- **Compliance exceptions** — narrowly-scoped allowances to a strict default

Each instance becomes a domain-specific tracking pattern (CLR, HWG, …) but follows the same lifecycle.

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
                                                    │    diagram edge       │
                                                    └───────────────────────┘
```

### Step 1 · Discover surface

A spec audit (or design review) reveals a relationship/dependency not yet modeled. Identify:
- **What is it?** (the architectural fact)
- **Why is it not already modeled?** (e.g., exception to default, fine-grained, rare)
- **What's the source spec?** (audit trail)

### Step 2 · Log locally (subsystem doc)

Add an entry to the relevant subsystem doc's "Known <pattern> surfaces" section. Use a consistent ID scheme (e.g. `CLR-01`, `HWG-02`).

Each entry captures:
- ID
- Spec/source identifier
- Description of the surface (what reads what, what depends on what)
- Resolution options (α / β / γ) with trade-offs
- Status (confirmed · pending spec clarification · candidate)

### Step 3 · Threshold check

Define a numeric threshold for promotion (typical: **N = 3 confirmed surfaces**). Below the threshold, surfaces stay logged locally. At or above, promote.

Rationale for N=3:
- N=1 — could be a one-off exception, not a pattern
- N=2 — could still be coincidence
- N=3 — clearly a recurring structural concern

Adjust N per project domain · document the choice in the design-decisions table.

### Step 4 · Promote or keep deferred

If count < N: keep tracking in subsystem doc. Add new entries as more audits reveal surfaces.

If count ≥ N: trigger promotion (next step).

### Step 5 · Canonical doc + diagram edge

Promotion actions:

1. **Create canonical doc** in `diagrams/4-cross-cutting/<pattern-name>.md` listing all known surfaces
2. **Move table** from subsystem doc to cross-cutting doc
3. **Add architecture edge** (aggregated or per-surface, depending on visual impact)
4. **Update design-decisions row** for this pattern: status `🟡 Provisional (N/3 confirmed)` → `🟢 Codified`
5. **Update README** navigation map

## How to structure a pattern-specific tracking

Each instantiation should specify:

| Element | Example (CLR pattern) |
|---|---|
| Pattern name | Cross-Layer Reads |
| ID prefix | CLR-XX |
| Resolution options | α direct access · β cross-layer read · γ skip |
| Threshold (N) | 3 confirmed surfaces |
| Promotion target | `4-cross-cutting/cross-layer-reads.md` |
| Architecture edge format | Aggregated edge with surfaces named in label, OR per-surface edges |
| Design-decisions row | `V5` (or similar visual-convention category) |

See [`architecture/patterns/cross-layer-reads-tracking.md`](../architecture/patterns/cross-layer-reads-tracking.md) and [`architecture/patterns/hardware-gaps-tracking.md`](../architecture/patterns/hardware-gaps-tracking.md) for concrete instantiations.

## Why the pattern works

- **Avoids premature commit** — diagram doesn't churn on 1–2 outliers
- **Preserves audit trail** — every surface logged, never silent
- **Explicit promotion trigger** — count-based, removes subjective "is it time?"
- **Reusable across concern types** — same shape applies to many domains (CLR, HWG, compliance exceptions, etc.)

## When NOT to use this pattern

- **One-off integration** — single special case, no expectation of recurrence → just document inline
- **Spec-mandated mass change** — spec says "every module must X" → apply broadly immediately
- **Critical compliance** — security/safety issue can't wait for accumulation → escalate immediately

## How to introduce a new pattern instantiation

When you encounter a new emerging concern (not CLR, not HWG), create a new tracking pattern:

1. Pick an ID prefix (3-letter abbreviation: e.g. `OCR` for OCS-Cloud-Read)
2. Define resolution options (α/β/γ)
3. Choose threshold (typically 3)
4. Identify promotion target (which `4-cross-cutting/` doc)
5. Add tracking section to relevant subsystem doc
6. Add design-decisions row codifying the deferral policy

Document the new pattern in a `<sub-skill>/patterns/<pattern-name>-tracking.md` file following the existing examples' shape.
