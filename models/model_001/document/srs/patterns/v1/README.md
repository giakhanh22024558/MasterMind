# model_001_srs · patterns

Reusable patterns for SRS document generation.

## Available patterns

| Pattern | Purpose |
|---|---|
| [`content-format-separation.md`](content-format-separation.md) | Separate content (`.md`) from presentation (Python); this also enables the auto-generated conventions (ID codes, figure numbers, numbering) |

## How to add a new pattern

1. Create `<pattern-name>.md` in this folder
2. Follow the structure: **Problem → Solution → Trade-offs → Worked example → When NOT to use → Cross-references**
3. If the pattern is an instantiation of a [meta-pattern](../../../../../../core/meta/), reference back to the meta-pattern instead of repeating it

## When to promote a pattern to `meta/`

If a pattern appears in 3+ skills → it is no longer skill-specific. Promote it to [`meta/`](../../../../../../core/meta/) per the [defer-then-promote pattern](../../../../../../core/meta/defer-then-promote-pattern/).
