---
name: diagram/erd
description: Build Entity-Relationship Diagrams (ERD) — entities and the relationships between them, in crow's-foot notation. Authored as Mermaid inside a .md context file; rendered to .drawio only on explicit request. Use to model a system's data structure, surface edge cases and business rules, and explain how parts of the system relate.
---

# ERD diagram sub-skill

For **Entity-Relationship Diagrams** — the entities of a system and the relationships connecting them, drawn with **crow's-foot** cardinality notation.

## When to use this sub-skill

Invoke when the user asks you to:

- **Model** a system's entities and the relationships between them
- **Surface edge cases and business rules** from relationship cardinalities
- **Explain** to a stakeholder how a change in one entity ripples to connected entities

For master architecture (C4) diagrams, use the `architecture` sub-skill. For cross-diagram methodology (conventions discovery, atomic edits), see [`core/diagram/_shared/`](../../../../core/diagram/_shared/).

## First step in any ERD work

1. **Discover conventions** — read `<project-root>/diagram-conventions.md` per [`conventions-discovery`](../../../../core/diagram/_shared/conventions-discovery/); fall back to [`conventions-defaults/`](conventions-defaults/).
2. **Work from the requirements** — an ERD is **derived from analyzed requirements**, not invented. Within the [business_analysis pipeline](../../business_analysis/) the ERD is built from the requirements table.

## Content modules

| Module | Purpose |
|---|---|
| [`conventions-schema/`](conventions-schema/) | What an ERD convention must define (entity naming, notation, file name) |
| [`conventions-defaults/`](conventions-defaults/) | Defaults used when the project doesn't specify |
| [`erd-notation/`](erd-notation/) | Crow's-foot notation, the Mermaid form, when to render `.drawio` |
| [`patterns/`](patterns/) | Reusable patterns |
| [`examples/`](examples/) | Worked walkthrough |
| [`scripts/`](scripts/) | Helper scripts |

## Workflow

### Workflow A · Draft an ERD

1. **Identify entities** from the source content — every entity should trace to a requirement.
2. **Draw relationships** between entities, choosing crow's-foot cardinality (see [`erd-notation/`](erd-notation/)).
3. **Author as Mermaid** — an `erDiagram` block inside a `.md` context file.
4. **Render to `.drawio`** into `output/` **only when the user explicitly asks** — use the atomic-edit scripts in [`core/diagram/_shared/scripts/`](../../../../core/diagram/_shared/scripts/). The Mermaid `.md` stays the source of truth.

### Workflow B · Audit an ERD for edge cases

1. Walk each relationship's cardinality (especially `zero-or-many`).
2. For each, ask "what happens at the boundary?" — surface the case to the user as a question or a business rule.

## Anti-patterns

- ❌ Rendering the ERD to `.drawio` without an explicit request — Mermaid `.md` is the default.
- ❌ Inventing entities the requirements don't support — raise a question instead.
- ❌ Hand-editing the `.drawio` as the master — re-render from the Mermaid `.md`.

## Cross-references

| Reference | Used for |
|---|---|
| [Core Rule](../../../../core/core-rule/) | `.md`/Mermaid is the agent layer; `.drawio` is the user layer |
| [`core/diagram/_shared/`](../../../../core/diagram/_shared/) | Conventions discovery, atomic edits, shared Drawio scripts |
| [business_analysis pipeline](../../business_analysis/) | The pipeline that feeds requirements into the ERD |
