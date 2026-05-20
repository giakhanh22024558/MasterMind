# Skill creation guide

Step-by-step process for creating a new skill in `skills/`. Apply this when a user asks you to build a new skill for a new domain (e.g. `business_analysis`, `code_review`, `data_modeling`, `interview-prep`).

## Step 1 · Decide the shape

Two shapes are possible:

### Shape A · Single-domain (flat)

For skills where there's only ONE main "type" of activity. The skill has top-level content modules and that's it.

```
skills/<skill>/
├── SKILL.md                          unversioned · agent-facing entry
├── README.md                         unversioned · human-facing
├── conventions-schema/v1/            what conventions the skill needs from a project
├── conventions-defaults/v1/          sensible defaults when project doesn't specify
├── patterns/v1/                      reusable patterns
├── examples/v1/                      worked walkthroughs
├── scripts/v1/                       helper scripts (if applicable)
└── <type-specific-docs>/v1/          one or more domain-specific docs
```

Example: `code-review` skill — one main activity (review code) · no need for sub-skills.

### Shape B · Multi-domain (with sub-skills)

For skills covering multiple distinct types (like `diagram/` covers architecture, DFD, future activity/BPMN/sequence/state/ERD). Use when each type has different conventions, notation, or workflows.

```
skills/<skill>/
├── SKILL.md                          unversioned · dispatcher
├── README.md                         unversioned
├── VERSIONING.md                     unversioned (optional — can refer to _meta)
├── _shared/                          cross-sub-skill methodology
│   └── <module>/v1/
├── <sub-skill-1>/                    follows uniform sub-skill structure (Shape A)
│   ├── SKILL.md
│   ├── conventions-schema/v1/
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
cp -r template/v1 skills/<your-skill-name>
```

Then **rename and update** every file with your skill's name and content.

## Step 3 · Write the top-level `SKILL.md`

This is the **agent-facing entry**. Required content:

| Section | Content |
|---|---|
| YAML frontmatter | `name: <your-skill-name>` · `description: <when to use, what it does, key features>` |
| When to use | List of triggers — what user requests invoke this skill |
| Core principles | 3-7 one-liner principles guiding the skill |
| Workflow templates | Concrete workflows the skill supports (with cross-refs to versioned content modules) |
| Anti-patterns | What NOT to do |
| Quick dispatch (Shape B only) | Table of sub-skills with one-line purpose |

Use the leaf-folder paths (`patterns/`, not `patterns/v1/`) in cross-references so they auto-resolve to latest.

## Step 4 · Write the top-level `README.md`

**Human-facing entry**. Mirrors `SKILL.md` content but with more narrative context. Includes:

- Quick-start table (if you want X, read Y)
- Folder layout diagram
- Adoption guide
- Stack assumptions (markdown, Python, etc.)

## Step 5 · Define `conventions-schema/v1/`

This is the **checklist** of what conventions a project must define when using your skill. Think of it as an interface contract.

For each item the project might want to specify, list:

- What the convention controls
- Format expected
- Default value (cross-ref to `conventions-defaults/`)
- Examples

This file is consumed when reading a project's `<skill>-conventions.md`. If something in the schema is undefined in the project file, the skill falls back to defaults.

## Step 6 · Define `conventions-defaults/v1/`

The **sensible defaults** applied when a project doesn't specify a convention. Make them:

- Domain-best-practice (not arbitrary)
- Self-documenting (each default has a rationale)
- Overridable (always make clear the project can change)

## Step 7 · Populate `patterns/v1/`

At least **one pattern** in `patterns/v1/`. A pattern is:

- A reusable structural approach
- Has a name, problem statement, solution, and trade-offs
- Cross-references other patterns / docs where applicable

Examples from `diagram/`: storage-exception, cross-layer-reads-tracking, hardware-gaps-tracking.

For a new skill (e.g. `code_review`), patterns might be: blast-radius-analysis, semantic-vs-syntactic, regression-risk-tracking, etc.

## Step 8 · Populate `examples/v1/`

At least **one worked walkthrough** showing how the skill applies to a concrete scenario. Use generic placeholders (no client/project-specific identifiers) so the example is reusable.

A good walkthrough:

- Sets up a concrete scenario
- Shows the workflow step-by-step
- Demonstrates pattern application
- Lists what went right + what to avoid

## Step 9 · Populate `scripts/v1/` (if applicable)

If the skill involves manipulating files (especially sync-prone files), provide:

- Helper Python scripts (atomic, idempotent, re-runnable)
- A `README.md` in the scripts folder listing each script's purpose

If the skill is pure-narrative (no file manipulation), the `scripts/v1/` folder can have just a `README.md` saying "no scripts required for this skill" — but the folder MUST exist per the uniform structure.

## Step 10 · Define `<type-specific-docs>/v1/`

Each domain has its own vocabulary:

- `diagram/architecture/` has `edge-labels/v1/`
- `diagram/dfd/` (future) would have `yourdon-notation/v1/`
- `business_analysis/` might have `stakeholder-matrix-format/v1/`, `requirement-types/v1/`
- `code_review/` might have `severity-levels/v1/`, `comment-conventions/v1/`

Write one or more docs describing the domain's specific vocabulary, notation, or rules.

## Step 11 · Update top-level navigation

| File | Update |
|---|---|
| `skills/README.md` | Add your skill to the "Currently implemented" table |
| Your skill's `SKILL.md` | Make sure description matches what the skill does · helps AI agents pick it |

## Step 12 · Test by invoking

Pretend you're an AI agent receiving a user request that should invoke this skill:

- Does `SKILL.md` clearly say "use this when…"?
- Can you follow the workflow templates without guessing?
- Are conventions discoverable from the schema?
- Are defaults sensible?

Iterate until you'd be confident applying the skill to a fresh project.

## Step 13 · Bump versions as you learn

When you discover the skill needs to change:

- **Small fix** (typo, broken link) → edit `v1/` in place · no bump needed
- **Behavior change** that breaks consumers → bump `v1` → `v2`
- **New pattern added** to existing module → bump if existing consumers would be surprised
- **Backward-compatible enhancement** → can update `v1` in place IF no consumer pins to a snapshot

See [`../versioning-pattern/`](../../versioning-pattern/) for the bumping process.

## Cross-references to meta-patterns

Inside your new skill's content, when discussing a meta-pattern (versioning, conventions-as-data, defer-then-promote, atomic-edits), **reference the meta-skill** instead of duplicating the content:

```markdown
For the versioning model, see [`meta/versioning-pattern/`](../../meta/versioning-pattern/).
```

This keeps the meta-pattern as single source of truth · your skill stays focused on domain content.

## Anti-patterns specific to skill creation

- ❌ Skipping `template/` — building from scratch tends to drift from convention
- ❌ Hardcoding domain examples in pattern docs (use placeholders like `<spec-id>`, `<reference-id>`)
- ❌ Writing patterns that are actually just project notes — patterns must be reusable across projects
- ❌ Inventing new folder structures — uniform structure exists for a reason
- ❌ Re-deriving meta-patterns instead of referencing `meta/`
- ❌ Forgetting to update `skills/README.md` after creating a new skill
