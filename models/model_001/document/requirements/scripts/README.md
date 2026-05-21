# requirements · scripts

This skill **defines** the requirements table; rendering the `.xlsx` is a pipeline step.

The `requirements.xlsx` is generated from the table `.md` by the pipeline's renderer — [`business_analysis/scripts/ba_md_to_xlsx.py`](../../../business_analysis/scripts/) — in `requirements` mode:

```bash
python ba_md_to_xlsx.py requirements <context>/requirements/context.md <output>/requirements.xlsx
```

No requirements-specific scripts. If requirements-specific tooling becomes necessary, add `<verb>-<noun>.py` here and list it in this README.
