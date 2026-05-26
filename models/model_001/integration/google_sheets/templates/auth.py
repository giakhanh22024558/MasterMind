# -*- coding: utf-8 -*-
"""Authorize a gspread client. Prefer Service Account, fall back to OAuth Desktop.

Drop-in — no edits required for a typical project (paths can be configured via
environment variables if needed).
"""
import os
import gspread

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDS_FILE = os.environ.get("GS_OAUTH_CREDS",    os.path.join(_ROOT, "credentials.json"))
TOKEN_FILE = os.environ.get("GS_OAUTH_TOKEN",    os.path.join(_ROOT, "token.json"))
SA_FILE    = os.environ.get("GS_SERVICE_ACCOUNT",os.path.join(_ROOT, "service_account.json"))

_client = None

def get_client():
    """Return a gspread client (singleton)."""
    global _client
    if _client is not None:
        return _client
    if os.path.exists(SA_FILE):
        _client = gspread.service_account(filename=SA_FILE)
    elif os.path.exists(CREDS_FILE):
        _client = gspread.oauth(
            credentials_filename=CREDS_FILE,
            authorized_user_filename=TOKEN_FILE,
        )
    else:
        raise FileNotFoundError(
            "❌ No credentials found. One of the following files is required at project root:\n"
            f"   {SA_FILE}   (Service Account JSON)\n"
            f"   {CREDS_FILE}   (OAuth Desktop App credentials)\n"
            "👉 See sheets_api/SETUP.md."
        )
    return _client
