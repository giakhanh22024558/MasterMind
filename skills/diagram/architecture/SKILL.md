---
name: diagram/architecture
description: Build, audit, and maintain master architecture diagrams (C4-style). Use for system landscape, zone boundaries, layer-level vs component-level edges, storage relationships, deferred-decision tracking (cross-layer reads, hardware access gaps). Loads project conventions from `<project-root>/diagram-conventions.md` and applies them; falls back to sub-skill defaults.
---

# Architecture diagram sub-skill

For master architecture diagrams in the C4 style — system landscape, zones, components, the edges connecting them, and the conventions governing their visualization.

## When to use this sub-skill

Invoke when the user asks you to:

- **Draft** or **extend** a master architecture diagram (C4-style)
- **Audit a module against its spec** — verify the diagram covers what the spec mandates
- Add **architecture-level edges** between zones/components
- **Refine edge labels** (verb form · reference-ID + characterization)
- Decide **layer-level vs component-level** edge granularity
- Apply the **storage exception** pattern
- Set up **deferred-decision tracking** (cross-layer reads, hardware access gaps)

For Data Flow Diagrams, use the `dfd/` sub-skill instead. For cross-diagram methodology (folder structure, design-decisions, atomic edits), see `_shared/`.

## First step in any architecture work

1. **Discover conventions** — read `<project-root>/diagram-conventions.md` per [`../_shared/conventions-discovery.md`](../_shared/conventions-discovery.md)
2. **Apply project conventions** where defined
3. **Fall back to** [`conventions-defaults.md`](conventions-defaults.md) for anything unspecified
4. **Acknowledge sources** when explaining choices to the user

## Sub-skill contents

| File | Purpose |
|---|---|
| [`conventions-schema.md`](conventions-schema.md) | What an architecture-diagram convention must define (used as checklist when reading project file or asking user) |
| [`conventions-defaults.md`](conventions-defaults.md) | Sensible defaults used when project doesn't specify |
| [`edge-labels.md`](edge-labels.md) | Architecture-specific edge label rules (verb form for operational · noun for data-payload · prohibited path format) |
| [`patterns/storage-exception.md`](patterns/storage-exception.md) | Hybrid edge granularity — layer-level default + component-level for storage cells |
| [`patterns/cross-layer-reads-tracking.md`](patterns/cross-layer-reads-tracking.md) | Defer-then-promote tracking for "Layer A reads Layer B" exceptions |
| [`patterns/hardware-gaps-tracking.md`](patterns/hardware-gaps-tracking.md) | Defer-then-resolve tracking for hardware access ambiguities |
| [`examples/audit-workflow-example.md`](examples/audit-workflow-example.md) | Worked walkthrough using generic placeholders |
| [`scripts/`](scripts/) | Architecture-specific scripts (if any beyond `_shared/scripts/`) |

## Workflow templates

### Workflow A · Spec-driven audit (architecture context)

When a user provides a module spec for a system that has an architecture diagram:

1. **Load** project conventions (from `<project-root>/diagram-conventions.md`)
2. **Read spec** — extract every input, output, storage target, constraint, mandate
3. **Build coverage table** (spec item → current edge/element → status)
4. **Classify gaps** (covered ✅ · partial 🟡 · missing 🔴)
5. **Recommend options** per gap (A/B/C/D with trade-offs)
6. **Apply** chosen + **log** non-applied as deferred design decisions

Use [`../_shared/spec-driven-audit.md`](../_shared/spec-driven-audit.md) for the general workflow + this sub-skill's patterns for resolution options.

### Workflow B · Adding an architecture edge

1. **Decide granularity** — layer-level (default) or component-level (storage exception only — see [`patterns/storage-exception.md`](patterns/storage-exception.md))
2. **Pick label form** — verb for operational, noun for data-payload (per [`edge-labels.md`](edge-labels.md))
3. **Add reference-ID + characterization** if citing a design-decision/spec (per [`../_shared/edge-labels-general.md`](../_shared/edge-labels-general.md))
4. **Update both Mermaid + Drawio atomically** — use scripts from [`../_shared/scripts/`](../_shared/scripts/)
5. **Log design decision** if architectural significance is non-trivial (per [`../_shared/design-decisions-format.md`](../_shared/design-decisions-format.md))

### Workflow C · Apply storage exception

When you need to add an edge involving a storage cell:

1. Confirm one endpoint is in a storage zone
2. Render at component level (not layer level)
3. Use bidirectional `<-->` for R/W, unidirectional for read-only or write-only
4. Label per architecture/edge-labels.md
5. Document in design-decisions if extending storage exception scope

See [`patterns/storage-exception.md`](patterns/storage-exception.md).

## Anti-patterns

- ❌ Drawing edges from spec wording without confirming destinations → imaginary architecture
- ❌ Skipping coverage table in audit → silent omissions
- ❌ Applying gap fixes without user choice → bypasses architectural review
- ❌ Component-level edges everywhere → defeats layer-level hybrid
- ❌ Using sub-skill defaults when project file specifies different conventions → project always wins
