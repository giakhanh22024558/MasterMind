# features · scripts

This skill **defines** the feature list; rendering the `.xlsx` is a pipeline step.

The `features.xlsx` is generated from the table `.md` by the pipeline's renderer — [`business_analysis/scripts/ba_md_to_xlsx.py`](../../../business_analysis/scripts/) — in `features` mode (it adds the `Priority` / `In Scope` dropdowns, the `Ready?` / `Done?` checkboxes, and merges feature-level cells):

```bash
python ba_md_to_xlsx.py features <context>/features/context.md <output>/features.xlsx
```

No feature-specific scripts. If feature-specific tooling becomes necessary, add `<verb>-<noun>.py` here and list it in this README.
