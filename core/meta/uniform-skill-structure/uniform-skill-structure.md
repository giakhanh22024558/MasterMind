# Uniform skill structure (mandatory)

Every concrete skill (and every category framework) in this repo MUST follow the same folder structure. This makes any skill predictable to navigate — readers know where `patterns/` is, where `scripts/` is, where conventions are defined.

> **Where skills live:** a concrete skill lives in a model at `models/model_NNN/<category>/<skill>/` (`<category>` is `diagram` or `document`). Cross-cutting framework and methodology live in `core/`.

## Shape A · Single concrete skill (flat)

A concrete skill — one main "type" of activity. It has top-level content modules and that's it. Lives at `models/model_NNN/<category>/<skill>/`.

```
models/model_NNN/<category>/<skill>/
├── SKILL.md                          ← agent-facing entry
├── README.md                         ← human-facing entry
├── conventions-schema/               ← what conventions the skill needs
│   └── conventions-schema.md
├── conventions-defaults/             ← sensible defaults
│   └── conventions-defaults.md
├── patterns/                         ← reusable patterns (1+ files)
├── examples/                         ← worked walkthroughs (1+ files)
├── scripts/                          ← helper scripts (or just README)
│   └── README.md
└── <type-specific-docs>/             ← 1+ domain-specific docs
    └── <doc>.md
```

Examples: `models/model_001/document/srs/`, `models/model_001/diagram/architecture/`.

## Shape B · Multi-domain category (framework + sub-skills)

When a domain covers multiple distinct types (like `diagram` covers architecture, DFD, future activity/BPMN/sequence/state/ERD), it is split across `core/` and `models/`:

- The **framework** lives in `core/<category>/` — the dispatcher `SKILL.md`, the cross-cutting `_shared/` methodology, and `_project-template/`. Invariant across projects.
- Each **concrete sub-skill** is a Shape A skill living in a model at `models/model_NNN/<category>/<type>/`.

```
core/<category>/                      ← framework (invariant)
├── SKILL.md                          ← dispatcher
├── README.md
├── _shared/                          ← cross-sub-skill methodology
│   ├── <module-a>/
│   ├── <module-b>/
│   └── scripts/
└── _project-template/
    └── PROJECT-CONVENTIONS.md         ← starter for projects adopting this category

models/model_NNN/<category>/          ← concrete sub-skills (per project)
├── <sub-skill-1>/                    ← Shape A folder structure
│   ├── SKILL.md                      sub-skill entry
│   ├── conventions-schema/
│   ├── conventions-defaults/
│   ├── patterns/
│   ├── examples/
│   ├── scripts/
│   └── <type-specific>/
└── <sub-skill-2>/                    ← same Shape A
    └── ...
```

Example: the `diagram` category — framework in `core/diagram/`, the `architecture` sub-skill in `models/model_001/diagram/architecture/`.

## Mandatory elements per skill / sub-skill

| Element | Required | Purpose |
|---|---|---|
| `SKILL.md` | ✅ | Agent-facing entry · YAML frontmatter (name, description) + when-to-use + workflow + anti-patterns |
| `README.md` | ✅ (for top-level) · optional (for sub-skill) | Human-facing overview |
| `conventions-schema/` | ✅ | Checklist of conventions a project must define |
| `conventions-defaults/` | ✅ | Defaults applied when project doesn't specify |
| `patterns/` | ✅ (at least 1 pattern · can be a `README.md` placeholder if no patterns yet) | Reusable structural approaches |
| `examples/` | ✅ (at least 1 walkthrough) | Concrete demonstrations |
| `scripts/` | ✅ (can be just a `README.md` if no scripts needed) | Helper scripts |
| `<type-specific-docs>/` | ⚙️ (at least 1 if the skill has domain-specific vocabulary) | Notation · vocabulary · rules |

`SKILL.md` and `README.md` are navigation docs — they always reflect the current state. The content modules (`conventions-schema/`, `patterns/`, etc.) hold the actual skill content.

## Why this structure

| Benefit | Mechanism |
|---|---|
| **Predictable navigation** | Reader always knows where `patterns/` is, where `scripts/` is |
| **Easy onboarding for new skills** | Copy `core/template/`, fill in content, done |
| **Modular evolution** | Change `patterns/` without touching `scripts/` |
| **Project-overridable conventions** | `conventions-schema/` + `conventions-defaults/` enable conventions-as-data pattern |
| **Self-documenting depth** | The folder structure itself is documentation |

## Adding a new content module to an existing skill

If you discover a recurring concept that deserves its own module (e.g. you keep adding similar patterns and want to formalize):

1. Create the folder: `models/model_NNN/<category>/<skill>/<new-module>/`
2. Add the content
3. Update the skill's `SKILL.md` to reference it
4. Done · the module is now part of the skill

The structure scales — there's no fixed maximum on how many content modules a skill has.

## Anti-patterns

- ❌ Putting `patterns/` at the top level alongside content from a sub-skill — patterns belong INSIDE the specific sub-skill (or in `_shared/` if cross-sub-skill)
- ❌ Skipping `conventions-schema/` — without it, projects don't know what to define
- ❌ Adding `scripts/` only if you have many scripts — even one helper deserves the folder for uniformity
- ❌ Adding new sibling folders to content-module folders (e.g. `patterns/templates/`) — keep each module flat

## Cross-references

- Within a skill, link to a content module by its folder path — a sibling module is `../<module>/`.
- Link to a meta-pattern via its `core/meta/` path — e.g. a skill linking to `core/meta/conventions-as-data-pattern/`.

See [`../conventions-as-data-pattern/`](../conventions-as-data-pattern/) for how conventions are loaded from project files.
