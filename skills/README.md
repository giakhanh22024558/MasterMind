# Skills

This folder contains the actual skills. Each subfolder is a self-contained skill following the uniform structure mandated by [`../meta/`](../meta/).

## Currently implemented

| Skill | Purpose | Status |
|---|---|---|
| [`diagram/`](diagram/) | Build, audit, and maintain software diagrams (architecture · DFD · future types) | ✅ Architecture sub-skill complete · DFD pending |
| [`models/model_001/model_001_srs/`](models/model_001/model_001_srs/) | Generate IEEE-standard SRS `.docx` documents from Markdown content (content/format separation) | ✅ Complete |

## How to add a new skill

This folder is for **created skills only**. To create a new skill:

1. **Read** [`../meta/SKILL.md`](../meta/SKILL.md) to understand the conventions (folder structure · versioning · conventions-as-data · defer-then-promote · atomic-edits)
2. **Scaffold** using [`../meta/scripts/v1/scaffold-new-skill.py`](../meta/scripts/v1/scaffold-new-skill.py) — copies [`../template/v1/`](../template/v1/) to `skills/<your-name>/` with placeholders pre-filled
3. **Fill in** content following the uniform structure
4. **Update this README** to add the new skill to the table above

## Folder layout

```
skills/
├── README.md                ← this file (overview of created skills)
├── diagram/                 ← actual skill
│   └── …                    follows uniform structure per meta-skill
└── models/                  ← skills grouped by numbered model
    └── model_001/
        └── model_001_srs/   ← actual skill (uniform structure)
```

Sibling folders at repo root:

- [`../meta/`](../meta/) — meta-skill (how to create any skill)
- [`../template/`](../template/) — starter scaffold for new skills

## License

Internal. Adapt freely. No warranty.
