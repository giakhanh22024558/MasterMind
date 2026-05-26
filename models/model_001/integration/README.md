# integration

Skill cluster cho **tích hợp với hệ thống bên ngoài** (Jira, Slack, Linear, …). Khác với category `document` (sinh deliverable file) hoặc `diagram` (sinh sơ đồ), category `integration` sinh ra **payload / import-format** để đẩy lên hệ thống thứ 3.

## Skills

| Skill | Purpose |
|---|---|
| [`jira/`](jira/) | Sinh Jira issue + sub-task từ Change Requests (Gap + Impact Analysis) |
| [`google_sheets/`](google_sheets/) | CRUD trên Google Sheets via API — cell-level edit (giữ comment, history, dropdown, conditional formatting). Drop-in template |

Mỗi skill follow Core Rule (`input/` → `context/` → output `output/`).
