# output/

**Deliverables** — file binary phức tạp được sinh từ artifact templates trong `docs/`.

## File types phổ biến

- `.docx` — SRS, reports
- `.xlsx` — backlog rendered, Gap/Impact Analysis, Jira CSV import
- `.drawio` — ERD / architecture diagrams (rendered từ Mermaid)
- `.pdf` — exported reports
- `.json` — Jira REST API payloads
- `jira/*.md` — task descriptions để paste vào Jira UI

## Convention

- ✅ Agent ghi file deliverable
- ✅ Agent đồng thời tạo `.md` sidecar trong `context/` (đọc tiết kiệm token)
- ✅ User có thể download / share file ở đây
- ❌ Đừng edit binary trong folder này thủ công — re-render từ source trong `docs/` hoặc artifact md

## Sub-folders phổ biến

```
output/
├── <project>-SRS.docx
├── <project>-Backlog.xlsx
├── Gap_Analysis.xlsx
├── <project>-ERD.drawio
└── jira/
    ├── all-tasks.md
    ├── cr-01-task.json
    └── cr-01-task.md
```

Agent tự tạo sub-folder khi cần.
