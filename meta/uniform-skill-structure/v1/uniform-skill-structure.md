# Uniform skill structure (mandatory)

Every skill (and every sub-skill within a multi-domain skill) in this repo MUST follow the same folder structure. This makes any skill predictable to navigate — readers know where `patterns/` is, where `scripts/` is, where conventions are defined.

## Shape A · Single-domain skill (flat)

```
skills/<skill>/
├── SKILL.md                          ← unversioned · agent-facing entry
├── README.md                         ← unversioned · human-facing entry
├── conventions-schema/v1/            ← versioned · what conventions the skill needs
│   └── conventions-schema.md
├── conventions-defaults/v1/          ← versioned · sensible defaults
│   └── conventions-defaults.md
├── patterns/v1/                      ← versioned · reusable patterns (1+ files)
├── examples/v1/                      ← versioned · worked walkthroughs (1+ files)
├── scripts/v1/                       ← versioned · helper scripts (or just README)
│   └── README.md
└── <type-specific-docs>/v1/          ← versioned · 1+ domain-specific docs
    └── <doc>.md
```

## Shape B · Multi-domain skill (with sub-skills)

```
skills/<skill>/
├── SKILL.md                          ← unversioned · top-level dispatcher
├── README.md                         ← unversioned
├── VERSIONING.md                     ← unversioned (optional · can ref _meta)
├── _shared/                          ← cross-sub-skill methodology
│   ├── <module-a>/v1/
│   ├── <module-b>/v1/
│   └── scripts/v1/
├── <sub-skill-1>/                    ← Shape A folder structure
│   ├── SKILL.md                      unversioned · sub-skill entry
│   ├── conventions-schema/v1/
│   ├── conventions-defaults/v1/
│   ├── patterns/v1/
│   ├── examples/v1/
│   ├── scripts/v1/
│   └── <type-specific>/v1/
└── <sub-skill-2>/                    ← same Shape A
    └── ...
```

Plus optionally:

```
skills/<skill>/
└── _project-template/v1/
    └── PROJECT-CONVENTIONS.md        ← starter for projects adopting this skill
```

## Mandatory elements per skill / sub-skill

| Element | Type | Required | Purpose |
|---|---|---|---|
| `SKILL.md` | unversioned file | ✅ | Agent-facing entry · YAML frontmatter (name, description) + when-to-use + workflow + anti-patterns |
| `README.md` | unversioned file | ✅ (for top-level) · optional (for sub-skill) | Human-facing overview |
| `conventions-schema/` | versioned content module | ✅ | Checklist of conventions a project must define |
| `conventions-defaults/` | versioned content module | ✅ | Defaults applied when project doesn't specify |
| `patterns/` | versioned content module | ✅ (at least 1 pattern · can be a `README.md` placeholder if no patterns yet) | Reusable structural approaches |
| `examples/` | versioned content module | ✅ (at least 1 walkthrough) | Concrete demonstrations |
| `scripts/` | versioned content module | ✅ (can be just a `README.md` if no scripts needed) | Helper scripts |
| `<type-specific-docs>/` | versioned content module | ⚙️ (at least 1 if the skill has domain-specific vocabulary) | Notation · vocabulary · rules |

## What's versioned, what's not

| Category | Versioned? | Rationale |
|---|---|---|
| `SKILL.md` (top-level + per sub-skill) | ❌ No | Always reflects current navigation |
| `README.md` | ❌ No | Always reflects current overview |
| `VERSIONING.md` (if present) | ❌ No | Meta-doc about versioning · always current |
| Content modules (`conventions-schema/`, `patterns/`, etc.) | ✅ Yes | Project consumers may depend on specific versions |
| `_shared/` content modules | ✅ Yes | Same reason |

See [`../versioning-pattern/`](../../versioning-pattern/) for the full versioning model.

## Why this structure

| Benefit | Mechanism |
|---|---|
| **Predictable navigation** | Reader always knows where `patterns/` is, where `scripts/` is |
| **Easy onboarding for new skills** | Copy `template/v1/`, fill in content, done |
| **Modular evolution** | Bump `patterns/v1` → `patterns/v2` without touching `scripts/` |
| **Project-overridable conventions** | `conventions-schema/` + `conventions-defaults/` enable conventions-as-data pattern |
| **Self-documenting depth** | The folder structure itself is documentation |

## Adding a new content module to an existing skill

If you discover a recurring concept that deserves its own module (e.g. you keep adding similar patterns and want to formalize):

1. Create the leaf folder: `skills/<skill>/<new-module>/v1/`
2. Add the content
3. Update the skill's `SKILL.md` to reference it
4. Done · the module is now part of the skill

The structure scales — there's no fixed maximum on how many content modules a skill has.

## Anti-patterns

- ❌ Putting `patterns/` at the top level alongside content from a sub-skill — patterns belong INSIDE the specific sub-skill (or in `_shared/` if cross-sub-skill)
- ❌ Skipping `conventions-schema/` — without it, projects don't know what to define
- ❌ Adding `scripts/` only if you have many scripts — even one helper deserves the folder for uniformity
- ❌ Versioning `SKILL.md` — it's navigation, not content
- ❌ Adding new sibling folders to leaf-content folders (e.g. `patterns/templates/`) — keep depth at `<module>/vN/`

## Cross-references

| Within a content module | Use leaf-folder paths (latest) — e.g. `[patterns/](../../patterns/)` |
| Pinned to a specific version | Use explicit `vN/` paths — e.g. `[v1/foo.md](../../patterns/v1/foo.md)` |
| To meta-patterns | Use `meta/` paths — e.g. `[versioning model](../../../meta/versioning-pattern/)` |

See [`../conventions-as-data-pattern/`](../../conventions-as-data-pattern/) for how conventions are loaded from project files.
