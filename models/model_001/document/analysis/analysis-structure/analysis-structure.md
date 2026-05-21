# Cấu trúc bảng Gap Analysis & Impact Analysis

Đặc tả cột của hai bảng phân tích. Nội dung viết ở `.md`, render ra `.xlsx` bằng [`../scripts/`](../scripts/) theo chuẩn style chung.

---

## 1 · Gap Analysis

Bảng phẳng, một hàng header. So sánh từng CR với SRS / hệ thống hiện tại.

| Cột | Nội dung |
|---|---|
| CR ID | Mã change request — `CR-XX` |
| Topic | Module / lĩnh vực CR thuộc về |
| Criteria | Tiêu chí / màn hình cụ thể |
| Description | Tóm tắt 1 dòng yêu cầu |
| Current System Behavior (As-Is) | Hiện trạng hệ thống / đặc tả SRS hiện tại |
| Client Expectation (To-Be) | **Nguyên văn** kỳ vọng của khách — không diễn giải lại |
| Expected Implementation | Định hướng thực hiện để khớp To-Be |
| Gap Type | Phân loại khoảng cách (xem [`../conventions-defaults/`](../conventions-defaults/)) |
| Impact Level | Mức độ ảnh hưởng — `P0` / `P1` / `P2` |
| Client Note | Ghi chú thêm / phản hồi của khách (tùy chọn) |

---

## 2 · Impact Analysis

Bảng **header 2 tầng** (có merge). Phân rã từng CR thành công sức + tác động.

### Cấu trúc cột

```
| CR ID | Implementation (nội dung task) | Estimation (man-hours) | Impacted Module | Decision |
|       |  BA  |  FE  |  BE             |  BA  |  FE  |  BE       |                 |          |
```

| Cột | Nội dung |
|---|---|
| CR ID | Mã change request — khớp với Gap Analysis |
| Implementation · BA | Việc của Business Analyst — **gạch đầu dòng từng task** |
| Implementation · FE | Việc của Frontend — gạch đầu dòng |
| Implementation · BE | Việc của Backend — gạch đầu dòng |
| Estimation · BA / FE / BE | Ước lượng man-hours từng vai trò (số) |
| Impacted Module | Module tính năng bị ảnh hưởng + ghi chú ngắn cần đổi gì |
| Decision | This Sprint / Next Sprint / Another Sprint / Invalid · Out-of-scope |

### Quy ước nội dung

- **Implementation**: mỗi phần BA/FE/BE là **danh sách gạch đầu dòng** (`•` hoặc `-`), không viết đoạn liền. Trong `.md` dùng `<br>` ngăn các dòng.
- **Estimation**: đơn vị **man-hours**, để số. Renderer tự cộng dòng **TỔNG**.
- **Decision**: chỉ là **đề xuất** của BA; người dùng/PM quyết định cuối. Render thành dropdown.
- **Impacted Module**: liệt kê module + 1 câu mô tả tác động cho mỗi module.

### Format .md nguồn cho renderer `impact`

Bảng phẳng 9 cột, ô bullet dùng `<br>`:

```
| CR ID | Impl · BA | Impl · FE | Impl · BE | Est BA | Est FE | Est BE | Impacted Module | Decision |
|-------|-----------|-----------|-----------|--------|--------|--------|-----------------|----------|
| CR-01 | • task A<br>• task B | • task C | • task D | 4 | 16 | 3 | Module X — đổi … | Next Sprint |
```

Renderer tự dựng header 2 tầng, tách bullet theo `<br>`, cộng dòng TỔNG, gắn dropdown Decision.
