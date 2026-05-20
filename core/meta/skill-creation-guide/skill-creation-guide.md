# Skill creation guide

Step-by-step process for creating a new skill in `models/`. Apply this when a user asks you to build a new skill for a new domain (e.g. `business_analysis`, `code_review`, `data_modeling`, `interview-prep`).

## Step 1 · Decide the shape

Two shapes are possible:

### Shape A · Single-domain (flat)

For skills where there's only ONE main "type" of activity. The skill has top-level content modules and that's it.

```
models/model_NNN/<category>/<skill>/
├── SKILL.md                          agent-facing entry
├── README.md                         human-facing
├── conventions-schema/            what conventions the skill needs from a project
├── conventions-defaults/          sensible defaults when project doesn't specify
├── patterns/                      reusable patterns
├── examples/                      worked walkthroughs
├── scripts/                       helper scripts (if applicable)
└── <type-specific-docs>/          one or more domain-specific docs
```

Example: `code-review` skill — one main activity (review code) · no need for sub-skills.

### Shape B · Multi-domain (with sub-skills)

For skills covering multiple distinct types (like `diagram/` covers architecture, DFD, future activity/BPMN/sequence/state/ERD). Use when each type has different conventions, notation, or workflows.

```
core/<category>/                      framework (invariant)
├── SKILL.md                          dispatcher
├── README.md
├── _shared/                          cross-sub-skill methodology
│   └── <module>/
└── _project-template/             starter conventions for adopting projects

models/model_NNN/<category>/          concrete sub-skills (per project)
├── <sub-skill-1>/                    follows uniform sub-skill structure (Shape A)
│   ├── SKILL.md
│   ├── conventions-schema/
│   ├── ...
└── <sub-skill-2>/                    same uniform shape
    └── ...
```

Example: `diagram/` skill — covers architecture, DFD, etc. · each has different notation and conventions.

### How to choose

- **Start with Shape A** if you're not sure
- **Move to Shape B** when you discover the skill has 2+ distinct types that share methodology but diverge on conventions/notation
- The migration A→B is easy: move existing content into a `<primary-type>/` sub-folder, create `_shared/` for the reusable bits

## Step 2 · Copy the template

```bash
cp -r core/template models/model_NNN/<category>/<your-skill-name>
```

Then **rename and update** every file with your skill's name and content.

## Step 3 · Write the top-level `SKILL.md`

This is the **agent-facing entry**. Required content:

| Section | Content |
|---|---|
| YAML frontmatter | `name: <your-skill-name>` · `description: <when to use, what it does, key features>` |
| When to use | List of triggers — what user requests invoke this skill |
| Core principles | 3-7 one-liner principles guiding the skill |
| Workflow templates | Concrete workflows the skill supports (with cross-refs to content modules) |
| Anti-patterns | What NOT to do |
| Quick dispatch (Shape B only) | Table of sub-skills with one-line purpose |

Cross-reference a content module by its folder path (e.g. `patterns/`).

## Step 4 · Write the top-level `README.md`

**Human-facing entry**. Mirrors `SKILL.md` content but with more narrative context. Includes:

- Quick-start table (if you want X, read Y)
- Folder layout diagram
- Adoption guide
- Stack assumptions (markdown, Python, etc.)

## Step 5 · Define `conventions-schema/`

This is the **checklist** of what conventions a project must define when using your skill. Think of it as an interface contract.

For each item the project might want to specify, list:

- What the convention controls
- Format expected
- Default value (cross-ref to `conventions-defaults/`)
- Examples

This file is consumed when reading a project's `<skill>-conventions.md`. If something in the schema is undefined in the project file, the skill falls back to defaults.

## Step 6 · Define `conventions-defaults/`

The **sensible defaults** applied when a project doesn't specify a convention. Make them:

- Domain-best-practice (not arbitrary)
- Self-documenting (each default has a rationale)
- Overridable (always make clear the project can change)

## Step 7 · Populate `patterns/`

At least **one pattern** in `patterns/`. A pattern is:

- A reusable structural approach
- Has a name, problem statement, solution, and trade-offs
- Cross-references other patterns / docs where applicable

Examples from `diagram/`: storage-exception, cross-layer-reads-tracking, hardware-gaps-tracking.

For a new skill (e.g. `code_review`), patterns might be: blast-radius-analysis, semantic-vs-syntactic, regression-risk-tracking, etc.

## Step 8 · Populate `examples/`

At least **one worked walkthrough** showing how the skill applies to a concrete scenario. Use generic placeholders (no client/project-specific identifiers) so the example is reusable.

A good walkthrough:

- Sets up a concrete scenario
- Shows the workflow step-by-step
- Demonstrates pattern application
- Lists what went right + what to avoid

## Step 9 · Populate `scripts/` (if applicable)

If the skill involves manipulating files (especially sync-prone files), provide:

- Helper Python scripts (atomic, idempotent, re-runnable)
- A `README.md` in the scripts folder listing each script's purpose

If the skill is pure-narrative (no file manipulation), the `scripts/` folder can have just a `README.md` saying "no scripts required for this skill" — but the folder MUST exist per the uniform structure.

## Step 10 · Define `<type-specific-docs>/`

Each domain has its own vocabulary:

- `diagram/architecture/` has `edge-labels/`
- `diagram/dfd/` (future) would have `yourdon-notation/`
- `business_analysis/` might have `stakeholder-matrix-format/`, `requirement-types/`
- `code_review/` might have `severity-levels/`, `comment-conventions/`

Write one or more docs describing the domain's specific vocabulary, notation, or rules.

## Step 11 · Update top-level navigation

| File | Update |
|---|---|
| `models/model_NNN/README.md` | Add your skill to the model's skill table |
| Your skill's `SKILL.md` | Make sure description matches what the skill does · helps AI agents pick it |

## Step 12 · Test by invoking

Pretend you're an AI agent receiving a user request that should invoke this skill:

- Does `SKILL.md` clearly say "use this when…"?
- Can you follow the workflow templates without guessing?
- Are conventions discoverable from the schema?
- Are defaults sensible?

Iterate until you'd be confident applying the skill to a fresh project.

## Cross-references to meta-patterns

Inside your new skill's content, when discussing a meta-pattern (conventions-as-data, defer-then-promote, atomic-edits), **reference the meta-skill** instead of duplicating the content:

```markdown
For the conventions-as-data principle, see [`conventions-as-data-pattern`](../../../core/meta/conventions-as-data-pattern/).
```

This keeps the meta-pattern as single source of truth · your skill stays focused on domain content.

## Anti-patterns specific to skill creation

- ❌ Skipping `core/template/` — building from scratch tends to drift from convention
- ❌ Hardcoding domain examples in pattern docs (use placeholders like `<spec-id>`, `<reference-id>`)
- ❌ Writing patterns that are actually just project notes — patterns must be reusable across projects
- ❌ Inventing new folder structures — uniform structure exists for a reason
- ❌ Re-deriving meta-patterns instead of referencing `core/meta/`
- ❌ Forgetting to update the model's `README.md` after creating a new skill
