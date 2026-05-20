# Meta-skill · scripts

| Script | Purpose |
|---|---|
| [`scaffold-new-skill.py`](scaffold-new-skill.py) | Copy `core/template/v1/` to a new skill folder under `models/` and rename placeholders. Quick start for a new skill. |

## How to use

Edit `scaffold-new-skill.py` CONFIG block:

```python
NEW_SKILL_NAME = "business_analysis"
NEW_SKILL_DESCRIPTION = "..."
```

Run:

```bash
python core/meta/scripts/v1/scaffold-new-skill.py
```

Output: a new skill folder under `models/model_NNN/<category>/` with the uniform structure, placeholders filled in, and a list of next steps.

## Why a script

Manually copying the template and renaming placeholders across 10+ files is tedious and error-prone. A script:

- Guarantees no placeholder is missed
- Reports next steps so creator doesn't forget
- Idempotent if you stop midway (deletes destination first via assertion)
- Documents the scaffold process via its own code
