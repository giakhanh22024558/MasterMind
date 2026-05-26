# Example — CR-01 → Jira tree

Worked example minh hoạ output của skill cho CR-01 (LEX project).

## Input snippets

**Gap Analysis row CR-01:**

| Field | Value |
|---|---|
| Topic | Quản lý vụ việc |
| Criteria | Dashboard — View mode |
| Description | Bổ sung chế độ xem dạng danh sách bảng cho vụ việc |
| As-Is | FEAT-001: 2 view mode = Danh sách thẻ + Kanban/Board. Không có list-table view |
| To-Be | Thêm view mode dạng list: hiển thị danh sách vụ việc theo dạng bảng, cột thông tin tương tự card view |
| Impl·BA | • Cập nhật SRS FEAT-001: thêm option View mode "List"<br>• Soạn đặc tả cột bảng<br>• Update wireframe Hình 17 |
| Impl·FE | • Implement chế độ xem List/table<br>• Toggle Card ↔ List<br>• Render bảng đủ cột |
| Impl·BE | • Đảm bảo API list vụ việc trả đủ field<br>• Không có entity mới |
| Est BA / FE / BE | 4 / 16 / 3 |
| Impacted Module | Quản lý vụ việc — Dashboard (FEAT-001) |
| Priority | P0 |
| Decision | This Sprint |
| Client Note | ok |

**Backlog match:** STORY-133 — `[CR-01] Bổ sung view mode dạng bảng (list/table) cho dashboard vụ việc`

**AC list cho STORY-133:**

- `AC-133-01` — Khi user nhấn toggle 'List view', thì dashboard chuyển sang dạng bảng với các cột Case ID / Tên / Loại / Khách hàng / …
- `AC-133-02` — Khi ở List view, single-click chọn dòng, double-click mở chi tiết
- `AC-133-03` — Nếu user toggle về Card, dashboard về dạng card cũ
- `AC-133-04` — Nếu user reload trang, view mode được nhớ theo session

---

## Output — Main task

**Title:** `[CR-01] Bổ sung chế độ xem dạng danh sách bảng cho vụ việc — Dashboard — View mode`

**Labels:** `cr-01`, `from-gap-analysis`, `quan-ly-vu-viec`

**Priority:** `Highest` *(P0)*

**Estimate:** `23 man-hours` *(4+16+3)*

**Description:**

```markdown
## Context

**As-Is:** FEAT-001: 2 view mode = Danh sách thẻ + Kanban/Board (chưa implement MS1-2). Không có list-table view.

**To-Be:** Thêm view mode dạng list: hiển thị danh sách vụ việc theo dạng bảng, với các cột thông tin tương tự view mode hiện tại (card view).

**Client Note:** ok

**Impacted Module:** Quản lý vụ việc — Dashboard (FEAT-001): thêm view mode thứ 3; ảnh hưởng component View mode toggle dùng chung.

**Decision:** This Sprint · **Priority:** P0

## Acceptance Criteria

| AC ID | Tiêu chí | Test status |
|---|---|---|
| AC-133-01 | ☐ Khi user nhấn toggle 'List view', thì dashboard chuyển sang dạng bảng với các cột Case ID / Tên / Loại / Khách hàng / Người phụ trách / Trạng thái / Hạn / Cập nhật cuối | Not tested |
| AC-133-02 | ☐ Khi ở List view, thì single-click chọn dòng, double-click mở chi tiết | Not tested |
| AC-133-03 | ☐ Nếu user toggle về Card, thì dashboard về dạng card cũ | Not tested |
| AC-133-04 | ☐ Nếu user reload trang, thì view mode được nhớ theo session | Not tested |

## Implementation breakdown

Xem 3 sub-task: `[BA]`, `[FE]`, `[BE]`.

## Reference

- Backlog: `STORY-133`
- Gap Analysis: row CR-01
```

---

## Output — Sub-task [BA]

**Title:** `[BA] [CR-01] Bổ sung chế độ xem dạng danh sách bảng cho vụ việc — Dashboard — View mode`

**Estimate:** `4 man-hours`

**Description:**

```markdown
## Công việc của BA

- Cập nhật SRS FEAT-001: thêm option View mode "List"
- Soạn đặc tả cột bảng (Case ID, Tên, Loại, KH, Người phụ trách, Trạng thái, Hạn, Cập nhật cuối)
- Update wireframe Hình 17

## Estimation

4 man-hours

## Reference

- Main task: <parent issue key>
- AC liên quan: AC-133-01, AC-133-02, AC-133-03, AC-133-04
```

---

## Output — Sub-task [FE]

**Title:** `[FE] [CR-01] Bổ sung chế độ xem dạng danh sách bảng cho vụ việc — Dashboard — View mode`

**Estimate:** `16 man-hours`

**Description:**

```markdown
## Công việc của FE

- Implement chế độ xem List/table cho dashboard vụ việc
- Toggle Card ↔ List
- Render bảng đủ cột; giữ behavior single/double-click chung

## Estimation

16 man-hours

## Reference

- Main task: <parent issue key>
- AC liên quan: AC-133-01, AC-133-02, AC-133-03, AC-133-04
```

---

## Output — Sub-task [BE]

**Title:** `[BE] [CR-01] Bổ sung chế độ xem dạng danh sách bảng cho vụ việc — Dashboard — View mode`

**Estimate:** `3 man-hours`

**Description:**

```markdown
## Công việc của BE

- Đảm bảo API list vụ việc trả đủ field cho cột bảng (Khách hàng, Hạn...)
- Không có entity mới

## Estimation

3 man-hours

## Reference

- Main task: <parent issue key>
- AC liên quan: AC-133-01, AC-133-02, AC-133-03, AC-133-04
```

---

## Visual tree

```
[CR-01] Bổ sung chế độ xem dạng danh sách bảng cho vụ việc — Dashboard — View mode
│  est: 23h · priority: Highest · labels: cr-01, from-gap-analysis, quan-ly-vu-viec
│  desc: context + 4 AC rows
│
├─ [BA] [CR-01] Bổ sung … — Dashboard — View mode    (4h)
├─ [FE] [CR-01] Bổ sung … — Dashboard — View mode    (16h)
└─ [BE] [CR-01] Bổ sung … — Dashboard — View mode    (3h)
```
