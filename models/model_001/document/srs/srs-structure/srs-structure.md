# SRS Template — content structure specification

Extracted from `FINAL_SRS_IEEE_LEX.md` (the LEXcentra project). This document describes the **template** every SRS following this standard must conform to — use it to create a new SRS or to check an existing one for consistency.

Reference standard: **IEEE Std 830-1998 / ISO/IEC/IEEE 29148:2018**.

> Section names, table column headers, and field labels below are kept in Vietnamese: they are the **literal text** an author writes into the `.md` and that the generator emits into the `.docx`. This skill produces Vietnamese-language SRS documents. The surrounding explanations are in English.

---

## 1. Overall layout

An SRS has **6 level-1 parts** (`#`), in this exact order:

```
[Cover page]
# Lịch sử Phiên bản       (Version History)
# Giới thiệu              (Introduction)
# Mô tả Tổng quan         (Overall Description)
# Yêu cầu Cụ thể          (Specific Requirements)
# Yêu cầu Phi chức năng   (Non-functional Requirements)
```

---

## 2. Cover page (before the first heading)

```
**[Product name]**
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

## 3. `# Lịch sử Phiên bản` (Version History)

A 4-column table, one row per version:

| Column | Content |
|---|---|
| Phiên bản (Version) | x.y.z |
| Ngày (Date) | DD/MM/YYYY |
| Mô tả (Description) | Changes, each item separated by `<br>` |
| Tác giả (Author) | Name of the person who made the change |

---

## 4. `# Giới thiệu` (Introduction)

- Opens with a **bullet list**: `Mục đích` (Purpose), `Phạm vi` (Scope), `Đối tượng` (Audience) — the item name in bold.
- `## Định nghĩa, Từ viết tắt và Ký hiệu` (Definitions, Acronyms and Symbols) — a 2-column table: `Thuật ngữ / Từ viết tắt` | `Định nghĩa`.
- `## Tổng quan Tài liệu` (Document Overview) — a paragraph + bullets describing the layout of the remaining sections.

---

## 5. `# Mô tả Tổng quan` (Overall Description)

| Subsection (`##`) | Content |
|---|---|
| Bối cảnh Sản phẩm (Product Context) | Paragraph + bullets describing the system and its external interfaces |
| Chức năng Sản phẩm (Product Functions) | 2-column table: `Lĩnh vực Tính năng` \| `Tóm tắt` |
| Phân loại Người dùng và Đặc điểm (User Classes and Characteristics) | Table: `Phân loại Người dùng` \| `Mô tả` \| `Trình độ Kỹ thuật` \| `Tần suất Sử dụng` |
| Yêu cầu Hành vi Chung (General Behavior Requirements) | A set of global rules, each rule a `###` subsection |

**Common general rules (`###`) typically include:** Quy tắc Validation Đầu vào · Quy tắc Xử lý Lỗi & Phản hồi · Quy tắc Hiển thị theo Vai trò (RBAC) · Quy tắc Trạng thái Loading · Quy tắc Hành vi Input (Inline Edit) · Quy tắc Hiển thị & Tương tác trên Màn danh sách · Quy tắc Tìm kiếm, Lọc & Sắp xếp.
→ Each rule is presented as a **3-column table**: `Tình huống` \| `Hành vi Hệ thống` \| `Ghi chú`.

---

## 6. `# Yêu cầu Cụ thể` (Specific Requirements) — the core part

Organized by **Module / Epic**. Each module is a `##` subsection:

```
## [Module name]                          (e.g. Quản lý người dùng)
   ### Danh sách Yêu cầu Chức năng
   ### Đặc tả Chi tiết — [Feature name] (FEAT-XXX[, FEAT-YYY])
   ### Đặc tả Chi tiết — [Feature name] (FEAT-ZZZ)
   ...
```

### 6.1. `### Danh sách Yêu cầu Chức năng` (Functional Requirements List)

A 3-column table listing every FR of the module:

| ID | Yêu cầu | Ưu tiên |
|---|---|---|
| FEAT-XXX | [Short requirement description] | Very High / High / Medium / Low |

### 6.2. `### Đặc tả Chi tiết — [Name] (FEAT-XXX)` — the repeating unit

Each feature specification has **5 sub-blocks in a fixed order**:

#### (a) The "Đặc tả Use Case" table — a 2-column key–value table

| Field | Content |
|---|---|
| Mã tính năng (Use case / Feature) | FEAT-XXX |
| Tác nhân (Actor) | Related user role |
| Mô tả (Description) | 1–3 sentences summarizing the feature |
| Sự kiện kích hoạt (Trigger) | The action/event that starts the use case |
| Tiền điều kiện (Precondition) | Conditions that must hold before running |
| Luồng chính (Main flow) | The steps, each separated by `<br>` |
| Luồng ngoại lệ / Xử lý lỗi (Exception flow / Error handling) | Error branches, each separated by `<br>` |
| Hậu điều kiện (Postcondition) | System state after completion |

#### (b) `#### Sơ đồ luồng` (Flow diagram)

A section holding the **business flow diagram** (activity / flow diagram) visualizing the Main flow + Exception flow. When no diagram exists yet, place a single-cell callout placeholder: `| [ Sơ đồ luồng — sẽ được bổ sung ] |`. Later, append the diagram with a `Hình [description]` caption (the generator numbers and centers it, same as the Wireframe section).

#### (c) `#### Giao diện / Wireframe` (Interface / Wireframe)

List the figures: `Hình [wireframe description]` — the generator numbers them `Hình <heading H4>-<n>`.

#### (d) `#### Đặc tả các thành phần` (Component specification)

One or more component tables. Each table may have a `#####` sub-heading (e.g. "Pop-up Tạo người dùng mới"). Standard columns:

| STT / ID | Tên / Label | Loại | Thuộc tính | Mô tả |
|---|---|---|---|---|

- **Loại** / **Thuộc tính**: only use values defined in the Legend (the General Behavior Requirements section) — see Section 8b.
- **STT / ID**: leave **empty** in the `.md` — the generator produces `COM-<heading H4>-<NNN>`.
- **Group row**: a row whose 5 cells all hold the same value is a group header (e.g. "Thông tin người dùng", "Hành động") — the generator merges it into one cell.

#### (e) `#### Business Rules / System Behavior`

A 2-column table — add it only when the feature has business constraints. Leave the "Mã BR" column empty — the generator produces `BR-<heading H4>-<NNN>`:

| Mã BR | Mô tả |
|---|---|

---

## 7. `# Yêu cầu Phi chức năng` (Non-functional Requirements)

Each NFR type is a `##` subsection: Hiệu năng (Performance) · Độ tin cậy và Tính sẵn sàng (Reliability & Availability) · Bảo mật (Security) · Khả năng Bảo trì (Maintainability) · Khả năng Mở rộng (Scalability) · Khả năng Sử dụng (Usability). Content as bullets or paragraphs.

---

## 8. Formatting conventions (mandatory)

| Convention | Description |
|---|---|
| Feature code | `FEAT-XXX` (3 digits). One specification may combine several codes: `(FEAT-001, FEAT-002)` |
| Line break inside a table cell | Use `<br>` — do not split into multiple markdown lines |
| Default-criterion tag | `[Mặc định]` placed after the value (e.g. search field, sort field) |
| Character limit | `Max_N_char` in the Thuộc tính column |
| Cross-reference | Cite a FEAT code or a section number (e.g. "per the rule in Section 2.4.1") |
| Bold | Key field names in the Use Case table, important keywords in BRs |
| Document status | `Draft` until finalized; the version increments per semver |

---

## 8b. Conventions handled automatically by the generator (`srs_format.py` + `srs_md_to_docx.py`)

The following conventions **do not need to be hand-written in the `.md`** — the generator produces them when building the `.docx`:

| Convention | Mechanism |
|---|---|
| Cover page | Logo (`assets/srs_logo.png`) + title + subtitle + version, centered. Taken from the `.md` frontmatter. **The cover page stands alone on one page** |
| Project name/code | A **variable** — the generator takes it from the cover-page title and passes it into the footer (`new_srs_document(project_name=...)`). Not hard-coded |
| Table of contents | Native TOC field (levels 1-3), updates when opened in Word. **The TOC stands alone on one page** |
| Heading numbering | Automatic — Heading 1-4: decimal `1` / `1.1` / `1.1.1` / `1.1.1.1` (lowest level = H4, 4 numbers). Heading 5: uppercase `A. B. C.`; Heading 6: lowercase `a. b. c.`. The first frontmatter heading (Lịch sử Phiên bản) is **not** numbered |
| Page breaks | Inserted automatically: after the cover page, after the TOC, after `Lịch sử Phiên bản` (so that section stands alone) |
| Heading 1 underline | Bottom border `single #193D74` |
| Duplicate-cell merge | A row whose cells are all identical (the "Đặc tả Use Case" header, group rows) → merged into one cell |
| Callout | A single-column table in the `.md` (`\| [ content ] \|`) → rendered with a cream background (e.g. the Flow-diagram placeholder) |
| **Component-table STT/ID** | Auto-generated `COM-<Heading 4 no-dot>-<NNN>` — **the code is derived from Heading 4**. Multiple tables under the H5 children of the same H4 → numbered continuously. Leave the STT/ID cells **empty** in the `.md` |
| **BR code** | Auto-generated `BR-<Heading 4 no-dot>-<NNN>`. Leave the Mã BR cells empty in the `.md` |
| Figure caption | Auto-numbered `Hình <Heading 4>-<n>`, centered. Applies to the Wireframe and Flow-diagram sections. In the `.md` just write `Hình [description]` |
| Loại/Thuộc tính Legend | The `{{LEGEND}}` marker in the `.md` → the generator inserts the 2 canonical legend tables |

**Important — reuse the Legend:** every `Loại` and `Thuộc tính` value used in a component specification MUST belong to the list defined in the Legend (the General Behavior Requirements section). Do not create new types/attributes — if a new value is needed, add it to the canonical Legend (`LEGEND_TYPES` / `LEGEND_ATTRS` in `srs_format.py`) first.

---

## 9. Checklist — does an SRS match the template

- [ ] All 6 level-1 parts present in the right order
- [ ] Cover page has the 5-row metadata table + the "Mục lục" line
- [ ] Lịch sử Phiên bản has exactly 4 columns
- [ ] Each module has a "Danh sách Yêu cầu Chức năng" before its detailed specifications
- [ ] Each `### Đặc tả Chi tiết` has all of: Use Case table (8 fields) → Wireframe → Component specification → (Business Rules if needed)
- [ ] Every FEAT code in a specification also appears in the module's "Danh sách Yêu cầu Chức năng"
- [ ] Component tables use the standard columns (STT/ID, Tên/Label, Loại, [Thuộc tính], Mô tả)
- [ ] Line breaks inside cells all use `<br>`
- [ ] A "Yêu cầu Phi chức năng" part exists at the end
