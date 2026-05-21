# analysis · conventions schema

Checklist convention một dự án cần khai khi dùng skill `analysis`. Điền vào `<project-root>/analysis-conventions.md`; mục nào bỏ trống → fallback [`../conventions-defaults/`](../conventions-defaults/).

(Về meta-pattern, xem [`core/meta/conventions-as-data-pattern/`](../../../../core/meta/conventions-as-data-pattern/).)

## Required conventions

### 1 · Nguồn CR

| Item | Format | Default | Ví dụ |
|---|---|---|---|
| Nguồn danh sách CR | Path / URL | `input/` của project | Google Sheet URL |
| Mã CR | Prefix + số | `CR-XX` | `CR-01` |

### 2 · Phân loại

| Item | Format | Default |
|---|---|---|
| Tập giá trị Gap Type | enum | 6 loại — xem conventions-defaults |
| Thang Impact Level | enum | `P0` / `P1` / `P2` |
| Nhãn Decision | enum | This / Next / Another Sprint · Invalid |

### 3 · Estimation

| Item | Format | Default |
|---|---|---|
| Đơn vị estimation | text | man-hours |
| Vai trò tách estimation | list | BA · FE · BE |

## Optional conventions

- **Override style .xlsx** — chỉ khai nếu dự án cần bộ màu brand riêng; mặc định KHÔNG override (giữ chuẩn chung `xlsx_style.py`).
- **Vai trò bổ sung** — nếu team có thêm vai trò (vd QA, DevOps) cần estimate riêng → khai ở đây.

## Checklist (cho skill agent)

- [ ] Nguồn CR xác định
- [ ] Gap Type / Impact Level / Decision dùng default hay project-specific?
- [ ] Đơn vị + vai trò estimation đã rõ?
- [ ] Có override style .xlsx không? (mặc định: không)

Mục bắt buộc chưa rõ → **hỏi người dùng** trước khi phân tích.
