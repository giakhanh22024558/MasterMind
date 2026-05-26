# -*- coding: utf-8 -*-
"""Authorize gspread client. Ưu tiên Service Account, fallback OAuth Desktop.

Drop-in — không cần sửa cho project bình thường (paths config qua biến môi trường nếu cần).
"""
import os
import gspread

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDS_FILE = os.environ.get("GS_OAUTH_CREDS",    os.path.join(_ROOT, "credentials.json"))
TOKEN_FILE = os.environ.get("GS_OAUTH_TOKEN",    os.path.join(_ROOT, "token.json"))
SA_FILE    = os.environ.get("GS_SERVICE_ACCOUNT",os.path.join(_ROOT, "service_account.json"))

_client = None

def get_client():
    """Return gspread client (singleton)."""
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
            "❌ Chưa có credentials. Cần một trong 2 file ở project root:\n"
            f"   {SA_FILE}   (Service Account JSON)\n"
            f"   {CREDS_FILE}   (OAuth Desktop App credentials)\n"
            "👉 Xem sheets_api/SETUP.md."
        )
    return _client
