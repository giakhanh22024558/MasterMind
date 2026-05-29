# wireframe · conventions schema

What a project may define in `<project-root>/wireframe-conventions.md` when using this skill. All optional — unspecified keys fall back to [`conventions-defaults/`](../conventions-defaults/).

```yaml
# Output format of the wireframe deliverable
format: html            # html (default) | svg | drawio | ascii

# Where wireframes are written (relative to working folder)
output_dir: output/wireframes/

# File naming pattern. {nn} = zero-padded sequence, {slug} = kebab screen name
file_name: "WF-{nn:02d}-{slug}.html"

# Language of client-facing wireframes (labels, annotations, assumptions)
language: en            # en (default) | vi | …

# Where to log Design Assumptions (for client awareness — NOT an approval gate)
assumptions_tracker:
  kind: qa_sheet        # qa_sheet | markdown
  file: output/<project>-SRS-QA.xlsx   # if kind=qa_sheet
  sheet: "WF Assumptions"
  # file: docs/wireframe-changes.md    # if kind=markdown
  id_format: "A-WF{wf_nn}-{nn:02d}"
  # columns: ID · Wireframe · Field/Area · Assumption · Client feedback  (NO status column)

# Visual palette (decoration only — keep low-fi)
palette:
  accent: "b8860b"      # amber — reserved for component-ID badges
  new_flag: "1a7f37"    # green — "NEW vs <source>" tag
```

## Keys

| Key | Meaning |
|---|---|
| `format` | Deliverable format. Default `html` (self-contained). |
| `output_dir` | Folder for wireframe files under the working folder. |
| `file_name` | Naming pattern. Keep the `WF-NN` prefix so wireframes cross-reference the change tracker. |
| `language` | Language for client-facing labels + the Design Assumptions table. |
| `assumptions_tracker` | Where badge assumptions are recorded for client awareness (no sign-off gate). If the Q&A workbook is hand-maintained, append via load+edit. |
| `palette.accent` | Badge color. Everything else stays grayscale. |

## What is NOT configurable

- The **assumption-badge discipline** (badge ↔ table row 1:1) — core to the skill.
- **Self-contained** output (no external assets) when `format: html`.
- **Low-fidelity** intent — this skill never produces pixel-perfect visual design.
