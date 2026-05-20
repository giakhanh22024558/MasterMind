# Meta-skill — README

How to create any new skill in this repo · the mindset, structure, and patterns that every skill follows.

## Quick start

| If you want to… | Read |
|---|---|
| Understand the meta-skill in one page | [`SKILL.md`](SKILL.md) |
| Walk through creating a new skill step-by-step | [`skill-creation-guide/`](skill-creation-guide/) |
| Learn the mandatory folder structure | [`uniform-skill-structure/`](uniform-skill-structure/) |
| Make project conventions configurable (not hardcoded) | [`conventions-as-data-pattern/`](conventions-as-data-pattern/) |
| Track emerging concerns before structural commit | [`defer-then-promote-pattern/`](defer-then-promote-pattern/) |
| Safely edit sync-prone files | [`atomic-edits-pattern/`](atomic-edits-pattern/) |
| See an existing skill applying all patterns | [`examples/`](examples/) (walks through the diagram skill) |
| Scaffold a new skill from template | [`scripts/`](scripts/) + [`../template/`](../template/) |

## The 3 essential patterns

Every skill in this repo applies these:

1. **Uniform folder structure** — `SKILL.md` + `conventions-schema/` + `conventions-defaults/` + `patterns/` + `examples/` + `scripts/` + type-specific docs
2. **Conventions as data** — projects provide their own conventions in a project-root file · skills read + apply
3. **Defer-then-promote** — emerging concerns are logged · promoted to canonical only after threshold

Plus **atomic edits** when the skill manipulates sync-prone files.

## Why a meta-skill

Without explicit codification of these patterns, every new skill creator would:
- Re-derive the folder structure
- Hardcode project specifics (then have to refactor later)
- Miss the defer-then-promote pattern → diagram clutter / silent omissions

The meta-skill says "here's how we do it" once, and every future skill picks up the convention without manual ramp-up.

## Folder layout

```
core/meta/
├── SKILL.md                          ← agent-facing entry
├── README.md                         ← this file
├── skill-creation-guide/             step-by-step creation process
├── uniform-skill-structure/          folder structure mandate
├── conventions-as-data-pattern/      conventions-as-data pattern
├── defer-then-promote-pattern/       generic defer-then-promote pattern
├── atomic-edits-pattern/             sync-prone file editing
├── examples/                         walkthroughs of existing skills
└── scripts/                          scaffolding scripts
```

`core/meta/` itself follows the uniform skill structure, just like any other skill.

## License

Internal. Adapt freely.
