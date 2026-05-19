# Conventions as data (not as code)

Project-specific conventions (color palettes, ID naming schemes, spec authority codes, etc.) should live in **project-side data files**, not hardcoded into skill content.

## The problem

When skill content hardcodes project specifics:
- The skill works for one project, fails for the next
- Updating conventions requires editing the skill itself
- Multiple projects forking the skill leads to drift
- Conventions become implicit / scattered

When conventions are data:
- One skill serves many projects
- Each project owns its conventions
- Skill stays generic and reusable
- Conventions are explicit / single-source

## The pattern

### Skill side · 3 components

Every skill has these three pieces (the uniform structure mandates them):

1. **`conventions-schema/v1/<schema>.md`** — checklist of what conventions a project MUST define when using this skill
2. **`conventions-defaults/v1/<defaults>.md`** — sensible defaults applied when project doesn't specify
3. **Conventions discovery protocol** — how the skill finds and loads project conventions (typically referenced from `_shared/conventions-discovery/` or analogous)

### Project side · single config file

Each project using a skill provides a single file at project root:

```
<project-root>/<skill>-conventions.md
```

Examples:
- `<project>/diagram-conventions.md` for the `diagram` skill
- `<project>/code-review-conventions.md` for the `code_review` skill
- `<project>/business-analysis-conventions.md` for the `business_analysis` skill

This file follows the skill's `conventions-schema/` structure — projects fill in sections that apply, leave others to defaults.

## Discovery protocol (in priority order)

When invoked, the skill should:

### 1 · Look for project's conventions file

Check for `<project-root>/<skill>-conventions.md`. If present, load it as authoritative.

### 2 · Check project's `CLAUDE.md` (or equivalent)

Many projects keep AI-agent instructions in `CLAUDE.md` at the root. Look for a section about this skill's conventions. Less explicit than dedicated file but acceptable.

### 3 · Infer from existing artifacts

If neither doc is present but the project has existing skill artifacts (diagrams, reviews, etc.), infer conventions from them. Flag inferences to the user for confirmation.

### 4 · Ask the user

When still ambiguous, present the `conventions-schema/` checklist and ask the user to fill in.

### 5 · Fall back to defaults

For anything still unspecified, use the skill's `conventions-defaults/`.

## Order of authority (project > defaults)

**Project always wins.** When project conventions specify a value, use it. When project doesn't specify, use defaults.

The skill never overrides project conventions silently. If conflict is detected (e.g. defaults say "X is mandatory" but project disables it), surface the deviation to the user.

## What to put in `conventions-schema/`

Per-skill checklist. Each item should specify:

- **What** the convention controls (color, ID format, default value, etc.)
- **Format** expected (regex, enum, tabular, etc.)
- **Default** value (cross-ref to `conventions-defaults/`)
- **Optional** examples

The schema is the **contract** between skill and project. Projects look at the schema to know what they CAN customize.

## What to put in `conventions-defaults/`

Sensible defaults that:

- Match domain best practice (not arbitrary)
- Are self-documenting (each default has a rationale)
- Are overridable (always make clear the project can change)

## Acknowledging which source applied

When the skill explains its choices to the user (e.g. "applied X color scheme"), it should mention the **source**:

- "Per your project's `<skill>-conventions.md` line 12, used X palette"
- "Project didn't specify Y, used skill default from `conventions-defaults/`"

This avoids silent surprises when defaults differ from project expectation.

## Suggesting updates to project conventions

When you encounter a situation not covered by the project's conventions file:

1. Apply best judgment using skill defaults
2. Note the gap in your response
3. Recommend the user update `<skill>-conventions.md` for future consistency
4. If the deviation might recur, suggest a design-decisions row (see [`../../diagram/_shared/design-decisions-format/`](../../../diagram/_shared/design-decisions-format/))

This way, conventions grow organically rather than calcifying.

## What NOT to put in `conventions-defaults/`

- Project-specific code references (e.g. `MOD-1234`)
- Specific spec authority codes (e.g. `<COMPANY>-<DOMAIN>-5126`)
- Specific color hex codes that only one client uses

These belong in **project-side** conventions, not defaults.

## Sub-skill behavior contract

Every skill (and every sub-skill) MUST:

1. **Load** project's `<skill>-conventions.md` (if present) before any work
2. **Apply** project conventions where defined
3. **Fall back to defaults** for unspecified items
4. **Acknowledge** the source when explaining choices
5. **Suggest updates** to project file when discovering recurring gaps

Skills must NOT:

- ❌ Hardcode project specifics in `conventions-defaults/`
- ❌ Use defaults silently when project file exists but is incomplete (suggest filling in)
- ❌ Override project conventions with defaults (project always wins)

## Example · how `diagram` skill applies this pattern

- Project: provides `<project>/diagram-conventions.md` based on [`diagram/_project-template/v1/PROJECT-CONVENTIONS.md`](../../../diagram/_project-template/v1/PROJECT-CONVENTIONS.md)
- Skill: reads project file per [`diagram/_shared/conventions-discovery/v1/`](../../../diagram/_shared/conventions-discovery/v1/conventions-discovery.md)
- Sub-skill: applies project conventions, falls back to `diagram/architecture/conventions-defaults/v1/`

The pattern is the same regardless of skill domain — just swap "diagram" for "code_review" or "business_analysis".
