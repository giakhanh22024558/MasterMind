# Setup — sheets_api template

## 5-minute setup

### 1. Install dependency

```bash
pip install gspread
```

### 2. Create Google OAuth credentials

1. Open **https://console.cloud.google.com**
2. Create a new project (or use an existing one)
3. **APIs & Services → Library** → enable **2 APIs**:
   - Google Sheets API
   - Google Drive API
4. (First time) Configure the OAuth consent screen: `External` → fill in minimal name/email → Save
5. **Credentials → Create Credentials → OAuth client ID**:
   - Application type: **Desktop app**
   - Name: anything
6. Download the JSON → rename to **`credentials.json`** → place at project root:
   ```
   <project-root>/credentials.json
   ```

### 3. Copy the template into the project

```bash
cp -r <mastermind>/models/model_001/integration/google_sheets/templates/ <project-root>/sheets_api/
rm <project-root>/sheets_api/SETUP.md  # docs not needed inside the project
```

### 4. Edit `config.py`

Open `<project-root>/sheets_api/config.py` and fill in:
- `SPREADSHEET_ID` (from the Sheet URL)
- `SHEET_NAME` (tab name)
- Column indexes
- Dropdown allowed values

### 5. Edit `backlog.py` (or another name)

CRUD class for the project's entity. Study the template to learn the pattern.

### 6. Verify

```bash
cd <project-root>
python -m sheets_api.verify_setup
```

First time → a browser opens automatically → sign in with the Google account that has edit access → approve → `token.json` is created; subsequent runs need no auth.

### 7. `.gitignore`

```
credentials.json
token.json
service_account.json
```

## Alternative — Service Account (for automation, no browser needed)

1. Cloud Console → Credentials → **Create Service Account**
2. Create a key (JSON) → download → rename to **`service_account.json`** → place at project root
3. Open the Google Sheet → **Share** → invite the service account email (`xxx@yyy.iam.gserviceaccount.com`) with Editor permission

The code automatically prefers Service Account when the file exists.

## Troubleshooting

| Error | Fix |
|---|---|
| `FileNotFoundError: credentials.json` | OAuth JSON not downloaded yet; see step 2 |
| `gspread.exceptions.APIError: 403` | The logged-in account has no edit access to the Sheet → share the Sheet with that email as Editor |
| `gspread.exceptions.WorksheetNotFound` | `SHEET_NAME` in `config.py` doesn't match; check the tab name on the Sheet |
| Token expired (every few months) | Delete `token.json` → re-run → reauthorize |
| `redirect_uri_mismatch` error | The OAuth client must be **Desktop app** (not Web app) |
