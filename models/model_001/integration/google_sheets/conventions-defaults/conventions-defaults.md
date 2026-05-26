# google_sheets · conventions defaults

Defaults áp dụng khi `<project-root>/google-sheets-conventions.md` không khai báo.

## Defaults

| Item | Default |
|---|---|
| Auth preference | Service Account nếu có `service_account.json`, fallback OAuth Desktop với `credentials.json` |
| OAuth token cache | `<project-root>/token.json` (auto-generated) |
| Library | `gspread` (v6+) — không dùng `google-api-python-client` thuần |
| Value input option | `USER_ENTERED` (Sheet parse formula / format theo locale) thay vì `RAW` |
| Insert row strategy | `insertDimension(inheritFromBefore=True)` mặc định; fallback `copyPaste(PASTE_NORMAL)` từ template row cùng type |
| Validation | Mọi dropdown value validate **client-side** trước khi push (raise `ValueError`) |
| Cache | Mỗi instance cache `get_all_values()` 1 lần; gọi `_invalidate()` sau mỗi write |
| Folder structure | `<project-root>/sheets_api/` package + `credentials.json` ở project root |
| Gitignore | `credentials.json`, `token.json`, `service_account.json` luôn vào `.gitignore` |
| Quota awareness | < 60 write/phút/user → ok thủ công; bulk → dùng `batch_update` |

## Override trong `<project-root>/google-sheets-conventions.md`

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

## Code conventions trong package `sheets_api/`

| File | Trách nhiệm |
|---|---|
| `auth.py` | `get_client()` singleton — đọc credentials, return authorized gspread client |
| `config.py` | Constants: SPREADSHEET_IDs, sheet names, column indexes (1-based), allowed dropdown values |
| `helpers.py` | `insert_inheriting()`, `copy_format()`, `validate_dropdown()`, row classifiers |
| `<entity>.py` | Mỗi loại entity 1 file (vd `backlog.py`, `ac.py`, `gap.py`). Class với CRUD methods |
| `__init__.py` | Export public classes |
| `verify_setup.py` | Smoke test — chạy `python -m sheets_api.verify_setup` |

## Naming convention

- Class: `<Entity>API` (vd `BacklogAPI`, `ACAPI`, `GapAnalysisAPI`)
- Method: `<verb>_<entity>` (`create_story`, `update_story`, `delete_story`, `find_story`, `stories()` cho list)
- ID generation: prefix + zero-padded number (vd `STORY-001`, `EPIC-01`, `AC-001-01`)

## Cross-references

- [`../patterns/insert-with-format-inheritance.md`](../patterns/insert-with-format-inheritance.md) — bug quan trọng + fix
- [`../templates/`](../templates/) — drop-in code
