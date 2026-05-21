# analysis — README

Skill phân tích **Change Request (CR)** thành hai artifact quyết định: **Gap Analysis** và **Impact Analysis**. Xuất sheet `.xlsx` theo chuẩn style chung của repo.

## Quick start

| Nếu bạn muốn… | Đọc |
|---|---|
| Hiểu skill trong 1 trang | [`SKILL.md`](SKILL.md) |
| Biết cấu trúc cột 2 bảng phân tích | [`analysis-structure/`](analysis-structure/) |
| Biết chuẩn style .xlsx chung | [`conventions-defaults/`](conventions-defaults/) |
| Xem ví dụ phân tích một CR | [`examples/`](examples/) |
| Render .xlsx | [`scripts/`](scripts/) |

## Quy trình

```
Change Request
   │
   ▼
[1] Gap Analysis     — CR khác gì hệ thống hiện tại?  (As-Is → To-Be)
   │
   ▼
[2] Impact Analysis  — tốn gì, đụng đâu?  (task BA/FE/BE · estimation · module · decision)
   │
   ▼
Người dùng / PM phê duyệt  →  quyết định CR nào vào sprint
```

## Render .xlsx

```bash
python scripts/analysis_md_to_xlsx.py gap     <input.md> <output.xlsx>
python scripts/analysis_md_to_xlsx.py impact  <input.md> <output.xlsx>
```

## Folder layout

```
analysis/
├── SKILL.md
├── README.md
├── analysis-structure/      ← cấu trúc cột Gap / Impact
├── conventions-schema/      ← convention dự án cần khai
├── conventions-defaults/    ← chuẩn style .xlsx + giá trị mặc định
├── patterns/                ← pattern Gap-then-Impact
├── examples/                ← walkthrough
└── scripts/                 ← xlsx_style.py + analysis_md_to_xlsx.py
```

## Vai trò trong pipeline business_analysis

Skill này là **nhánh xử lý Change Request** của pipeline BA: khi có yêu cầu thay đổi → Gap Analysis → Impact Analysis → người dùng duyệt → các CR được chọn đi tiếp qua skill [`features`](../features/) để tách thành feature đưa vào sprint.

## Stack

- **Markdown** cho nội dung phân tích
- **Python** (`openpyxl`) cho renderer — cài: `pip install openpyxl`
