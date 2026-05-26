# -*- coding: utf-8 -*-
"""Smoke test setup. Chạy: python -m sheets_api.verify_setup"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print("══════ sheets_api setup verification ══════\n")

try:
    import gspread
    print(f"✓ gspread v{gspread.__version__}")
except ImportError:
    print("✗ gspread CHƯA cài. Chạy: pip install gspread"); sys.exit(1)

try:
    from sheets_api import BacklogAPI
    from sheets_api.auth import CREDS_FILE, SA_FILE, TOKEN_FILE
    from sheets_api import config as C
except Exception as e:
    print(f"✗ Import sheets_api fail: {e}"); sys.exit(1)

print(f"\nConfig:")
print(f"  Spreadsheet ID: {C.SPREADSHEET_ID[:20]}{'...' if len(C.SPREADSHEET_ID) > 20 else ''}")
print(f"  Backlog sheet:  {C.BACKLOG_SHEET}")
if C.SPREADSHEET_ID.startswith("<"):
    print("\n✗ Chưa sửa SPREADSHEET_ID trong config.py"); sys.exit(1)

print(f"\nCredentials check:")
print(f"  Service Account ({SA_FILE}): {'✓' if os.path.exists(SA_FILE) else '✗'}")
print(f"  OAuth creds     ({CREDS_FILE}): {'✓' if os.path.exists(CREDS_FILE) else '✗'}")
print(f"  OAuth token     ({TOKEN_FILE}): {'✓' if os.path.exists(TOKEN_FILE) else '○ chưa có'}")

if not os.path.exists(CREDS_FILE) and not os.path.exists(SA_FILE):
    print("\n✗ Thiếu credentials. Xem SETUP.md."); sys.exit(1)

print("\n──── Authorize + read test ────")
try:
    bk = BacklogAPI()
    print(f"✓ Connected to sheet '{bk.ws.title}'")
    print(f"✓ {len(bk.epics())} epic · {len(bk.features())} feature · {len(bk.stories())} story")
except Exception as e:
    print(f"✗ {type(e).__name__}: {e}")
    print("\nNếu 403: account login chưa có quyền edit Sheet?")
    sys.exit(1)

print("\n══════ Setup OK ══════")
print("Thử: bk.update_story('STORY-XXX', status='In Review')")
