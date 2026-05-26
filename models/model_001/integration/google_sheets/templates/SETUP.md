# Setup — sheets_api template

## 5 phút setup

### 1. Install dep

```bash
pip install gspread
```

### 2. Tạo Google OAuth credentials

1. Mở **https://console.cloud.google.com**
2. Tạo project mới (hoặc dùng có sẵn)
3. **APIs & Services → Library** → bật **2 API**:
   - Google Sheets API
   - Google Drive API
4. (Lần đầu) Configure OAuth consent screen: `External` → fill name/email tối thiểu → Save
5. **Credentials → Create Credentials → OAuth client ID**:
   - Application type: **Desktop app**
   - Name: bất kỳ
6. Download JSON → rename **`credentials.json`** → đặt vào project root:
   ```
   <project-root>/credentials.json
   ```

### 3. Copy template vào project

```bash
cp -r <mastermind>/models/model_001/integration/google_sheets/templates/ <project-root>/sheets_api/
rm <project-root>/sheets_api/SETUP.md  # docs này không cần trong project
```

### 4. Sửa `config.py`

Mở `<project-root>/sheets_api/config.py`, điền:
- `SPREADSHEET_ID` (lấy từ URL Sheet)
- `SHEET_NAME` (tab name)
- Column indexes
- Dropdown allowed values

### 5. Sửa `backlog.py` (hoặc tên khác)

Class CRUD cho entity của project. Xem template để hiểu pattern.

### 6. Verify

```bash
cd <project-root>
python -m sheets_api.verify_setup
```

Lần đầu → browser tự mở → sign in Google account có quyền edit Sheet → cho phép → tạo `token.json`, lần sau không cần auth lại.

### 7. `.gitignore`

```
credentials.json
token.json
service_account.json
```

## Alternative — Service Account (cho automation, không cần browser)

1. Cloud Console → Credentials → **Create Service Account**
2. Create key (JSON) → download → rename **`service_account.json`** → đặt vào project root
3. Mở Google Sheet → **Share** → invite email service account (`xxx@yyy.iam.gserviceaccount.com`) với quyền Editor

Code tự ưu tiên Service Account nếu file tồn tại.

## Troubleshooting

| Lỗi | Giải pháp |
|---|---|
| `FileNotFoundError: credentials.json` | Chưa tải OAuth JSON; xem bước 2 |
| `gspread.exceptions.APIError: 403` | Account login chưa có quyền edit Sheet → share email với role Editor |
| `gspread.exceptions.WorksheetNotFound` | `SHEET_NAME` trong `config.py` không khớp; check tên tab trên Sheet |
| Token expired (vài tháng 1 lần) | Xóa `token.json` → chạy lại → reauthorize |
| Lỗi `redirect_uri_mismatch` | OAuth client phải là **Desktop app** (không phải Web app) |
