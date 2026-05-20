---
name: model_001_srs
description: Generate IEEE 830 / ISO-IEC-IEEE 29148 Software Requirements Specification (SRS) documents in .docx format from Markdown content. Separates content (written in .md) from presentation (Python code). Automatically handles the cover page, native table of contents, multi-level heading numbering, STT/ID & figure-number generation, table-header cell merging, and callouts. Use when creating/updating an SRS, converting SRS content into a properly formatted Word file, or setting up SRS authoring conventions for a project.
---

# model_001_srs — Generate IEEE-standard SRS documents

A skill that packages the workflow for producing **Software Requirements Specification** documents to the IEEE standard in `.docx` format. Core principle: **content is written in Markdown, presentation lives in Python code** — the author focuses only on content, and the generator applies all formatting (font, color, numbering, cover page, table of contents, ID codes...).

## When to use this skill

Invoke when the user asks to:

- **Create a new SRS document** for a system/product
- **Convert SRS content** (already in `.md` or yet to be written) into a properly formatted `.docx` Word file
- **Update** an existing SRS and re-export the `.docx`
- **Set up authoring conventions** for an SRS in a project (structure, format, ID codes)
- **Check** whether an SRS document matches the standard template/format

## First step in any task

1. **Discover conventions** — look for `<project-root>/model_001_srs-conventions.md` per [`conventions-as-data-pattern`](../../../../core/meta/conventions-as-data-pattern/)
2. **Apply the project conventions** for declared items (project name, logo, version, colors...)
3. **Fall back to** [`conventions-defaults/`](conventions-defaults/) for every item not declared
4. **Acknowledge the source** when explaining a choice ("per project conventions" / "using default")

## Content modules

| Module | Purpose |
|---|---|
| [`conventions-schema/`](conventions-schema/) | Checklist of conventions a project must declare when using the skill (name, logo, version, colors) |
| [`conventions-defaults/`](conventions-defaults/) | Default formatting decoded from a standard SRS (font, color, page, numbering, ID codes) |
| [`srs-structure/`](srs-structure/) | Specification of SRS content structure — 6 parts, the repeating Detailed Specification block, legend |
| [`patterns/`](patterns/) | Reusable patterns — content/format separation, auto-generated IDs & figure numbers |
| [`examples/`](examples/) | Worked walkthrough — generate a complete SRS from a sample file |
| [`scripts/`](scripts/) | `srs_format.py` (format standard) + `srs_md_to_docx.py` (generator) |

## Workflow templates

### Workflow A · Generate an SRS .docx from Markdown content

1. **Discover project conventions** (the first step above)
2. **Author / prepare content** in a `.md` file following the structure in [`srs-structure/`](srs-structure/):
   - Frontmatter (project name, version, metadata table) → cover page
   - 6 level-1 parts; each feature = one `### Đặc tả Chi tiết — … (FEAT-XXX)` block with 5 sub-blocks
   - Leave the STT/ID and BR-code cells **empty** — the generator fills them
   - Write figure captions as `Hình [description]` — the generator numbers them
3. **Run the generator**: `python scripts/srs_md_to_docx.py <input.md> <output.docx>`
4. **Verify**: open the `.docx`, let Word refresh the table-of-contents field; cross-check the formatting against [`conventions-defaults/`](conventions-defaults/)

### Workflow B · Check whether an SRS matches the standard

1. Read [`srs-structure/`](srs-structure/) — the structure checklist
2. Read [`conventions-defaults/`](conventions-defaults/) — the format checklist
3. Compare the target document against each checklist item; report deviations

### Workflow C · Update / extend the format standard

1. Edit the format logic in [`scripts/`](scripts/) → `srs_format.py` (do NOT edit content)
2. Update [`conventions-defaults/`](conventions-defaults/) to match

## Core principles

- **Content in .md, format in Python** — never mixed; changing the format never touches content and vice versa
- **Conventions are auto-generated, not hand-written** — STT/ID codes, figure numbers, heading numbering, and cell merging are handled by the generator
- **Reuse the Legend** — only use `Loại` (type) / `Thuộc tính` (attribute) values already defined; never invent new ones
- **No hard-coded project specifics** — project name and logo are variables passed in

## Anti-patterns

- ❌ Hand-writing formatting in the `.md` (manual bold, manual alignment) — let the generator handle it
- ❌ Pre-filling STT/ID codes or figure numbers in the `.md` — the generator will overwrite them / produce duplicates
- ❌ Hard-coding the project name "LEXcentra" into the code — it must be the variable `project_name`
- ❌ Defining new `Loại`/`Thuộc tính` values outside the canonical Legend
- ❌ Editing the `.docx` directly and expecting it to sync back to the `.md` — the `.md` is the source of truth

## Cross-references to meta-patterns

| Meta-pattern | This skill uses it when |
|---|---|
| [Uniform skill structure](../../../../core/meta/uniform-skill-structure/) | The skill follows the mandatory Shape A layout |
| [Conventions as data](../../../../core/meta/conventions-as-data-pattern/) | Project conventions live in `<project>/model_001_srs-conventions.md` |
| [Atomic edits](../../../../core/meta/atomic-edits-pattern/) | The generator writes a `.docx` (a sync-prone file) — read once / write once, close Word before running |
| [Defer-then-promote](../../../../core/meta/defer-then-promote-pattern/) | When a new `Loại`/`Thuộc tính` value recurs → consider adding it to the canonical Legend |

## Stack note

This skill deviates slightly from the repo's default stack (markdown + plain text): the [`scripts/assets/`](scripts/assets/) folder contains **one binary image file** (`srs_logo.png`) — the mandatory cover-page logo. This is a necessary asset, similar to a diagram export.
