# Acceptance Criteria — writing convention

Cách viết Acceptance Criteria (AC) cho mỗi User Story trong feature backlog. **Áp dụng cho mọi project** dùng skill `features`; project có thể override trong `<project-root>/features-conventions.md`.

## Định nghĩa

AC là **tiêu chí xác định một User Story được coi là "Done"** — mô tả hành vi quan sát được của tính năng, **kiểm chứng được bởi QA**. Trả lời câu hỏi: "khi người dùng làm X trên màn này, hệ thống phải phản hồi thế nào?"

## Format chuẩn — chọn theo ngôn ngữ AC

| Ngôn ngữ AC | Format | Ví dụ |
|---|---|---|
| **Tiếng Việt** (mặc định) | `Nếu [tiền đề], khi [hành động] thì [kết quả]` hoặc `Khi [hành động], thì [kết quả]` hoặc `Nếu [điều kiện], thì [kết quả]` | `Nếu thiếu field bắt buộc, thì nút Lưu disable` |
| **Tiếng Anh** | `Given [precondition], when [action], then [result]` | `Given missing required field, when click Save, then Save button is disabled` |

**Không trộn hai format trong cùng một file.** Project tiếng Việt → toàn bộ AC dùng "Khi/Nếu... thì..."; project tiếng Anh → toàn bộ AC dùng GWT.

### Khi nào tỉnh lược

Với tiêu chí đơn giản chỉ là khẳng định kiểm chứng được, **không bắt buộc đủ ba mệnh đề**. Bỏ "Nếu/Khi" nếu không cần tiền đề:

- ✅ `Người tạo tự được gán làm Case Manager + Client Manager`
- ✅ `Sort phụ áp dụng theo Thời gian cập nhật`
- ❌ `Then người tạo tự được gán...` *(đừng để chữ "Then" lẻ — viết thẳng câu khẳng định)*

## 6 nguyên tắc khi viết AC

1. **Kiểm chứng được** — QA đọc xong biết cách test, trả lời đúng/sai. Không test được → không phải AC.
2. **Một AC = một điều kiện** — đừng nhồi nhiều hành vi vào một dòng; tách để tick riêng.
3. **Mô tả "what", không phải "how"** — "hệ thống báo lỗi khi email trùng", **không** phải "dùng unique index".
4. **Hành vi quan sát được**, không phải nội bộ kỹ thuật.
5. **Cả happy path lẫn edge case** — lỗi / rỗng / trùng / không-quyền hay bị sót.
6. **Đủ dùng cho sprint, không đánh bóng** — AC là disposable, không phải spec vĩnh cửu.

## KHÔNG đưa vào AC (chỉ reference tới artifact khác)

| Nội dung | Nơi thực sự thuộc về |
|---|---|
| List field tĩnh, layout, màu sắc | **Figma** (wireframe / design) |
| Cách implement | **Technical design** |
| Quy tắc nghiệp vụ dùng nhiều màn | **Business Rules catalog** — reference theo ID (vd: `theo BR-MAT-02`) |
| Quyền theo vai trò | **Permission Matrix** |
| Format ngày, cách hiển thị toast | **UX Guidelines** |

> **Lưu ý field A/B/C:** đừng liệt kê "màn có field A, B, C" vào AC (đó là layout → Figma). Chỉ đưa field vào AC khi **sự xuất hiện của nó là hành vi có điều kiện** (hiện/ẩn/disable/bắt buộc theo trạng thái hoặc vai trò).

## Ví dụ chuẩn — STORY-007 "Tạo vụ việc"

```
☐ Nếu các field bắt buộc đã điền, khi nhấn Lưu thì tạo vụ việc + chuyển trang chi tiết
☐ Nếu thiếu field bắt buộc, thì nút Lưu disable
☐ Người tạo tự được gán làm Case Manager + Client Manager (theo CR-05)
☐ Nếu chọn luật sư phụ trách, thì dropdown chỉ hiện người cùng phòng ban (theo BR-MAT-02)
```

Phiên bản tiếng Anh tương đương:

```
☐ Given all required fields are filled, when clicking Save, then create matter + navigate to detail page
☐ Given missing required field, then Save button is disabled
☐ Creator is auto-assigned as Case Manager + Client Manager (per CR-05)
☐ Given a lawyer assignee is chosen, then the dropdown only shows users in the same department (per BR-MAT-02)
```

## Anti-patterns

- ❌ Trộn "Given... thì..." (nửa Anh nửa Việt)
- ❌ Liệt kê toàn bộ field của form vào AC
- ❌ Chỉ định implementation detail ("dùng API X, lưu vào table Y")
- ❌ AC quá dài, nhồi nhiều behavior — phải tách
- ❌ AC chỉ là restatement của User Story name (không thêm điều kiện kiểm chứng)
- ❌ AC không nói rõ "thì gì" — không đo được pass/fail

## Sheet layout — Acceptance Criteria

AC nằm ở **sheet riêng** trong workbook backlog (không nhồi vào sheet Backlog), map về Story qua mã code để maintain độc lập. **5 cột chuẩn:**

| # | Cột | Mục đích | Ghi chú |
|---|---|---|---|
| A | **Story ID** | Mã `STORY-XXX`. Lặp lại trên mọi AC row để filter / pivot. | Bold trên story-header row |
| B | **AC ID** | Mã `AC-{storyNum}-{NN}` (vd `AC-007-01`). Không reuse. Trống trên story-header row. | mono font |
| C | **Tiêu chí / User Story** | Story-header row: tên User Story (bold). AC row: nội dung AC dạng `☐ Nếu… thì…` | wrap text |
| D | **BR ref** | Tham chiếu sang Business Rule trong SRS theo mã (vd `BR-MAT-02`). Để trống nếu không cần. | mono font |
| E | **Test status** | Dropdown 4 giá trị (xem bên dưới). Default: `Not tested`. | dropdown |

### Hai loại dòng

- **Story-header row** (1 dòng / story): A=Story ID (bold) · C=tên User Story (bold). B/D/E trống.
- **AC row** (n dòng / story): A=Story ID (lặp) · B=AC ID · C=`☐ <AC text>` · D=BR refs · E=Test status.

### Test status — dropdown values

| Giá trị | Ý nghĩa |
|---|---|
| `Not tested` | Chưa được QA test (default) |
| `Passed` | QA đã test, đạt |
| `Failed` | QA đã test, không đạt — cần sửa |
| `Blocked` | Không test được (chờ dependency / blocker) |

### Quy ước maintain độc lập

- AC sheet **không tô màu nền** — chỉ bold story-header row để phân tách. Border thin trên toàn sheet.
- Story ID lặp trên mọi AC row → AutoFilter theo Story ID hoạt động đúng.
- AC ID không tái sử dụng khi xóa AC (giữ truy vết test history). Khi sửa nội dung AC, **giữ nguyên AC ID**.
- Khi BR thay đổi (do CR mới), chỉ cần update cột D (BR ref) — không đụng AC text khác.

## Cross-references

- [`conventions-defaults.md`](conventions-defaults.md) — các default code/priority/scope cho skill `features`
- [`../patterns/`](../patterns/) — các pattern viết User Story
- Skill `srs` ([`../../srs/`](../../srs/)) cũng tham chiếu AC này khi sinh use-case spec; mã BR ở cột D trỏ về Business Rules trong SRS.
