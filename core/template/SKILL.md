---
name: <skill-name>
description: <skill description here>
---

# <SKILL_NAME>

(One-paragraph overview of what this skill does and why it exists.)

## When to use this skill

Invoke when the user asks you to:

- (List concrete triggers — what user requests should invoke this skill)
- …

## First step in any work with this skill

1. **Discover conventions** — look for `<project-root>/<skill-name>-conventions.md` per [`meta/conventions-as-data-pattern/`](../meta/conventions-as-data-pattern/)
2. **Apply project conventions** where defined
3. **Fall back to** [`conventions-defaults/`](conventions-defaults/) for anything unspecified
4. **Acknowledge sources** when explaining choices

## Content modules

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
| [Uniform skill structure](../meta/uniform-skill-structure/) | This skill follows the mandatory layout |
| [Conventions as data](../meta/conventions-as-data-pattern/) | Project conventions live in `<project>/<skill-name>-conventions.md` |
| [Defer-then-promote](../meta/defer-then-promote-pattern/) | (If applicable — when this skill tracks emerging concerns) |
| [Atomic edits](../meta/atomic-edits-pattern/) | (If applicable — when this skill manipulates sync-prone files) |
