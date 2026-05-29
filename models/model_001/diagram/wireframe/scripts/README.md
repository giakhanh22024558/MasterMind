# wireframe · scripts

A wireframe is authored by hand (copy [`../templates/wireframe-base.html`](../templates/) and fill it in); the HTML is the source of truth, no build step. Scripts only help with **packaging for client review** (Workflow D in [`../SKILL.md`](../SKILL.md)).

## Snapshot a wireframe (HTML → PNG)

Use an installed headless browser; trim the page background with PIL.

```bash
chrome --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1.5 \
  --screenshot="snapshots/WF-NN.png" --window-size=1460,1800 "file:///…/WF-NN-<slug>.html"
```
```python
# trim the gray page margin to the white sheet
from PIL import Image, ImageChops
im = Image.open(p).convert("RGB")
bbox = ImageChops.difference(im, Image.new("RGB", im.size, im.getpixel((2, 2)))).getbbox()
im.crop(bbox).save(p)   # check bbox[3] < height-2 → not cut off at the bottom
```
Save to `output/wireframes/snapshots/`. Set `--window-size` height generously; the trim removes the excess.

## Build the client deliverable (`build-client-md.py`)

Render one Markdown for Confluence from a list of screens. Keep a `SHEETS` list of
`(label, companion_md, png, screen_title, show_assumptions, show_spec)` and, per screen, emit:
① the snapshot image `![](wireframes/snapshots/WF-NN.png)`, then — if `show_spec` — ②.A the
component-spec tables (parsed from the companion `.md`'s `## Component specification`) and — if
`show_assumptions` — ②.B the assumptions (parsed from `## Design Assumptions`). A read-only list
screen uses `show_spec=False` → snapshot only.

The script **parses the companion `.md` files** (single source of truth) so the deliverable
stays in sync — never re-type spec/assumptions.

Other optional helpers (name `<verb>-<noun>.py`):
- `new-wireframe.py` — scaffold `WF-NN-<slug>.html` + `WF-NN-<slug>.md` from the templates with the next sequence number.

## Guidance

- Any script touching a **hand-maintained** file (e.g. a Q&A workbook with filled client answers) MUST `openpyxl` **load + edit in place** — never regenerate from scratch.
- Keep scripts dependency-light (`openpyxl`, `Pillow` only — both standard in model_001 projects).
- Don't maintain the deliverable in two formats; pick one (Markdown preferred).
