# Example — LEX project walkthrough

Full showcase of the `google_sheets` skill applied to the LEX project (legal case management). The project keeps 2 Sheets in parallel on Drive: **Features list** (Backlog + AC) + **Gap Analysis** (CR tracking).

## Project schema

**Sheet `Backlog`** — 3-level hierarchy:

| Col | Field | Type |
|---|---|---|
| A | Epic ID | `EPIC-XX` |
| B | Epic name | text |
| C | Feature ID | `FEAT-XXX` |
| D | Feature name | text |
| E | Story ID | `STORY-XXX` |
| F | User Story | text |
| G | Priority | dropdown: Very high / High / Medium / Low |
| H | Status | dropdown: Backlog / Ready / In Progress / In Review / Done |
| I | Lifecycle | dropdown: Active / Done / Archived / Superseded |

**Sheet `Acceptance Criteria`** — polymorphic (story header rows + AC rows):

| Col | Story header row | AC row |
|---|---|---|
| A | Story ID (bold) | Story ID |
| B | (empty) | AC ID `AC-XXX-NN` |
| C | User story name (bold) | `☐ <criteria>` |
| D | (empty) | BR ref |
| E | (empty) | Test status (dropdown) |

## Setup

```bash
# 1. Copy template from MasterMind
cp -r mastermind/models/model_001/integration/google_sheets/templates/ \
      LEX-SLI-SRS/sheets_api/

# 2. Edit config.py — set SPREADSHEET_ID = "198n3cwq..." (Features list 2)

# 3. Create OAuth credentials → credentials.json at project root

# 4. pip install gspread

# 5. Verify
cd LEX-SLI-SRS
python -m sheets_api.verify_setup
# → Connected to sheet 'Backlog' — 11 epic · 43 feature · 136 story
```

## Customizations for LEX

Because LEX has an extra `Acceptance Criteria` sheet (not in the template), add an `ac.py` module:

```python
# sheets_api/ac.py
from .auth import get_client
from . import config as C
from .helpers import insert_inheriting, validate_dropdown, find_row_index

TEST_STATUS_VALUES = ["Not tested", "Passed", "Failed", "Blocked"]

def classify_ac_row(row):
    pad = list(row) + [""] * 5
    sid, aid = pad[0], pad[1]
    if sid and sid.startswith("STORY-") and not aid:
        return "story_header", {"story_id": sid, "name": pad[2]}
    if sid and aid and aid.startswith("AC-"):
        return "ac", {"story_id": sid, "id": aid, "text": pad[2],
                      "br_ref": pad[3], "test_status": pad[4]}
    return "other", None

class ACAPI:
    def __init__(self):
        self.gc = get_client()
        self.ws = self.gc.open_by_key(C.SPREADSHEET_ID).worksheet("Acceptance Criteria")
        self._cache = None
    # ... (similar pattern: _all, _template_row_of, list_for_story, create, update, delete)
```

→ Full code in [LEX project: `sheets_api/ac.py`](../../../../../../../sheets_api/ac.py).

## Usage examples in the project

### Update story status
```python
from sheets_api import BacklogAPI
BacklogAPI().update_story("STORY-013", status="In Review")
```

### Create a new story + ACs in one command
```python
from sheets_api import BacklogAPI, ACAPI
bk, ac = BacklogAPI(), ACAPI()

new_id = bk.create_story("FEAT-001",
    "[CR-19] User filters matters by Tag",
    priority="High", status="Ready", lifecycle="Active")

ac.create_story_header(new_id, "[CR-19] User filters matters by Tag")
ac.create(new_id, "When the user picks ≥1 Tag, the list filters with OR logic between Tags")
ac.create(new_id, "If 0 Tags are picked, the Tag filter does not apply (other filters remain)")
```

### Mark an AC as passed after QA
```python
ACAPI().update_test_status("AC-013-02", "Passed")
```

### Bulk update — flip every story in a feature from Backlog → Ready
```python
bk = BacklogAPI()
for s in bk.stories(feature_id="FEAT-001"):
    if s["status"] == "Backlog":
        bk.update_story(s["id"], status="Ready")
```

## Result

- ✅ Every edit is **one revision** on the Sheet (visible in the Drive Activity panel)
- ✅ Comments, filter views, conditional formatting **preserved**
- ✅ Dropdown color chips (Very high = red, Done = gray, …) **preserved** on inserted rows
- ✅ Apps Script `onEdit` triggers → auto re-exports `.xlsx` → Drive Desktop syncs to local in ~3s

## Pitfalls hit in the LEX project

| Bug | Fix |
|---|---|
| Inserted row loses dropdowns + has yellow bg | `insertDimension(inheritFromBefore=True)` + fallback `copyPaste(PASTE_NORMAL)` from template — encoded in `helpers.insert_inheriting()` |
| Apps Script `onEdit` creates duplicate `.xlsx (1)` file | Added `Utilities.sleep(800)` between delete-old + create-new in the script |
| Token expires after ~3 months | Delete `token.json` → re-run verify_setup → re-authorize in browser |

## Cross-references

- [Pattern · cell-level-edit](../patterns/cell-level-edit.md)
- [Pattern · insert-with-format-inheritance](../patterns/insert-with-format-inheritance.md)
- [Pattern · hierarchical-row-types](../patterns/hierarchical-row-types.md)
- [Setup guide](../templates/SETUP.md)
