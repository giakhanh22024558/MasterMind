# core

The **invariant core** of MasterMind. Everything in `core/` is shared across all projects and **does not change** when a new model is added.

## Contents

| Folder | Role |
|---|---|
| [`core-rule/`](core-rule/) | The 3-layer core rule (input → `.md` → Python → `.docx`/`.drawio`) — every model must follow it |
| [`cross-reference/`](cross-reference/) | The cross-reference technique for editing user-layer files *(stub — pending details)* |
| [`diagram/`](diagram/) | Diagram-skill framework — `_shared/` methodology, project template |
| [`document/`](document/) | Document-skill framework for `.docx` generation |
| [`meta/`](meta/) | Meta-skill — how to create a new skill (folder structure, patterns) |
| [`template/`](template/) | Scaffold for bootstrapping a new skill |

## Principles

- `core/` does **not** contain project-specific skills — concrete skills live in [`../models/`](../models/).
- `core/` is **not** modified when a new project/model is added. If you must change core, treat it as a global change and weigh the impact on every model.
- Every skill in `models/` references back to `core/` for shared methodology.
