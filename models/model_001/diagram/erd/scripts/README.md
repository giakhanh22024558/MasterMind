# ERD · scripts

The ERD is authored as **Mermaid inside a `.md`** — no scripts are needed to create or edit it.

When the user explicitly asks for a `.drawio` render, use the **shared atomic-edit Drawio scripts** in [`core/diagram/_shared/scripts/`](../../../../../core/diagram/_shared/scripts/) — there are no ERD-specific scripts.

## How to add a script

If ERD-specific tooling becomes necessary, create `<verb>-<noun>.py` here with a docstring stating its purpose, and list it in this README.
