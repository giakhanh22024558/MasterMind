# <skill-name> · conventions schema

The checklist of what conventions a project must define when using this skill. Projects fill in this schema (typically in `<project-root>/<skill-name>-conventions.md`); unspecified items fall back to [`conventions-defaults/`](../conventions-defaults/).

(For the meta-pattern, see [`meta/conventions-as-data-pattern/`](../../meta/conventions-as-data-pattern/).)

## Required conventions

### 1 · (Convention category)

For each item, the project should specify a value or accept the default.

| Item | Format | Default | Example |
|---|---|---|---|
| (item) | (regex / enum / table) | (cross-ref defaults) | (sample) |
| … | | | |

### 2 · (Convention category)

…

### N · (Convention category)

…

## Optional conventions

Conventions that may not apply to every project:

- (Optional item · when to define)
- …

## Checklist (for skill agent)

When loading a project's conventions file for the first time:

- [ ] (item 1 resolved)
- [ ] (item 2 resolved)
- [ ] …

If any item is undefined and not optional, **ask the user** before proceeding.
