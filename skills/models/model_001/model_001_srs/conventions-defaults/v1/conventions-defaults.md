# model_001_srs · conventions defaults

Format mặc định áp dụng khi `<project-root>/model_001_srs-conventions.md` không khai báo. Toàn bộ giá trị dưới đây **decode trực tiếp từ một tài liệu SRS chuẩn** đang dùng thực tế, và được mã hóa trong [`../../scripts/v1/srs_format.py`](../../scripts/v1/srs_format.py). Dự án có thể override.

(Về meta-pattern, xem [`meta/conventions-as-data-pattern/`](../../../../../../meta/conventions-as-data-pattern/).)

## Trang & lề (Page)

| Thuộc tính | Default | Ghi chú |
|---|---|---|
| Khổ giấy | A4 dọc (210 × 297 mm) | — |
| Lề | 19.05 mm đều 4 cạnh | = 1080 dxa |
| Khoảng cách header/footer | 12.5 mm | = 708 dxa |

## Font

| Vai trò | Font | Cỡ |
|---|---|---|
| Chữ thân bài | Mulish | 11 pt |
| Chữ trong bảng | Mulish | 10 pt |
| Tiêu đề trang bìa | Mulish | 28 pt |
| Caption (Hình) | Mulish italic | 9 pt |

## Bảng màu

| Tên | Hex | Dùng cho |
|---|---|---|
| Màu chủ đạo | `193D74` | Heading 1/2, nền header bảng, gạch chân H1 |
| Accent teal | `156082` | Heading 5 |
| Xám | `656668` | Heading 4, dòng version trang bìa |
| Navy caption | `0E2841` | Caption |
| Chữ thân bài | `252729` | Body text, Title, Heading 3 |
| Nền callout | `FFF8DF` | Bảng callout 1 ô (placeholder) |
| Chữ header bảng | `FFFFFF` | Chữ trên nền header xanh |

## Heading

| Cấp | Cỡ | Đậm | Màu | Numbering |
|---|---|---|---|---|
| Title | 28 pt | — | `252729` | — |
| Heading 1 | 16 pt | ✅ | `193D74` | `1` · có **gạch chân** `#193D74` |
| Heading 2 | 13 pt | ✅ | `193D74` | `1.1` |
| Heading 3 | 11.5 pt | ✅ | `252729` | `1.1.1` |
| Heading 4 | 11 pt | ✅ | `656668` | `1.1.1.1` (cấp thấp nhất dạng số) |
| Heading 5 | 11 pt | ✅ | `156082` | `A. B. C.` (chữ HOA, restart theo H4) |
| Heading 6 | 11 pt | — | `1F4D78` | `a. b. c.` (chữ thường, restart theo H5) |

- Heading frontmatter đầu tiên ("Lịch sử Phiên bản") **không** numbering.

## Bảng

| Thuộc tính | Default |
|---|---|
| Bề rộng nội dung | 171.9 mm (A4 − 2 lề) |
| Viền | Đơn 0.5 pt, toàn bộ ô |
| Header | Nền `#193D74`, chữ trắng in đậm 10 pt |
| Body | Chữ 10 pt màu đen |
| Hàng có mọi ô giống nhau | Tự merge thành 1 ô |

## Quy ước tự sinh

| Quy ước | Format mặc định |
|---|---|
| Mã STT/ID bảng thành phần | `COM-<Heading 4 bỏ dấu chấm>-<NNN>` · nối tiếp trong cùng H4 |
| Mã Business Rule | `BR-<Heading 4 bỏ dấu chấm>-<NNN>` |
| Số hình | `Hình <Heading 4>-<n>` · căn giữa · áp dụng cho Wireframe + Sơ đồ luồng |
| Trang bìa | Đứng độc lập 1 trang |
| Mục lục | Field TOC native cấp 1-3, đứng độc lập 1 trang, tự cập nhật khi mở Word |
| Ngắt trang | Sau trang bìa · sau Mục lục · sau "Lịch sử Phiên bản" |

## Footer

`{Tên dự án}  ·  Software Requirements Specification` + tab phải + `Trang {PAGE} / {NUMPAGES}` — toàn bộ 9 pt.

## Legend Loại / Thuộc tính (canonical)

Danh sách giá trị `Loại` (Input, Select, Button, Date Picker…) và `Thuộc tính` (`Required`, `Unique`, `Read-only`, `Max_N_char`, `[Mặc định]`…) là **canonical**, định nghĩa trong `LEGEND_TYPES` / `LEGEND_ATTRS` tại [`../../scripts/v1/srs_format.py`](../../scripts/v1/srs_format.py). Tài liệu chính **tái sử dụng**, không tạo mới.

## Khi defaults áp dụng

Mỗi mục dự án không khai trong `model_001_srs-conventions.md` → lấy default ở đây. Skill **acknowledge nguồn** khi giải thích:

- "Theo `model_001_srs-conventions.md` của dự án, dùng X"
- "Dự án không khai Y, dùng default từ `conventions-defaults/`"
