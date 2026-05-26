---
name: google_sheets
description: Edit Google Sheets directly via the Sheets API (gspread) — cell-level CRUD that preserves comments, version history, filter views, conditional formatting and data validation. Provides ready-to-use templates with the critical `insertDimension(inheritFromBefore=True)` + `copyPaste(PASTE_NORMAL)` pattern needed to insert rows without losing formatting/dropdowns. Use whenever a project needs Claude (or scripts) to edit a Sheet "live" — alternative to download → modify → upload-overwrite which destroys comments/history.
---

# google_sheets — edit Google Sheet live via API

## Khi nào dùng

Khi project có data sống trên Google Sheets và cần Claude / script edit theo lệnh, mà **giữ nguyên** comment, version history, filter view, conditional formatting, dropdown.

**Anti-use case:** chỉ cần đọc/dump → dùng MCP `read_file_content` / Drive Desktop sync `.xlsx` đơn giản hơn. Skill này dành cho **write**.

## Khác biệt cốt lõi — Cell-level vs File-replace

| | Cell-level (skill này) | File-replace (upload .xlsx đè) |
|---|---|---|
| Comment / Note | ✅ Giữ | ❌ Mất |
| Version history | ✅ Mỗi edit là 1 revision | ❌ Reset |
| Filter view | ✅ Giữ | ❌ Mất |
| Conditional formatting | ✅ Giữ | ❌ Mất |
| Data validation (dropdown) | ✅ Giữ | ❌ Mất |
| Setup | OAuth 1 lần (~5 phút) | Không cần |

→ Skill này **bắt buộc** khi user dùng Sheet làm working tool (không phải dump-and-replace).

## 3 patterns cốt lõi

| Pattern | Giải quyết |
|---|---|
| [`cell-level-edit`](patterns/cell-level-edit.md) | Triết lý: why API vs replace; trade-off OAuth setup |
| [`insert-with-format-inheritance`](patterns/insert-with-format-inheritance.md) | **Bug phổ biến nhất**: `insert_row` thuần làm mất format/DV — fix bằng `insertDimension(inheritFromBefore=True)` + fallback `copyPaste(PASTE_NORMAL)` từ template |
| [`hierarchical-row-types`](patterns/hierarchical-row-types.md) | Cách classify row theo "cột nào filled" — vd Epic row (col A+B), Feature row (col C+D), Story row (col E+F+G+H+I) — đặc trưng cho backlog management sheets |

## Templates (drop-in)

[`templates/`](templates/) — bộ Python files copy vào project:

```
<project-root>/
└── sheets_api/                       ← copy templates here
    ├── __init__.py                   (ready)
    ├── auth.py                       (ready, configurable paths)
    ├── helpers.py                    (ready — _insert_inheriting, validators)
    ├── config.py                     (project FILL IN — IDs, cols, dropdowns)
    ├── backlog.py                    (project CUSTOMIZE — entity CRUD)
    └── verify_setup.py               (ready)
```

Project customize chính:
1. `config.py` — Spreadsheet IDs, sheet names, column mappings, allowed dropdown values
2. `backlog.py` (hoặc tên khác) — CRUD methods cho entity của project (Story/Task/Ticket…)

## Workflow

### Lần đầu setup (per project)

1. Copy `templates/` → `<project-root>/sheets_api/`
2. Sửa `config.py`: điền `SPREADSHEET_ID`, `SHEET_NAME`, column indexes, allowed dropdown values
3. Sửa `backlog.py`: classify rows theo schema project, CRUD methods cho entity
4. User tạo OAuth credentials (xem [`templates/SETUP.md`](templates/SETUP.md))
5. Run `python -m sheets_api.verify_setup`

### Daily use

```python
from sheets_api import BacklogAPI
bk = BacklogAPI()
bk.update_story("STORY-013", status="In Review")     # cell-level edit
bk.create_story("FEAT-001", "...", priority="High")  # insert with inherit format
```

## Khi nào KHÔNG dùng skill này

- ❌ Cần edit Google Docs / Slides → API khác (Docs API, Slides API)
- ❌ Project quá nhỏ — 1-2 lần edit/tháng → dùng MCP `create_file` để copy + edit thủ công đơn giản hơn
- ❌ Sheet không phải Google Sheets — nếu file là `.xlsx` thuần trên Drive (không phải Sheets native) → dùng openpyxl + upload đè (chấp nhận mất history)

## Anti-patterns

- ❌ Dùng `gspread.Worksheet.insert_row()` thuần — sẽ mất format/DV (xem [pattern insert-with-format-inheritance](patterns/insert-with-format-inheritance.md))
- ❌ Hard-code Spreadsheet ID rải rác trong code — luôn để 1 chỗ trong `config.py`
- ❌ Không validate dropdown value trước khi push — pollute Sheet với value lạ
- ❌ Commit `credentials.json` / `token.json` lên git — đưa vào `.gitignore`
- ❌ Dùng API key — Sheets API yêu cầu OAuth hoặc Service Account, **không** chấp nhận API key cho write

## Cross-references

| Reference | Used for |
|---|---|
| [`integration/jira/`](../jira/) | Sibling skill — Jira issue CRUD (concept tương tự, REST API) |
| [`document/features/`](../../document/features/) | Skill quản lý backlog — output của `features` là input của skill này |
| [`document/analysis/`](../../document/analysis/) | Gap/Impact Analysis cũng có thể edit qua API tương tự |
| [Core Rule](../../../../core/core-rule/) | Sheet trên Drive = User layer (source of truth khi user edit); local .md = Context layer |

## Dependencies

- `pip install gspread` (v6+ recommended)
- Google Cloud project với Sheets API + Drive API enabled
- OAuth Desktop credentials hoặc Service Account JSON
