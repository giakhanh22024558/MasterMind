# business_analysis · scripts

## Available scripts

| Script | Purpose |
|---|---|
| [`ba_md_to_xlsx.py`](ba_md_to_xlsx.py) | Generate the pilot `.xlsx` from a table `.md` — works for both the requirements table and the feature list |

## Install

```bash
pip install openpyxl
```

## Use

```bash
# Requirements table -> xlsx (flattens timestamp sections, adds a Run column)
python ba_md_to_xlsx.py requirements <context>/requirements/context.md <output>/requirements.xlsx

# Feature list -> xlsx (Priority / In Scope dropdowns, Ready?/Done? checkboxes,
# epic-level + feature-level cells merged across their rows)
python ba_md_to_xlsx.py features <context>/features/context.md <output>/features.xlsx
```

The `.md` is the source of truth (context layer). The `.xlsx` is the user's
manual pilot copy — write it into the working folder's `output/` directory,
per the [Core Rule](../../../../core/core-rule/).

## Notes (atomic edits)

The generator writes a `.docx`/`.xlsx`-class file that may be cloud-synced.
Per [`atomic-edits-pattern`](../../../../core/meta/atomic-edits-pattern/):

- **Close Excel** before running (an open file causes a `Permission denied` error).
- The generator reads the `.md` once and writes the `.xlsx` once — re-runnable, idempotent.
- Excel has no openpyxl-native form-control checkbox, so `Ready?` / `Done?` are
  a two-value dropdown (`☐` / `☑`).

## How to add a new script

1. Create `<verb>-<noun>.py` with a docstring stating its purpose.
2. Update the "Available scripts" table above.
