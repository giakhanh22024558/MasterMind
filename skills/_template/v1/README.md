# <skill-name>

(Human-facing overview of this skill — what it covers, who uses it, and how to adopt it.)

## Quick start

| If you want to… | Read |
|---|---|
| Understand this skill in one page | [`SKILL.md`](SKILL.md) |
| Set conventions for using this skill in your project | [`conventions-schema/`](conventions-schema/) |
| See defaults | [`conventions-defaults/`](conventions-defaults/) |
| See reusable patterns | [`patterns/`](patterns/) |
| See worked walkthroughs | [`examples/`](examples/) |
| Use helper scripts | [`scripts/`](scripts/) |

## Folder layout

```
<skill-name>/
├── SKILL.md                                       ← unversioned · agent-facing entry
├── README.md                                      ← unversioned · this file
├── conventions-schema/v1/                         versioned
├── conventions-defaults/v1/                       versioned
├── patterns/v1/                                   versioned
├── examples/v1/                                   versioned
└── scripts/v1/                                    versioned
```

## How to adopt in a project

1. **Copy the project-conventions template** (if this skill provides one) or fill in based on [`conventions-schema/`](conventions-schema/)
2. **Save** as `<project-root>/<skill-name>-conventions.md`
3. **Fill in** what applies · leave defaults for the rest
4. **Optionally pin module versions** if your project depends on older behavior

## How to evolve this skill

| Change | Action |
|---|---|
| Typo / broken link | Edit `vN/` in place · no bump |
| Behavior change (breaking) | Bump `v(N)` → `v(N+1)` · don't touch old |
| New pattern added | Bump if existing consumers would be surprised, else update in place |

See [`../_meta/versioning-pattern/`](../_meta/versioning-pattern/) for full versioning model.

## License

(Adapt as needed for your skill.)
