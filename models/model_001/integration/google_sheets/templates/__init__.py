# -*- coding: utf-8 -*-
"""sheets_api — CRUD on Google Sheets via the gspread API.

Cell-level edits (preserves comments / history / dropdowns / conditional formatting).
Setup: see SETUP.md.

Usage:
    from sheets_api import BacklogAPI
    bk = BacklogAPI()
    bk.update_story("STORY-013", status="In Review")
    bk.create_story("FEAT-001", "...", priority="High")
"""
from .backlog import BacklogAPI

__all__ = ["BacklogAPI"]
__version__ = "0.1.0"
