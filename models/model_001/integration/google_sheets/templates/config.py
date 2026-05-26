# -*- coding: utf-8 -*-
"""Project config — EDIT THIS FILE per project.

Each project copies the template and fills in real values.
"""

# ─── Spreadsheet IDs ─────────────────────────────────────────────────────────
# Take from the Sheet URL: docs.google.com/spreadsheets/d/<ID>/edit
SPREADSHEET_ID = "<PASTE_SPREADSHEET_ID_HERE>"

# ─── Sheet (tab) names ───────────────────────────────────────────────────────
BACKLOG_SHEET = "Backlog"            # ← rename to match the actual sheet tab

# ─── Backlog column indexes (1-based) ────────────────────────────────────────
# Example schema: Epic ID | Epic | Feature ID | Feature | Story ID | User Story | Priority | Status | Lifecycle
B_EPIC_ID    = 1
B_EPIC       = 2
B_FEAT_ID    = 3
B_FEAT       = 4
B_STORY_ID   = 5
B_USER_STORY = 6
B_PRIORITY   = 7
B_STATUS     = 8
B_LIFECYCLE  = 9

# ─── ID format ───────────────────────────────────────────────────────────────
EPIC_PREFIX,  EPIC_DIGITS  = "EPIC-",  2     # EPIC-01, EPIC-02, ...
FEAT_PREFIX,  FEAT_DIGITS  = "FEAT-",  3     # FEAT-001, FEAT-002, ...
STORY_PREFIX, STORY_DIGITS = "STORY-", 3     # STORY-001, STORY-002, ...

# ─── Allowed dropdown values (validated before push) ─────────────────────────
PRIORITY_VALUES  = ["Very high", "High", "Medium", "Low"]
STATUS_VALUES    = ["Backlog", "Ready", "In Progress", "In Review", "Done"]
LIFECYCLE_VALUES = ["Active", "Done", "Archived", "Superseded"]
