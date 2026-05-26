# Acceptance Criteria — writing convention

How to write Acceptance Criteria (AC) for each User Story in the feature backlog. **Applies to every project** that uses the `features` skill; a project may override in `<project-root>/features-conventions.md`.

## Definition

AC is the **set of criteria that determine when a User Story is "Done"** — it describes observable behavior of the feature and is **verifiable by QA**. It answers: "when the user does X on this screen, how must the system respond?"

## Two supported formats — pick one per project

The skill supports **two equally first-class AC writing formats**. Pick one per project via `ac_writing.language` in `<project-root>/features-conventions.md`.

| Convention key | Format | Pattern | Example |
|---|---|---|---|
| `ac_writing.language: en` | **English (GWT)** | `Given [precondition], when [action], then [result]` | `Given a missing required field, when clicking Save, then the Save button is disabled` |
| `ac_writing.language: vi` | **Vietnamese** | `Nếu [tiền đề], khi [hành động] thì [kết quả]` · `Khi [hành động], thì [kết quả]` · `Nếu [điều kiện], thì [kết quả]` | `Nếu thiếu field bắt buộc, thì nút Lưu disable` |

**Do not mix the two formats within one file.** A Vietnamese project → every AC uses "Khi/Nếu… thì…"; an English project → every AC uses GWT.

**Default when the project does not declare:** `en` (per MasterMind's English standardization). A Vietnamese project should set `ac_writing.language: vi` explicitly in its `features-conventions.md`.

### Eliding clauses

For a simple criterion that is just a verifiable assertion, **all three clauses are not required**. Drop the leading "Given/When" (or "Nếu/Khi") when there is no precondition:

| EN (GWT) | VI |
|---|---|
| ✅ `The creator is auto-assigned as Case Manager + Client Manager` | ✅ `Người tạo tự được gán làm Case Manager + Client Manager` |
| ✅ `Secondary sort applies on Updated Time` | ✅ `Sort phụ áp dụng theo Thời gian cập nhật` |
| ❌ `Then the creator is auto-assigned…` *(do not leave a stray "Then" — write a direct assertion)* | ❌ `Thì người tạo tự được gán…` *(do not leave a stray "Thì")* |

## 6 principles for writing AC (apply to both languages)

1. **Verifiable** — after reading, QA knows how to test it and can answer pass/fail. Not testable → not an AC.
2. **One AC = one condition** — do not pack multiple behaviors into one line; split so each can be ticked separately.
3. **Describe "what", not "how"** — "the system raises an error when the email already exists", **not** "use a unique index".
4. **Observable behavior**, not internal technical detail.
5. **Cover both happy path and edge cases** — error / empty / duplicate / unauthorized cases are commonly missed.
6. **Enough for the sprint, no polish** — AC is disposable, not a permanent spec.

## DO NOT put in AC (only reference other artifacts)

| Content | Where it actually belongs |
|---|---|
| Static field list, layout, colors | **Figma** (wireframe / design) |
| Implementation approach | **Technical design** |
| Business rules spanning multiple screens | **Business Rules catalog** — reference by ID (e.g. `per BR-MAT-02` / `theo BR-MAT-02`) |
| Role-based permissions | **Permission Matrix** |
| Date formats, toast styling | **UX Guidelines** |

> **Note on fields A/B/C:** do not list "the screen has fields A, B, C" as an AC (that is layout → Figma). Only include a field in an AC when **its presence is a conditional behavior** (show/hide/disable/required depending on state or role).

## Canonical example — STORY-007 "Create matter"

### English (`ac_writing.language: en`)

```
☐ Given all required fields are filled, when clicking Save, then create the matter + navigate to the detail page
☐ Given a missing required field, then the Save button is disabled
☐ The creator is auto-assigned as Case Manager + Client Manager (per CR-05)
☐ Given a lawyer assignee is picked, then the dropdown only shows users in the same department (per BR-MAT-02)
```

### Vietnamese (`ac_writing.language: vi`)

```
☐ Nếu các field bắt buộc đã điền, khi nhấn Lưu thì tạo vụ việc + chuyển trang chi tiết
☐ Nếu thiếu field bắt buộc, thì nút Lưu disable
☐ Người tạo tự được gán làm Case Manager + Client Manager (theo CR-05)
☐ Nếu chọn luật sư phụ trách, thì dropdown chỉ hiện người cùng phòng ban (theo BR-MAT-02)
```

The two blocks are semantically identical — every project picks **one** and stays with it across the whole backlog.

## Switching language mid-project

Not recommended (AC traceability gets messy), but if necessary:

1. Update `<project-root>/features-conventions.md`: change `ac_writing.language` value
2. Translate all existing AC rows in one pass (do not leave a mix)
3. Keep the same AC IDs (no renumbering) — translation is content-only, not identity

## Anti-patterns

- ❌ Mixing "Given… thì…" (half English, half Vietnamese) within one AC or one project
- ❌ Listing every field of the form as ACs
- ❌ Specifying implementation details ("use API X, store in table Y")
- ❌ AC too long, packing multiple behaviors — must be split
- ❌ AC that is just a restatement of the User Story name (no extra verifiable condition)
- ❌ AC that does not state "then what" — pass/fail cannot be measured

## Sheet layout — Acceptance Criteria

AC lives in a **separate sheet** within the backlog workbook (not stuffed into the Backlog sheet), mapped to Story by code so it can be maintained independently. **5 standard columns:**

| # | Column | Purpose | Notes |
|---|---|---|---|
| A | **Story ID** | `STORY-XXX` code. Repeated on every AC row to enable filter / pivot. | Bold on the story-header row |
| B | **AC ID** | `AC-{storyNum}-{NN}` (e.g. `AC-007-01`). Never reused. Empty on the story-header row. | mono font |
| C | **Criterion / User Story** | Story-header row: User Story name (bold). AC row: AC content as `☐ Given… then…` (EN) or `☐ Nếu… thì…` (VI) | wrap text |
| D | **BR ref** | Reference to a Business Rule in the SRS by code (e.g. `BR-MAT-02`). Blank if not needed. | mono font |
| E | **Test status** | Dropdown, 4 values (see below). Default: `Not tested`. | dropdown |

### Two row kinds

- **Story-header row** (1 row per story): A=Story ID (bold) · C=User Story name (bold). B/D/E empty.
- **AC row** (n rows per story): A=Story ID (repeated) · B=AC ID · C=`☐ <AC text>` · D=BR refs · E=Test status.

### Test status — dropdown values (language-agnostic)

| Value | Meaning |
|---|---|
| `Not tested` | Not yet tested by QA (default) |
| `Passed` | Tested by QA, passing |
| `Failed` | Tested by QA, failing — needs fix |
| `Blocked` | Cannot be tested (waiting on a dependency / blocker) |

These values stay in English regardless of `ac_writing.language` — they are operational metadata, not user-story content.

### Maintenance conventions

- AC sheet **has no background fill** — bold story-header row is the only separator. Thin border across the whole sheet.
- Story ID repeated on every AC row → AutoFilter by Story ID works correctly.
- AC IDs are not reused when an AC is deleted (preserves test history). When AC text is edited, **keep the same AC ID**.
- When a BR changes (due to a new CR), only update column D (BR ref) — do not touch the rest of the AC text.

## Cross-references

- [`conventions-defaults.md`](conventions-defaults.md) — default codes / priority / scope for the `features` skill (lists `ac_writing.language` default)
- [`../patterns/`](../patterns/) — patterns for writing User Stories
- The `srs` skill ([`../../srs/`](../../srs/)) also references these ACs when generating use-case specs; BR codes in column D point to Business Rules in the SRS.
- The `setup` skill template [`templates/conventions/features-conventions.md`](../../../setup/templates/conventions/features-conventions.md) — bootstrap project convention file (already includes the `ac_writing` override block).
