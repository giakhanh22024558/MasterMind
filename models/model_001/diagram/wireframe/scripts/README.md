# wireframe · scripts

No mandatory scripts — a wireframe is authored by copying [`../templates/wireframe-base.html`](../templates/) and filling it in by hand. The HTML is the source of truth; there is no build step.

Optional helper scripts a project may add here (name `<verb>-<noun>.py`):

- `log-assumptions.py` — append/replace a `WF Assumptions` sheet in the project Q&A workbook via `openpyxl` **load+edit** (preserves existing sheets/answers). Columns: `ID · Wireframe · Field/Area · Assumption · Question to confirm · Client answer · Status`.
- `new-wireframe.py` — scaffold `output/wireframes/WF-NN-<slug>.html` from the base template with the next sequence number.

Guidance:

- Any script touching a **hand-maintained** workbook (one that already has filled client answers) MUST load the existing file and edit in place — never regenerate from scratch.
- Keep scripts dependency-light (`openpyxl` only, matching the rest of model_001).
