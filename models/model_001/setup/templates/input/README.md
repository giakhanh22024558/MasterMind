# input/

**User-managed** raw materials cho project. Drop file ở đây dưới mọi format:

- `.docx` — SRS, requirement docs, contracts
- `.xlsx` — CR list, issue tracker, feature list
- `.pdf` — specs scanned
- `.png` / `.jpg` — wireframe screenshots, UI mockups
- `.drawio` / `.fig` — diagrams from designer
- `.csv` / `.txt` — data exports

## Core Rule

- ✅ User drop file
- ✅ Agent ĐỌC (qua python-docx / openpyxl / MCP read)
- ❌ Agent KHÔNG ghi vào folder này (đây là input từ phía user)

Mỗi file `input/<name>.<ext>` → agent sinh `context/<name>.md` sidecar tương ứng (đọc tiết kiệm token các session sau).

## Workflow

1. User drop file vào đây
2. Yêu cầu agent: `"đọc context của <file>"` hoặc `"sync drive"` cho integration sync
3. Agent tạo `context/<file>.md` mirror file dạng markdown
4. Sau đó skill khác dùng `context/<file>.md` làm input cho artifact (vd `docs/requirements.md`)
