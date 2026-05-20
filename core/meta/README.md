# Meta-skill — README

How to create any new skill in this repo · the mindset, structure, and patterns that every skill follows.

## Quick start

| If you want to… | Read |
|---|---|
| Understand the meta-skill in one page | [`SKILL.md`](SKILL.md) |
| Walk through creating a new skill step-by-step | [`skill-creation-guide/`](skill-creation-guide/) |
| Learn the mandatory folder structure | [`uniform-skill-structure/`](uniform-skill-structure/) |
| Learn the versioning model | [`versioning-pattern/`](versioning-pattern/) |
| Make project conventions configurable (not hardcoded) | [`conventions-as-data-pattern/`](conventions-as-data-pattern/) |
| Track emerging concerns before structural commit | [`defer-then-promote-pattern/`](defer-then-promote-pattern/) |
| Safely edit sync-prone files | [`atomic-edits-pattern/`](atomic-edits-pattern/) |
| See an existing skill applying all patterns | [`examples/`](examples/) (walks through `diagram/`) |
| Scaffold a new skill from template | [`scripts/`](scripts/) + [`../template/v1/`](../template/v1/) |

## The 4 essential patterns

Every skill in this repo applies these:

1. **Uniform folder structure** — `SKILL.md` + `conventions-schema/` + `conventions-defaults/` + `patterns/` + `examples/` + `scripts/` + type-specific docs
2. **Per-leaf-folder versioning** — every content module has `vN/` subfolders · default = latest
3. **Conventions as data** — projects provide their own conventions in a project-root file · skills read + apply
4. **Defer-then-promote** — emerging concerns are logged · promoted to canonical only after threshold

Plus **atomic edits** when the skill manipulates sync-prone files.

## Why a meta-skill

Without explicit codification of these patterns, every new skill creator would:
- Re-derive the folder structure
- Re-invent the versioning model
- Hardcode project specifics (then have to refactor later)
- Miss the defer-then-promote pattern → diagram clutter / silent omissions

The meta-skill says "here's how we do it" once, and every future skill picks up the convention without manual ramp-up.

## Folder layout

```
meta/
├── SKILL.md                                       ← agent-facing entry
├── README.md                                      ← this file
├── skill-creation-guide/v1/                       step-by-step creation process
├── uniform-skill-structure/v1/                    folder structure mandate
├── versioning-pattern/v1/                         versioning model
├── conventions-as-data-pattern/v1/                conventions-as-data pattern
├── defer-then-promote-pattern/v1/                 generic defer-then-promote pattern
├── atomic-edits-pattern/v1/                       sync-prone file editing
├── examples/v1/                                   walkthroughs of existing skills
└── scripts/v1/                                    scaffolding scripts
```

`meta/` itself follows the uniform skill structure — meta-patterns versioned at leaf-folder grain, just like any other skill.

## License

Internal. Adapt freely.
