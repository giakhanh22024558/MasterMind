# SRS Template — Mô tả cấu trúc tài liệu

Trích xuất từ `FINAL_SRS_IEEE_LEX.md` (dự án LEXcentra). Tài liệu này mô tả **khuôn mẫu** mà mọi bản SRS theo chuẩn này phải tuân theo — dùng để tạo mới hoặc kiểm tra tính nhất quán của một SRS.

Chuẩn tham chiếu: **IEEE Std 830-1998 / ISO/IEC/IEEE 29148:2018**.

---

## 1. Bố cục tổng thể

SRS gồm **6 phần cấp 1** (`#`), theo đúng thứ tự:

```
[Trang bìa]
# Lịch sử Phiên bản
# Giới thiệu
# Mô tả Tổng quan
# Yêu cầu Cụ thể
# Yêu cầu Phi chức năng
```

---

## 2. Trang bìa (trước heading đầu tiên)

```
**[Tên sản phẩm]**
**Software Requirements Specification**
Phiên bản [Draft x.y.z] · [DD/MM/YYYY]

| **Dự án** |   |
|---|---|
| **Loại tài liệu** | Software Requirements Specification (SRS) |
| **Tiêu chuẩn IEEE** | IEEE Std 830-1998 / ISO/IEC/IEEE 29148:2018 |
| **Trạng thái** | Draft – Phiên bản [x.y.z] |
| **Được chuẩn bị bởi** | [Đội/Tổ chức] |
| **Ngày** | [DD/MM/YYYY] |

**Mục lục**
```

---

## 3. `# Lịch sử Phiên bản`

Bảng 4 cột, mỗi dòng = 1 phiên bản:

| Cột | Nội dung |
|---|---|
| Phiên bản | x.y.z |
| Ngày | DD/MM/YYYY |
| Mô tả | Các thay đổi, mỗi ý cách nhau bằng `<br>` |
| Tác giả | Tên người thực hiện |

---

## 4. `# Giới thiệu`

- Mở đầu bằng **bullet list**: `Mục đích`, `Phạm vi`, `Đối tượng` (in đậm tên mục).
- `## Định nghĩa, Từ viết tắt và Ký hiệu` — bảng 2 cột: `Thuật ngữ / Từ viết tắt` | `Định nghĩa`.
- `## Tổng quan Tài liệu` — đoạn văn + bullet mô tả bố cục các mục còn lại.

---

## 5. `# Mô tả Tổng quan`

| Tiểu mục (`##`) | Nội dung |
|---|---|
| Bối cảnh Sản phẩm | Đoạn văn + bullet mô tả hệ thống và các giao tiếp ngoại vi |
| Chức năng Sản phẩm | Bảng 2 cột: `Lĩnh vực Tính năng` \| `Tóm tắt` |
| Phân loại Người dùng và Đặc điểm | Bảng: `Phân loại Người dùng` \| `Mô tả` \| `Trình độ Kỹ thuật` \| `Tần suất Sử dụng` |
| Yêu cầu Hành vi Chung | Tập các quy tắc toàn cục, mỗi quy tắc là 1 tiểu mục `###` |

**Các quy tắc chung (`###`) thường có:** Quy tắc Validation Đầu vào · Quy tắc Xử lý Lỗi & Phản hồi · Quy tắc Hiển thị theo Vai trò (RBAC) · Quy tắc Trạng thái Loading · Quy tắc Hành vi Input (Inline Edit) · Quy tắc Hiển thị & Tương tác trên Màn danh sách · Quy tắc Tìm kiếm, Lọc & Sắp xếp.
→ Mỗi quy tắc trình bày dạng **bảng 3 cột**: `Tình huống` \| `Hành vi Hệ thống` \| `Ghi chú`.

---

## 6. `# Yêu cầu Cụ thể` — phần lõi

Tổ chức theo **Module / Epic**. Mỗi module là 1 tiểu mục `##`:

```
## [Tên Module]                          (vd: Quản lý người dùng)
   ### Danh sách Yêu cầu Chức năng
   ### Đặc tả Chi tiết — [Tên tính năng] (FEAT-XXX[, FEAT-YYY])
   ### Đặc tả Chi tiết — [Tên tính năng] (FEAT-ZZZ)
   ...
```

### 6.1. `### Danh sách Yêu cầu Chức năng`

Bảng 3 cột liệt kê toàn bộ FR của module:

| ID | Yêu cầu | Ưu tiên |
|---|---|---|
| FEAT-XXX | [Mô tả ngắn yêu cầu] | Very High / High / Medium / Low |

### 6.2. `### Đặc tả Chi tiết — [Tên] (FEAT-XXX)` — đơn vị lặp

Mỗi đặc tả tính năng gồm **5 khối con theo thứ tự cố định**:

#### (a) Bảng "Đặc tả Use Case" — bảng 2 cột (key–value)

| Trường | Nội dung |
|---|---|
| Mã tính năng (Use case / Feature) | FEAT-XXX |
| Tác nhân | Vai trò người dùng liên quan |
| Mô tả | 1–3 câu tóm tắt tính năng |
| Sự kiện kích hoạt | Hành động/sự kiện mở đầu use case |
| Tiền điều kiện | Điều kiện phải đúng trước khi chạy |
| Luồng chính | Các bước, mỗi bước cách nhau `<br>` |
| Luồng ngoại lệ / Xử lý lỗi | Các nhánh lỗi, mỗi nhánh cách nhau `<br>` |
| Hậu điều kiện | Trạng thái hệ thống sau khi hoàn tất |

#### (b) `#### Sơ đồ luồng`

Mục chứa **sơ đồ luồng nghiệp vụ** (activity / flow diagram) trực quan hóa Luồng chính + Luồng ngoại lệ. Khi chưa có diagram, đặt placeholder dạng callout 1 ô: `| [ Sơ đồ luồng — sẽ được bổ sung ] |`. Về sau append diagram bằng caption `Hình [mô tả]` (generator tự đánh số + căn giữa như mục Wireframe).

#### (c) `#### Giao diện / Wireframe`

Liệt kê các hình: `Hình [Mô tả wireframe]` — generator tự đánh số `Hình <heading H4>-<n>`.

#### (d) `#### Đặc tả các thành phần`

Một hoặc nhiều bảng component. Mỗi bảng có thể có sub-heading `#####` (vd "Pop-up Tạo người dùng mới"). Cột chuẩn:

| STT / ID | Tên / Label | Loại | Thuộc tính | Mô tả |
|---|---|---|---|---|

- **Loại** / **Thuộc tính**: chỉ dùng giá trị đã định nghĩa ở Legend (Mục Yêu cầu Hành vi Chung) — xem Mục 8b.
- **STT / ID**: để **trống** trong .md — generator tự sinh `COM-<heading H4>-<NNN>`.
- **Dòng nhóm**: một dòng có cả 5 ô cùng giá trị = tiêu đề nhóm (vd "Thông tin người dùng", "Hành động") — generator tự merge thành 1 ô.

#### (e) `#### Business Rules / System Behavior`

Bảng 2 cột — chỉ thêm khi tính năng có ràng buộc nghiệp vụ. Cột "Mã BR" để trống — generator tự sinh `BR-<heading H4>-<NNN>`:

| Mã BR | Mô tả |
|---|---|

---

## 7. `# Yêu cầu Phi chức năng`

Mỗi loại NFR là 1 tiểu mục `##`: Hiệu năng · Độ tin cậy và Tính sẵn sàng · Bảo mật · Khả năng Bảo trì · Khả năng Mở rộng · Khả năng Sử dụng. Nội dung dạng bullet hoặc đoạn văn.

---

## 8. Quy ước định dạng (bắt buộc tuân thủ)

| Quy ước | Mô tả |
|---|---|
| Mã tính năng | `FEAT-XXX` (3 chữ số). Một đặc tả có thể gộp nhiều mã: `(FEAT-001, FEAT-002)` |
| Xuống dòng trong ô bảng | Dùng `<br>` — không tách thành nhiều dòng markdown |
| Tag tiêu chí mặc định | `[Mặc định]` đặt sau giá trị (vd ô tìm kiếm, sắp xếp) |
| Giới hạn ký tự | `Max_N_char` trong cột Thuộc tính |
| Tham chiếu chéo | Trích mã FEAT hoặc số Mục (vd "theo quy tắc Mục 2.4.1") |
| In đậm | Tên trường key trong bảng Use Case, từ khóa quan trọng trong BR |
| Trạng thái tài liệu | `Draft` cho tới khi chốt; phiên bản tăng theo semver |

---

## 8b. Quy ước do generator tự xử lý (`srs_format.py` + `srs_md_to_docx.py`)

Các quy ước sau **không cần viết tay trong .md** — generator tự sinh khi build `.docx`:

| Quy ước | Cơ chế |
|---|---|
| Trang bìa | Logo (`assets/srs_logo.png`) + tiêu đề + phụ đề + version, căn giữa. Lấy từ frontmatter .md. **Trang bìa đứng độc lập 1 trang** |
| Tên/Mã dự án | **Biến** — generator lấy từ tiêu đề trang bìa, truyền vào footer (`new_srs_document(project_name=...)`). Không hard-code |
| Mục lục | Field TOC native (cấp 1-3), tự cập nhật khi mở Word. **Mục lục đứng độc lập 1 trang** |
| Numbering heading | Tự động — Heading 1-4: số thập phân `1` / `1.1` / `1.1.1` / `1.1.1.1` (cấp thấp nhất = H4, 4 số). Heading 5: chữ HOA `A. B. C.`; Heading 6: chữ thường `a. b. c.`. Heading frontmatter đầu tiên (Lịch sử Phiên bản) **không** numbering |
| Ngắt trang | Tự chèn page break: sau trang bìa, sau Mục lục, sau "Lịch sử Phiên bản" (để mục này đứng độc lập) |
| Gạch chân Heading 1 | Viền dưới `single #193D74` |
| Merge ô trùng | Hàng có mọi ô giống hệt nhau (header "Đặc tả Use Case", dòng nhóm) → tự merge thành 1 ô |
| Callout | Bảng 1 cột trong .md (`\| [ nội dung ] \|`) → render nền kem (vd placeholder Sơ đồ luồng) |
| **STT/ID bảng thành phần** | Tự sinh `COM-<Heading 4 no-dot>-<NNN>` — **mã lấy theo Heading 4**. Nhiều bảng trong các H5 con của cùng 1 H4 → đánh số nối tiếp. Ô STT/ID trong .md để **trống** |
| **Mã BR** | Tự sinh `BR-<Heading 4 no-dot>-<NNN>`. Ô Mã BR trong .md để trống |
| Caption Hình | Tự đánh số `Hình <Heading 4>-<n>`, căn giữa. Áp dụng cho mục Wireframe và Sơ đồ luồng. Trong .md chỉ cần ghi `Hình [mô tả]` |
| Legend Loại/Thuộc tính | Marker `{{LEGEND}}` trong .md → generator chèn 2 bảng chú giải canonical |

**Quan trọng — tái sử dụng Legend:** Mọi giá trị `Loại` và `Thuộc tính` dùng trong đặc tả thành phần PHẢI thuộc danh sách đã định nghĩa ở Legend (Mục Yêu cầu Hành vi Chung). Không tự tạo loại/thuộc tính mới — nếu cần giá trị mới, bổ sung vào Legend canonical (`LEGEND_TYPES` / `LEGEND_ATTRS` trong `srs_format.py`) trước.

---

## 9. Checklist kiểm tra một SRS có khớp template

- [ ] Có đủ 6 phần cấp 1 đúng thứ tự
- [ ] Trang bìa có bảng metadata 5 dòng + dòng "Mục lục"
- [ ] Lịch sử Phiên bản đúng 4 cột
- [ ] Mỗi module có "Danh sách Yêu cầu Chức năng" trước các đặc tả chi tiết
- [ ] Mỗi `### Đặc tả Chi tiết` có đủ: bảng Use Case (8 trường) → Wireframe → Đặc tả thành phần → (Business Rules nếu cần)
- [ ] Mọi mã FEAT trong đặc tả đều xuất hiện ở "Danh sách Yêu cầu Chức năng" của module
- [ ] Bảng component đúng cột chuẩn (STT/ID, Tên/Label, Loại, [Thuộc tính], Mô tả)
- [ ] Xuống dòng trong ô đều dùng `<br>`
- [ ] Có phần "Yêu cầu Phi chức năng" ở cuối
