# Pattern · Content / Format separation (content-in-md, format-in-python)

The foundational pattern of the `model_001_srs` skill.

## Problem

When authoring a technical document directly in Word:

- The author juggles content and formatting at once → loss of focus, inconsistent formatting
- A global format change (heading color, font) must be applied by hand in many places
- Identifier codes (STT/ID, figure numbers) and heading numbering written by hand → easy to duplicate or misalign
- Hard to review content because it is mixed with presentation markup
- Every new document rebuilds the formatting from scratch

## Solution

Separate the two concerns into two independent layers:

| Layer | Where it lives | Holds |
|---|---|---|
| **Content** | `.md` file | Words, heading structure, tables, bullets — NO presentation formatting |
| **Format** | Python code | Font, color, page, numbering, cover page, table of contents, auto-generated conventions |

A **generator** combines the two layers → produces the `.docx`:

```
content.md  ──┐
              ├──▶  srs_md_to_docx.py  ──▶  output.docx
srs_format.py ┘     (generator)            (correct standard formatting)
```

- `srs_format.py` — the format standard: color/font/page constants, heading styles, multi-level numbering, the API to build the cover page / TOC / tables / callouts.
- `srs_md_to_docx.py` — the generator: parses the `.md`, applies the format, handles the auto-generated conventions.

### Consequence: the "auto-generated" conventions

Because format is code, the generator handles things that used to be hand-written:

| Convention | Mechanism |
|---|---|
| Heading numbering | Native multilevel list — `1`/`1.1`/`1.1.1`/`1.1.1.1`, H5 `A.B.C.` |
| STT/ID codes | `COM-<heading H4>-<NNN>` — derived from the table position, continuous within the same H4 |
| Figure numbers | `Hình <heading H4>-<n>` — counted per section |
| Cell merging | A row with all cells identical → merged into one cell |
| Cover page / TOC | Built from the `.md` frontmatter + a native TOC field |

→ The author leaves STT/ID cells **empty** and writes captions as `Hình [description]` with no number — the generator fills them in.

## Trade-offs

**Pros:**
- The author focuses only on content; formatting is always consistent
- A global format change = edit one place in Python, rebuild
- ID codes, figure numbers, and numbering are never duplicated or misaligned
- The `.md` file is easy to review, diff, and version-control

**Cons:**
- Requires a build step (running the script) — not instant WYSIWYG
- The author must follow the conventional `.md` structure (see [`srs-structure/`](../../srs-structure/))
- Final visual fine-tuning (image positioning…) still requires opening Word

## Worked example

See [`examples/`](../../examples/) — generating a complete SRS from `SRS_Sample.md`.

## When NOT to use

- A one-off, short document that does not need a repeatable standard format → authoring directly in Word is faster
- A document needing real-time multi-person collaboration on the same Word file

## Cross-references

- The generator writes a sync-prone `.docx` file → apply [`atomic-edits-pattern`](../../../../../../core/meta/atomic-edits-pattern/): close Word before building, build = read/write once, re-runnable.
- If a new `Loại`/`Thuộc tính` value recurs ≥3 times → consider promoting it to the canonical Legend per [`defer-then-promote-pattern`](../../../../../../core/meta/defer-then-promote-pattern/).
