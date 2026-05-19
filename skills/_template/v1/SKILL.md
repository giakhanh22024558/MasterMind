---
name: <skill-name>
description: <skill description here>
---

# <SKILL_NAME>

(One-paragraph overview of what this skill does and why it exists.)

> Every content module in this skill is versioned at the leaf-folder level (`v1/`, `v2/`, …). Default behavior: use the highest `vN`. See [`../_meta/versioning-pattern/`](../_meta/versioning-pattern/) for the full model.

## When to use this skill

Invoke when the user asks you to:

- (List concrete triggers — what user requests should invoke this skill)
- …

## First step in any work with this skill

1. **Discover conventions** — look for `<project-root>/<skill-name>-conventions.md` per [`../_meta/conventions-as-data-pattern/`](../_meta/conventions-as-data-pattern/)
2. **Apply project conventions** where defined
3. **Fall back to** [`conventions-defaults/`](conventions-defaults/) for anything unspecified
4. **Acknowledge sources** when explaining choices

## Content modules (all versioned)

| Module | Purpose |
|---|---|
| [`conventions-schema/`](conventions-schema/) | What conventions a project must define when using this skill |
| [`conventions-defaults/`](conventions-defaults/) | Sensible defaults used when project doesn't specify |
| [`patterns/`](patterns/) | Reusable patterns for this domain |
| [`examples/`](examples/) | Worked walkthroughs |
| [`scripts/`](scripts/) | Helper scripts (if applicable) |

(Add type-specific docs as needed, e.g. `notation/`, `vocabulary/`, `severity-levels/`.)

## Workflow templates

### Workflow A · (name)

1. (step)
2. (step)
3. …

### Workflow B · (name)

…

## Anti-patterns

- ❌ (anti-pattern 1)
- ❌ (anti-pattern 2)
- …

## Cross-references to meta-patterns

| Meta-pattern | When this skill uses it |
|---|---|
| [Uniform skill structure](../_meta/uniform-skill-structure/) | This skill follows the mandatory layout |
| [Versioning pattern](../_meta/versioning-pattern/) | Every content module versioned at leaf-folder grain |
| [Conventions as data](../_meta/conventions-as-data-pattern/) | Project conventions live in `<project>/<skill-name>-conventions.md` |
| [Defer-then-promote](../_meta/defer-then-promote-pattern/) | (If applicable — when this skill tracks emerging concerns) |
| [Atomic edits](../_meta/atomic-edits-pattern/) | (If applicable — when this skill manipulates sync-prone files) |
