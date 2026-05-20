# model_001_srs — README

A skill that generates **Software Requirements Specification (SRS)** documents to the IEEE 830 / ISO·IEC·IEEE 29148 standard in `.docx` format, from content written in Markdown.

Philosophy: **content is written in `.md` · presentation lives in Python code**. The author handles only content; the generator applies all formatting and the auto-generated conventions.

## Quick start

| If you want to… | Read |
|---|---|
| Understand the skill in one page | [`SKILL.md`](SKILL.md) |
| Know the content structure of an SRS | [`srs-structure/`](srs-structure/) |
| Know the standard format (font, color, page, numbering) | [`conventions-defaults/`](conventions-defaults/) |
| Know what a project must declare | [`conventions-schema/`](conventions-schema/) |
| See a full SRS-generation example | [`examples/`](examples/) |
| Run the generator | [`scripts/`](scripts/) |

## Generate an SRS file — 3 steps

1. **Author content** in a `.md` file following the structure in [`srs-structure/`](srs-structure/)
2. **Run**: `python scripts/srs_md_to_docx.py <input.md> <output.docx>`
3. **Open** the `.docx` in Word → the table-of-contents field updates automatically

## What the toolkit does for you

| Handled automatically | Detail |
|---|---|
| Cover page | Logo + project name + version + metadata table, standalone on one page |
| Table of contents | Native TOC field (levels 1-3), updates automatically when opened in Word |
| Heading numbering | H1-H4 decimal `1`/`1.1`/`1.1.1`/`1.1.1.1`; H5 `A. B. C.`; H6 `a. b. c.` |
| STT/ID codes | Auto-generates `COM-<heading H4>-<NNN>` for component tables, `BR-…` for Business Rules |
| Figure numbers | Auto-numbers `Hình <heading H4>-<n>`, centered |
| Cell merging | A row whose cells are all identical → merged into one cell |
| Formatting | Mulish font, color `#193D74`, A4, underlined Heading 1, footer with page numbers |

## Folder layout

```
srs/
├── SKILL.md                       ← agent-facing entry
├── README.md                      ← this file
├── conventions-schema/         ← conventions a project must declare
├── conventions-defaults/       ← default formatting (decoded from a standard SRS)
├── srs-structure/              ← specification of SRS content structure
├── patterns/                   ← reusable patterns
├── examples/                   ← walkthrough + sample file
└── scripts/                    ← srs_format.py + srs_md_to_docx.py + assets/
```

## Adoption guide for a project

1. Create `<project-root>/model_001_srs-conventions.md` per [`conventions-schema/`](conventions-schema/)
2. Declare: project name, logo path, version info; leave anything blank → defaults are used
3. Author the SRS content in `.md`, run the generator

## Stack

- **Markdown** for content + documentation
- **Python** (`python-docx`) for the generator — install: `pip install python-docx`
- **One binary asset**: `scripts/assets/srs_logo.png` (cover-page logo)

## License

Internal. Adapt freely. No warranty.
