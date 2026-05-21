# analysis · conventions defaults

Giá trị mặc định khi `<project-root>/analysis-conventions.md` không khai báo. Dự án có thể override.

(Về meta-pattern, xem [`core/meta/conventions-as-data-pattern/`](../../../../core/meta/conventions-as-data-pattern/).)

---

## Chuẩn style .xlsx chung (BẮT BUỘC — áp cho MỌI sheet)

Mọi file `.xlsx` sinh ra trong repo (requirements, features, gap analysis, impact analysis…) PHẢI dùng cùng một chuẩn hình thức, mã hóa trong [`../scripts/xlsx_style.py`](../scripts/xlsx_style.py):

| Thành phần | Giá trị chuẩn |
|---|---|
| Nền header | `#1F4E79` (xanh đậm) |
| Chữ header | `#FFFFFF` trắng, in đậm, căn giữa, wrap |
| Viền ô | Đơn mảnh, màu `#BFBFBF`, toàn bộ ô |
| Ô body | Căn trên (vertical top), wrap text |
| Freeze | Cố định hàng header |
| Auto-filter | Bật trên hàng header |
| Nền dòng tổng / nhấn | `#BDD7EE` |

**Thang độ rộng cột** (đơn vị char-width Excel — dùng cho nhất quán):

| Hằng | Giá trị | Dùng cho |
|---|---|---|
| `W_ID` | 12 | Cột mã / ID |
| `W_NARROW` | 10 | Cột số (estimation, count) |
| `W_SHORT` | 16 | Nhãn ngắn (decision, status) |
| `W_MED` | 24 | Cột vừa |
| `W_WIDE` | 40 | Nội dung dài |
| `W_XWIDE` | 48 | Nội dung rất dài (mô tả, module) |

> Không tự chế màu/border riêng. Mọi script sinh `.xlsx` import `xlsx_style.py` để đảm bảo đồng bộ.

---

## Gap Type — phân loại khoảng cách (mặc định)

| Gap Type | Ý nghĩa |
|---|---|
| Missing | Yêu cầu chưa có trong hệ thống — phải làm mới |
| Missing (New Feature) | Tính năng hoàn toàn mới, quy mô lớn |
| Modification | Đổi behavior/dữ liệu của tính năng đã có |
| Enhancement | Mở rộng tính năng đã có (thêm field/option) |
| Behavior Change | Đổi luồng UX của tính năng đã có |
| No Change | Hệ thống đã đáp ứng — không cần thay đổi |

## Impact Level — mức ảnh hưởng (mặc định)

`P0` (bắt buộc / ưu tiên cao) · `P1` (nên có) · `P2` (có thể hoãn).

## Decision — quyết định sprint (mặc định)

`This Sprint` · `Next Sprint` · `Another Sprint` · `Invalid / Out-of-scope`.
Render thành dropdown trong cột Decision; **giá trị là đề xuất**, người dùng/PM chỉnh.

## Estimation

Đơn vị **man-hours**. Tách 3 vai trò **BA / FE / BE**. Renderer tự cộng dòng TỔNG.

---

## Khi defaults áp dụng

Mỗi mục dự án không khai trong `analysis-conventions.md` → lấy default ở đây. Skill **acknowledge nguồn** khi giải thích lựa chọn.
