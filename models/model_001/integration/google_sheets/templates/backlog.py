# -*- coding: utf-8 -*-
"""CRUD cho hierarchical backlog (Epic → Feature → Story).

Project có thể:
- DÙNG NGUYÊN nếu schema giống template (9 cột chuẩn)
- CUSTOMIZE classify_row() + column refs trong config.py nếu schema khác
- COPY pattern này để viết module cho entity khác (Task, Ticket, …)
"""
from .auth import get_client
from . import config as C
from .helpers import (
    insert_inheriting, validate_dropdown, next_sequential_id,
    find_row_index, find_section_end,
)

# ─── Row classifier (KHỚP với schema trong config.py) ────────────────────────
def classify_row(row):
    """Trả ('epic' | 'feature' | 'story' | 'other', dict|None)."""
    pad = list(row) + [""] * 9
    if pad[C.B_EPIC_ID - 1] and pad[C.B_EPIC - 1] and not pad[C.B_FEAT_ID - 1]:
        return "epic", {"id": pad[C.B_EPIC_ID - 1], "name": pad[C.B_EPIC - 1]}
    if pad[C.B_FEAT_ID - 1] and pad[C.B_FEAT - 1]:
        return "feature", {"id": pad[C.B_FEAT_ID - 1], "name": pad[C.B_FEAT - 1]}
    if pad[C.B_STORY_ID - 1] and str(pad[C.B_STORY_ID - 1]).startswith(C.STORY_PREFIX):
        return "story", {
            "id": pad[C.B_STORY_ID - 1], "name": pad[C.B_USER_STORY - 1],
            "priority": pad[C.B_PRIORITY - 1],
            "status":   pad[C.B_STATUS - 1],
            "lifecycle":pad[C.B_LIFECYCLE - 1],
        }
    return "other", None


class BacklogAPI:
    """CRUD trên sheet Backlog."""

    def __init__(self):
        self.gc = get_client()
        self.ws = self.gc.open_by_key(C.SPREADSHEET_ID).worksheet(C.BACKLOG_SHEET)
        self._cache = None

    def _all(self, fresh=False):
        if fresh or self._cache is None:
            self._cache = self.ws.get_all_values()
        return self._cache

    def _invalidate(self):
        self._cache = None

    def _template_row_of(self, row_type):
        for i, r in enumerate(self._all(), start=1):
            if classify_row(r)[0] == row_type:
                return i
        return None

    # ─── READ ────────────────────────────────────────────────────────────────
    def epics(self):
        return [m for r in self._all(fresh=True)[1:]
                for t, m in [classify_row(r)] if t == "epic"]

    def features(self, epic_id=None):
        out = []; cur_epic = None
        for r in self._all(fresh=True)[1:]:
            t, m = classify_row(r)
            if t == "epic": cur_epic = m["id"]
            elif t == "feature" and (epic_id is None or cur_epic == epic_id):
                out.append({**m, "epic_id": cur_epic})
        return out

    def stories(self, feature_id=None, epic_id=None):
        out = []; cur_epic = cur_feat = None
        for r in self._all(fresh=True)[1:]:
            t, m = classify_row(r)
            if t == "epic": cur_epic = m["id"]
            elif t == "feature": cur_feat = m["id"]
            elif t == "story":
                if feature_id and cur_feat != feature_id: continue
                if epic_id and cur_epic != epic_id: continue
                out.append({**m, "feature_id": cur_feat, "epic_id": cur_epic})
        return out

    def find_story(self, story_id):
        return next((s for s in self.stories() if s["id"] == story_id), None)
    def find_feature(self, feature_id):
        return next((f for f in self.features() if f["id"] == feature_id), None)
    def find_epic(self, epic_id):
        return next((e for e in self.epics() if e["id"] == epic_id), None)

    # ─── CREATE ──────────────────────────────────────────────────────────────
    def create_epic(self, name):
        new_id = next_sequential_id(C.EPIC_PREFIX, C.EPIC_DIGITS, self.epics())
        template = self._template_row_of("epic")
        insert_at = len(self._all()) + 1
        values = [new_id, name] + [""] * 7
        if template:
            insert_inheriting(self.ws, insert_at, values, template_row=template)
        else:
            self.ws.append_row(values, value_input_option="USER_ENTERED")
        self._invalidate()
        return new_id

    def create_feature(self, epic_id, name):
        if not self.find_epic(epic_id):
            raise ValueError(f"Epic {epic_id} không tồn tại")
        epic_row = find_row_index(self._all(),
                                  lambda r: r and r[0] == epic_id)
        insert_at = find_section_end(self._all(), epic_row, classify_row,
                                     allow_types={"feature", "story"}) + 1
        new_id = next_sequential_id(C.FEAT_PREFIX, C.FEAT_DIGITS, self.features())
        # Row trên thường là story → wrong inherit. Copy từ feature template.
        template = self._template_row_of("feature")
        values = ["", "", new_id, name] + [""] * 5
        insert_inheriting(self.ws, insert_at, values, template_row=template)
        self._invalidate()
        return new_id

    def create_story(self, feature_id, name, priority="Medium",
                     status="Backlog", lifecycle="Active"):
        validate_dropdown(priority,  C.PRIORITY_VALUES,  "priority")
        validate_dropdown(status,    C.STATUS_VALUES,    "status")
        validate_dropdown(lifecycle, C.LIFECYCLE_VALUES, "lifecycle")
        if not self.find_feature(feature_id):
            raise ValueError(f"Feature {feature_id} không tồn tại")

        feat_row = find_row_index(self._all(),
                                  lambda r: len(r) > 2 and r[C.B_FEAT_ID - 1] == feature_id)
        insert_at = find_section_end(self._all(), feat_row, classify_row,
                                     allow_types={"story"}) + 1
        new_id = next_sequential_id(C.STORY_PREFIX, C.STORY_DIGITS, self.stories())

        values = ["", "", "", "", new_id, name, priority, status, lifecycle]

        # Quyết định strategy theo type của row trên
        prev_type = classify_row(self._all()[insert_at - 2])[0] if insert_at >= 2 else None
        if prev_type == "story":
            insert_inheriting(self.ws, insert_at, values)  # inherit from before
        else:
            template = self._template_row_of("story")
            insert_inheriting(self.ws, insert_at, values, template_row=template)
        self._invalidate()
        return new_id

    # ─── UPDATE ──────────────────────────────────────────────────────────────
    def update_epic_name(self, epic_id, new_name):
        row = find_row_index(self._all(), lambda r: r and r[0] == epic_id)
        if not row: raise ValueError(f"Epic {epic_id}")
        self.ws.update_cell(row, C.B_EPIC, new_name)
        self._invalidate()
        return row

    def update_feature_name(self, feature_id, new_name):
        row = find_row_index(self._all(),
                             lambda r: len(r) > 2 and r[C.B_FEAT_ID - 1] == feature_id)
        if not row: raise ValueError(f"Feature {feature_id}")
        self.ws.update_cell(row, C.B_FEAT, new_name)
        self._invalidate()
        return row

    def update_story(self, story_id, name=None, priority=None,
                     status=None, lifecycle=None):
        validate_dropdown(priority,  C.PRIORITY_VALUES,  "priority")
        validate_dropdown(status,    C.STATUS_VALUES,    "status")
        validate_dropdown(lifecycle, C.LIFECYCLE_VALUES, "lifecycle")
        row = find_row_index(self._all(),
                             lambda r: len(r) > 4 and r[C.B_STORY_ID - 1] == story_id)
        if not row: raise ValueError(f"Story {story_id}")
        updates = []
        if name is not None:      updates.append((C.B_USER_STORY, name))
        if priority is not None:  updates.append((C.B_PRIORITY,   priority))
        if status is not None:    updates.append((C.B_STATUS,     status))
        if lifecycle is not None: updates.append((C.B_LIFECYCLE,  lifecycle))
        if updates:
            from gspread.utils import rowcol_to_a1
            batch = [{"range": rowcol_to_a1(row, col), "values": [[val]]}
                     for col, val in updates]
            self.ws.batch_update(batch, value_input_option="USER_ENTERED")
            self._invalidate()
        return row

    # ─── DELETE ──────────────────────────────────────────────────────────────
    def delete_story(self, story_id):
        row = find_row_index(self._all(),
                             lambda r: len(r) > 4 and r[C.B_STORY_ID - 1] == story_id)
        if not row: raise ValueError(f"Story {story_id}")
        self.ws.delete_rows(row)
        self._invalidate()
        return row

    def delete_feature(self, feature_id, cascade=False):
        start = find_row_index(self._all(),
                               lambda r: len(r) > 2 and r[C.B_FEAT_ID - 1] == feature_id)
        if not start: raise ValueError(f"Feature {feature_id}")
        if cascade:
            end = find_section_end(self._all(), start, classify_row,
                                   allow_types={"story"})
            self.ws.delete_rows(start, end)
            self._invalidate()
            return (start, end)
        self.ws.delete_rows(start)
        self._invalidate()
        return start

    def delete_epic(self, epic_id, cascade=False):
        start = find_row_index(self._all(), lambda r: r and r[0] == epic_id)
        if not start: raise ValueError(f"Epic {epic_id}")
        if cascade:
            end = find_section_end(self._all(), start, classify_row,
                                   allow_types={"feature", "story"})
            self.ws.delete_rows(start, end)
            self._invalidate()
            return (start, end)
        self.ws.delete_rows(start)
        self._invalidate()
        return start
