# Example · Generating a complete SRS for the "RoomBooking" system

A walkthrough of generating a full SRS `.docx` document from a Markdown file using the `model_001_srs` skill. Sample content file: [`SRS_Sample.md`](SRS_Sample.md).

## Setup · scenario

We need to create an SRS for `RoomBooking` — an internal meeting-room booking system. Scope: 1 module (`Quản lý đặt phòng họp`) with 3 features (`FEAT-001` view calendar, `FEAT-002` create a booking, `FEAT-003` cancel a booking).

## Step-by-step

### 1 · Discover conventions

Look for `<project-root>/model_001_srs-conventions.md`. This demo project has none → use all defaults from [`conventions-defaults/`](../../conventions-defaults/). The project name is taken from the cover-page title in the `.md` (`RoomBooking`).

### 2 · Author the `.md` content

Following the structure in [`srs-structure/`](../../srs-structure/):

- **Frontmatter** — project name, subtitle, version, metadata table → the generator builds the cover page
- **6 level-1 parts** — Lịch sử Phiên bản · Giới thiệu · Mô tả Tổng quan · Yêu cầu Cụ thể · Yêu cầu Phi chức năng
- **Each feature** = `### Đặc tả Chi tiết — … (FEAT-XXX)` with 5 sub-blocks: Use Case · Flow diagram · Wireframe · Component specification · Business Rules
- Leave the **STT/ID cells empty**, write captions as `Hình [description]` with no number, use the `{{LEGEND}}` marker for the legend tables

### 3 · Run the generator

```bash
python ../../scripts/v1/srs_md_to_docx.py SRS_Sample.md RoomBooking_SRS.docx
```

Expected output:

```
Built: .../RoomBooking_SRS.docx
  headings=40, tables=21, total blocks=92
```

### 4 · Open & verify

Open the `.docx` in Word — the table-of-contents field updates automatically. Cross-check:

- The cover page stands alone (logo + "RoomBooking" + version + metadata)
- The TOC stands alone, levels 1-3
- "Lịch sử Phiên bản" stands alone on one page, not numbered
- Heading numbering: `1 Giới thiệu` … `3.1.2.1 Sơ đồ luồng`; sub-items `A. / B.`
- The Use Case table has a single merged header cell; component tables have STT/ID codes `COM-3123-001`…
- Figures are centered, numbered `Hình 3.1.2.2-1`
- Footer `RoomBooking · Software Requirements Specification    Trang X / Y`

## Patterns demonstrated

- [`content-format-separation`](../../patterns/v1/content-format-separation.md) — pure content in the `.md`, formatting applied by `srs_format.py`, the generator handles ID codes & figure numbers & numbering & cell merging.

## What went right · what to avoid

| ✅ Do | ❌ Avoid |
|---|---|
| Leave STT/ID cells empty — the generator fills them | Pre-filling `COM-…` in the `.md` (it will be overwritten / duplicated) |
| Write captions as `Hình [description]` with no number | Numbering figures manually like `Hình 1.` |
| Close Word before running the generator | Running the generator while the `.docx` is open (`Permission denied` error) |
| Use Loại/Thuộc tính values from the Legend | Inventing new component types outside the Legend |
