# google_sheets · conventions defaults

Defaults applied when `<project-root>/google-sheets-conventions.md` does not declare otherwise.

## Defaults

| Item | Default |
|---|---|
| Auth preference | Service Account if `service_account.json` is present, fallback to OAuth Desktop with `credentials.json` |
| OAuth token cache | `<project-root>/token.json` (auto-generated) |
| Library | `gspread` (v6+) — do not use raw `google-api-python-client` |
| Value input option | `USER_ENTERED` (Sheet parses formulas / formats per locale) instead of `RAW` |
| Insert row strategy | `insertDimension(inheritFromBefore=True)` by default; fallback `copyPaste(PASTE_NORMAL)` from a template row of the same type |
| Validation | Every dropdown value is validated **client-side** before push (raises `ValueError`) |
| Cache | Each instance caches `get_all_values()` once; call `_invalidate()` after every write |
| Folder structure | `<project-root>/sheets_api/` package + `credentials.json` at project root |
| Gitignore | `credentials.json`, `token.json`, `service_account.json` always go into `.gitignore` |
| Quota awareness | < 60 writes/minute/user → fine for manual use; for bulk → use `batch_update` |

## Override in `<project-root>/google-sheets-conventions.md`

```yaml
auth:
  preferred: service_account    # service_account | oauth
  oauth_creds: ./creds/desktop.json
  oauth_token: ./creds/token.json
  service_account: ./creds/sa.json

sheets:
  - id: "1AbC...xyz"
    name: "Backlog"
    description: "Main backlog"

insert:
  strategy: inherit_from_before     # inherit_from_before | copy_template | both
  template_lookup: first_match      # first_match | named_template
```

## Code conventions inside the `sheets_api/` package

| File | Responsibility |
|---|---|
| `auth.py` | `get_client()` singleton — reads credentials, returns an authorized gspread client |
| `config.py` | Constants: SPREADSHEET_IDs, sheet names, column indexes (1-based), allowed dropdown values |
| `helpers.py` | `insert_inheriting()`, `copy_format()`, `validate_dropdown()`, row classifiers |
| `<entity>.py` | One file per entity type (e.g. `backlog.py`, `ac.py`, `gap.py`). Class with CRUD methods |
| `__init__.py` | Exports public classes |
| `verify_setup.py` | Smoke test — run with `python -m sheets_api.verify_setup` |

## Naming convention

- Class: `<Entity>API` (e.g. `BacklogAPI`, `ACAPI`, `GapAnalysisAPI`)
- Method: `<verb>_<entity>` (`create_story`, `update_story`, `delete_story`, `find_story`, `stories()` for listing)
- ID generation: prefix + zero-padded number (e.g. `STORY-001`, `EPIC-01`, `AC-001-01`)

## Cross-references

- [`../patterns/insert-with-format-inheritance.md`](../patterns/insert-with-format-inheritance.md) — critical bug + fix
- [`../templates/`](../templates/) — drop-in code
