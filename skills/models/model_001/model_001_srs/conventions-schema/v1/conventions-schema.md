# model_001_srs · conventions schema

Checklist các convention một dự án cần khai báo khi dùng skill `model_001_srs`. Dự án điền schema này vào `<project-root>/model_001_srs-conventions.md`; mục nào bỏ trống → fallback về [`../../conventions-defaults/`](../../conventions-defaults/).

(Về meta-pattern, xem [`meta/conventions-as-data-pattern/`](../../../../../../meta/conventions-as-data-pattern/).)

## Required conventions

### 1 · Định danh dự án

| Item | Format | Default | Ví dụ |
|---|---|---|---|
| Tên dự án | Text ngắn | (lấy từ tiêu đề trang bìa của file .md) | `RoomBooking` |
| Phụ đề tài liệu | Text | `Software Requirements Specification` | — |
| Đường dẫn logo | Path tới file ảnh (.png) | [`scripts/v1/assets/srs_logo.png`](../../scripts/v1/assets/srs_logo.png) | `assets/my_logo.png` |

> Tên dự án **không hard-code** — generator lấy từ dòng tiêu đề đầu tiên của frontmatter `.md` và truyền vào footer + trang bìa.

### 2 · Metadata tài liệu

| Item | Format | Default | Ví dụ |
|---|---|---|---|
| Phiên bản | `Draft x.y.z` theo semver | `Draft 1.0.0` | `Draft 1.0.3` |
| Ngày | `DD/MM/YYYY` | (ngày tạo) | `19/05/2026` |
| Đội chuẩn bị | Text | `[Đội kỹ thuật]` | `Đội kỹ thuật Slitigenz` |

### 3 · Bảng màu (tùy chọn override)

| Item | Format | Default | Ghi chú |
|---|---|---|---|
| Màu chủ đạo | Hex `RRGGBB` | `193D74` | Heading 1/2 + nền header bảng + gạch chân H1 |
| Màu accent | Hex | `156082` | Heading 5 |
| Màu chữ thân bài | Hex | `252729` | — |

> Đa số dự án **không cần override màu** — bộ màu mặc định decode từ SRS chuẩn. Chỉ khai khi cần đồng bộ brand riêng.

## Optional conventions

- **Giới hạn AI prompt** (`Max_N_char` cho ô nhập AI) — chỉ khai nếu hệ thống có tính năng AI; default `4000`
- **Giá trị Loại/Thuộc tính bổ sung** — nếu domain cần Loại component mới, bổ sung vào Legend canonical (`LEGEND_TYPES` / `LEGEND_ATTRS` trong `scripts/v1/srs_format.py`) trước khi dùng, **không** tự chế trong .md

## Checklist (cho skill agent)

Khi nạp file conventions của dự án lần đầu:

- [ ] Tên dự án xác định (từ .md hoặc conventions file)
- [ ] Logo: dùng file dự án hay default?
- [ ] Phiên bản + ngày + đội chuẩn bị đã có
- [ ] Có override màu brand không?
- [ ] Hệ thống có tính năng AI → cần khai giới hạn prompt không?

Nếu mục bắt buộc nào chưa rõ và không phải optional → **hỏi người dùng** trước khi sinh tài liệu.
