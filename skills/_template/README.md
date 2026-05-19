# Skill template

Copy-paste starter scaffold for creating a new skill in `skills/`.

## How to use

### Option A · Use the scaffolding script (recommended)

```bash
# Edit CONFIG block in scripts/_meta/scaffold-new-skill.py first
python skills/_meta/scripts/v1/scaffold-new-skill.py
```

Output: a new `skills/<your-skill-name>/` folder with the uniform structure, placeholders renamed, and a list of next steps.

### Option B · Manual copy

```bash
cp -r skills/_template/v1 skills/<your-skill-name>
```

Then manually find-and-replace placeholders:
- `<skill-name>` → your skill name (snake_case, e.g. `business_analysis`)
- `<SKILL_NAME>` → your skill name (display form, e.g. `Business Analysis`)
- `<skill description here>` → your skill's description

## What you get

```
<your-skill-name>/
├── SKILL.md                                       agent-facing entry
├── README.md                                      human-facing overview
├── conventions-schema/v1/conventions-schema.md    checklist of conventions
├── conventions-defaults/v1/conventions-defaults.md  defaults
├── patterns/v1/README.md                          placeholder + how to add patterns
├── examples/v1/README.md                          placeholder + how to add examples
└── scripts/v1/README.md                           placeholder + when to add scripts
```

Each module starts with at minimum a README that:
- Explains what the module should contain
- Notes the convention for adding new items
- Cross-references the meta-patterns

## What to do next

1. Fill in `SKILL.md` workflow templates with your skill's actual workflows
2. Define your conventions in `conventions-schema/v1/conventions-schema.md`
3. Set sensible defaults in `conventions-defaults/v1/conventions-defaults.md`
4. Add at least one pattern in `patterns/v1/`
5. Add at least one worked walkthrough in `examples/v1/`
6. (If applicable) Add scripts in `scripts/v1/`
7. Update `skills/README.md` to add your skill to the "Currently implemented" table

See [`../_meta/skill-creation-guide/`](../_meta/skill-creation-guide/) for the full step-by-step guide.
