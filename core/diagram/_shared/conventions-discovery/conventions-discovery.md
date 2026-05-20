# Conventions discovery protocol

How the diagram skill loads a project's specific conventions (color palette, ID prefixes, spec authority codes, etc.) before applying any diagram-type sub-skill.

## Why this exists

Different projects have different conventions:
- Different color palettes
- Different ID naming schemes (`MOD-001`, `SVC-1.2.3`, `<team>-<feature>`, etc.)
- Different spec authority codes (`RFC-XXXX`, `<INTERNAL>-XXXX`)
- Different decision-ID prefixes (`M0a`, `ADR-001`, `DD-001`)
- Different edge label vocabularies

The skill must **apply the project's conventions**, not impose its own.

## Discovery protocol (in priority order)

### 1. Look for a dedicated conventions file

Check for `diagram-conventions.md` at the project root:

```
<project-root>/
├── diagram-conventions.md         ← ✅ load this first if present
├── diagrams/
└── …
```

If present, this is the **authoritative source**. Read it before any diagram work.

### 2. Check `CLAUDE.md` for a diagram section

If no dedicated file, check the project's `CLAUDE.md` (which usually holds AI-agent instructions) for a section about diagram conventions. Look for headings like:
- `## Diagram conventions`
- `## Visual style guide`
- `# Diagram Visual Style Guide`

If found, extract relevant info.

### 3. Look at existing diagrams in `diagrams/`

If no explicit conventions docs, scan existing diagrams to infer:
- What colors are used per zone purpose?
- What ID naming schemes appear?
- What edge label styles are in use?

This is **inference, not authority** — flag inferred conventions to the user for confirmation.

### 4. Ask the user

If still unclear:
- Present the diagram-type's `conventions-schema.md` (what conventions are needed)
- Ask the user to fill in or confirm defaults
- Optionally generate a starter `diagram-conventions.md` from the user's answers

### 5. Fall back to sub-skill defaults

For anything still unspecified, use the diagram-type sub-skill's `conventions-defaults.md` (e.g. `architecture/conventions-defaults.md` for an architecture diagram).

## Format of `diagram-conventions.md` (at project root)

The skill expects this file to follow the structure in [`_project-template/`](../../_project-template/). Sections per diagram type — projects fill in what they use, leave the rest blank.

Example skeleton:

```markdown
# Diagram conventions for <project name>

## General
- Decision-ID prefix scheme: `M0a–M0Z` for mobile-side, `S<n>` for system, `O<n>` for ops, …
- Spec authority codes: `<PROJECT>-<DOMAIN>-NNNN` (e.g. `ACME-MOB-5126`)
- Rejection trigger format: `RT-NN`

## Architecture diagram conventions
- Color palette per zone purpose (override defaults):
  | Zone | Fill | Stroke |
  |---|---|---|
  | Mobile · UI layer | `#bbdefb` | `#0277bd` |
  | Mobile · core safety | `#c8e6c9` | `#2e7d32` |
  | …
- Edge label rules: follow `architecture/edge-labels.md` defaults
- Storage exception scope: per `architecture/patterns/storage-exception.md`

## DFD conventions
- Process numbering: Yourdon `N.M`
- Grey-out style: per `dfd/conventions-defaults.md`
- Canvas-overlay base: `diagrams/1-overview/<project>-architecture.drawio`

## (Future: other diagram types when adopted)
```

## When project conventions disagree with skill defaults

**Project wins.** If project conventions specify a different color palette than the sub-skill default, use the project's. The skill defaults exist only as fallback for unspecified items.

## Documenting deviations

If the project intentionally deviates from a sub-skill's recommended pattern (e.g. doesn't use the storage exception · uses pure layer-level edges), capture that in `diagram-conventions.md` with a rationale. Don't make the skill silently work around it.

## When you discover conventions are missing

When you encounter a situation not covered by the project's `diagram-conventions.md` (new edge type · new component class · new audit pattern):

1. Apply your best judgment using the sub-skill defaults
2. Note the gap in your response
3. Recommend the user update `diagram-conventions.md` to capture the new convention for future consistency
4. If the deviation might recur across diagrams, suggest adding it as a row in the project's design-decisions table

This way, conventions grow organically rather than calcifying.

## Sub-skill behavior contract

Every diagram-type sub-skill MUST:

1. **Load** `diagram-conventions.md` (if present) before any drawing/auditing work
2. **Apply** project conventions where defined
3. **Fall back to defaults** (`<sub-skill>/conventions-defaults.md`) for unspecified items
4. **Acknowledge** the source (project file vs default) when explaining choices to the user
5. **Suggest updates** to `diagram-conventions.md` when discovering recurring gaps

Sub-skills must NOT:

- ❌ Hardcode project specifics
- ❌ Use defaults silently when project file exists but is incomplete (suggest filling in)
- ❌ Override project conventions with defaults (project always wins)
