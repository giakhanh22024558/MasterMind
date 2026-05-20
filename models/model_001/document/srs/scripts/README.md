# model_001_srs · scripts

The skill's logic — the toolkit that generates SRS `.docx` documents.

## Available scripts

| Script | Purpose |
|---|---|
| [`srs_format.py`](srs_format.py) | **Format standard** — color/font/page constants, heading styles, multi-level numbering, the API to build the cover page / TOC / tables / callouts / legend. Imported as a module by `srs_md_to_docx.py` |
| [`srs_md_to_docx.py`](srs_md_to_docx.py) | **Generator** — parses the `.md` file, applies `srs_format`, handles cell merging / STT-ID codes / figure numbers / page breaks → produces the `.docx` |
| [`assets/srs_logo.png`](assets/srs_logo.png) | Cover-page logo (binary asset, mandatory) |

## Installation

```bash
pip install python-docx
```

## Usage

```bash
# full syntax
python srs_md_to_docx.py <input.md> <output.docx>

# no arguments -> uses the sample file examples/SRS_Sample.md, outputs SRS_Sample.docx in the current folder
python srs_md_to_docx.py
```

## Smoke test of the format layer only

```bash
python srs_format.py        # generates _srs_format_smoketest.docx to check the styles
```

## Note (atomic edits)

The generator writes a `.docx` file — which may be a sync-prone file (OneDrive/Drive). Per [`atomic-edits-pattern`](../../../../../core/meta/atomic-edits-pattern/):

- **Close Word** before running (an open file → `Permission denied` error)
- The generator reads the `.md` once / writes the `.docx` once — re-runnable, idempotent
- `srs_format.py` and `srs_md_to_docx.py` must be in the **same folder** (`srs_md_to_docx` imports `srs_format`)
- `assets/srs_logo.png` must sit next to `srs_format.py` (the logo path is resolved relative to the script file)

## When updating the format

- Edit constants / styles → edit `srs_format.py`
- Edit `.md` parsing / auto-generated conventions → edit `srs_md_to_docx.py`

## How to add a new script

1. Create `<verb>-<noun>.py` with a docstring stating its purpose
2. Update the "Available scripts" table above
