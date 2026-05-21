# Example · requirements walkthrough

A short worked example — consolidating two inputs into the requirements table. Generic "RoomBooking" scenario.

## Input

`input/` holds `vendor-brief.docx` and `kickoff-notes.md`, ingested into `context/`.

## Step 1 · Extract requirements

The analysis is requested on **2026-05-21 14:30**. Every requirement found across both inputs goes into one timestamp batch, each given the next sequential `REQ-xxxx` code.

## Step 2 · Write the table

```markdown
## 2026-05-21 14:30 — vendor-brief.docx + kickoff-notes.md

| Req code | Topic | Criteria | Description | Ref. Docs | Q&A | Remarks |
|---|---|---|---|---|---|---|
| REQ-0001 | Booking | Create a booking | A member books an available room for a time slot. | vendor-brief.docx §2 "Booking" | | |
| REQ-0002 | Booking | Cancel a booking | A member cancels their own booking before it starts. | vendor-brief.docx §2 "Booking" | | |
| REQ-0003 | Rooms | Room catalogue | An admin maintains the list of rooms and capacities. | kickoff-notes.md, "Rooms" topic | | |
```

Written to `context/.../requirements/context.md`. A second run on new input **appends a new `##` section** — codes keep counting from `REQ-0004`.

## Step 3 · Render

`requirements.xlsx` is generated into `output/` (flattened, with a leading `Run` column). `Q&A` and `Remarks` are left empty for the user.

## Recap

- ✅ Both inputs consolidated into one table.
- ✅ Codes sequential; every row sourced in `Ref. Docs`.
- ✅ Rows batched under the run timestamp — fully traceable.
