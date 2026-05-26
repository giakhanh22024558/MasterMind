---
name: google_sheets
description: Edit Google Sheets directly via the Sheets API (gspread) — cell-level CRUD that preserves comments, version history, filter views, conditional formatting and data validation. Provides ready-to-use templates with the critical `insertDimension(inheritFromBefore=True)` + `copyPaste(PASTE_NORMAL)` pattern needed to insert rows without losing formatting/dropdowns. Use whenever a project needs Claude (or scripts) to edit a Sheet "live" — alternative to download → modify → upload-overwrite which destroys comments/history.
---

# google_sheets — edit Google Sheets live via API

## When to use

When a project has live data in Google Sheets and needs Claude / scripts to edit on command while **preserving** comments, version history, filter views, conditional formatting, and dropdowns.

**Anti-use case:** read-only / dump → use MCP `read_file_content` or Drive Desktop `.xlsx` sync (simpler). This skill is for **write** operations.

## Core distinction — Cell-level vs File-replace

| | Cell-level (this skill) | File-replace (upload .xlsx overwrite) |
|---|---|---|
| Cell comments / notes | ✅ Preserved | ❌ Lost |
| Version history | ✅ Each edit is one revision | ❌ Reset |
| Filter views | ✅ Preserved | ❌ Lost |
| Conditional formatting | ✅ Preserved | ❌ Lost |
| Data validation (dropdowns) | ✅ Preserved | ❌ Lost |
| Setup | OAuth one-time (~5 min) | None |

→ This skill is **mandatory** when the user uses a Sheet as a working tool (not dump-and-replace).

## 3 core patterns

| Pattern | Solves |
|---|---|
| [`cell-level-edit`](patterns/cell-level-edit.md) | Philosophy: why API vs replace; OAuth setup trade-off |
| [`insert-with-format-inheritance`](patterns/insert-with-format-inheritance.md) | **Most common bug**: vanilla `insert_row` drops format/DV — fix with `insertDimension(inheritFromBefore=True)` + fallback `copyPaste(PASTE_NORMAL)` from a template |
| [`hierarchical-row-types`](patterns/hierarchical-row-types.md) | Classify rows by "which columns are filled" — e.g. Epic row (col A+B), Feature row (col C+D), Story row (col E+F+G+H+I) — characteristic of backlog-management sheets |

## Templates (drop-in)

[`templates/`](templates/) — Python files to copy into a project:

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

What each project customizes:
1. `config.py` — Spreadsheet IDs, sheet names, column mappings, allowed dropdown values
2. `backlog.py` (or other name) — CRUD methods for the project's entity (Story/Task/Ticket…)

## Workflow

### First-time setup (per project)

1. Copy `templates/` → `<project-root>/sheets_api/`
2. Edit `config.py`: fill in `SPREADSHEET_ID`, `SHEET_NAME`, column indexes, allowed dropdown values
3. Edit `backlog.py`: classify rows for the project schema, CRUD methods per entity
4. User creates OAuth credentials (see [`templates/SETUP.md`](templates/SETUP.md))
5. Run `python -m sheets_api.verify_setup`

### Daily use

```python
from sheets_api import BacklogAPI
bk = BacklogAPI()
bk.update_story("STORY-013", status="In Review")     # cell-level edit
bk.create_story("FEAT-001", "...", priority="High")  # insert with inherited format
```

## When NOT to use this skill

- ❌ Need to edit Google Docs / Slides → different API (Docs API, Slides API)
- ❌ Project too small — 1-2 edits per month → use MCP `create_file` to copy + edit manually (simpler)
- ❌ Sheet is not Google Sheets — if the file is a pure `.xlsx` on Drive (not native Sheets) → use openpyxl + upload-overwrite (accept history loss)

## Anti-patterns

- ❌ Using vanilla `gspread.Worksheet.insert_row()` — drops format/DV (see [insert-with-format-inheritance pattern](patterns/insert-with-format-inheritance.md))
- ❌ Hard-coding Spreadsheet IDs scattered through the code — keep them in one place inside `config.py`
- ❌ Not validating dropdown values before pushing — pollutes the Sheet with stray values
- ❌ Committing `credentials.json` / `token.json` to git — put them in `.gitignore`
- ❌ Using an API key — Sheets API requires OAuth or Service Account; API keys are **not** accepted for write operations

## Cross-references

| Reference | Used for |
|---|---|
| [`integration/jira/`](../jira/) | Sibling skill — Jira issue CRUD (similar concept, REST API) |
| [`document/features/`](../../document/features/) | Backlog-management skill — its output is this skill's input |
| [`document/analysis/`](../../document/analysis/) | Gap/Impact Analysis can also be edited via API the same way |
| [Core Rule](../../../../core/core-rule/) | Sheet on Drive = User layer (source of truth when the user edits); local .md = Context layer |

## Dependencies

- `pip install gspread` (v6+ recommended)
- Google Cloud project with Sheets API + Drive API enabled
- OAuth Desktop credentials or Service Account JSON
