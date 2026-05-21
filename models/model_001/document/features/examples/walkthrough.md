# Example · feature list walkthrough

A short worked example — deriving features from a requirements table. Generic "RoomBooking" scenario.

## Input — the requirements table

| Req code | Topic | Criteria |
|---|---|---|
| REQ-0001 | Booking | Create a booking |
| REQ-0002 | Booking | Cancel a booking |
| REQ-0003 | Rooms | Room catalogue |

## Step 1 · Group requirements into features

- `REQ-0001` + `REQ-0002` (both `Booking`) → one feature, "Booking management".
- `REQ-0003` → "Room catalogue".

## Step 2 · Write the feature list

One row per user story; feature-level cells filled on the feature's first row.

```markdown
| Feature ID | Feature Name | Ref. Req (Feature) | Description (Feature) | User Story | Ref. Req (Story) | Description (Story) | Priority | Ready? | Done? | In Scope |
|---|---|---|---|---|---|---|---|---|---|---|
| FEAT-0001 | Booking management | REQ-0001, REQ-0002 | Members create and cancel bookings. | A member can book an available room. | REQ-0001 | Pick a room + slot. | High | ☑ | ☐ | In scope |
| | | | | A member can cancel their booking. | REQ-0002 | Before start time only. | Medium | ☑ | ☐ | |
| FEAT-0002 | Room catalogue | REQ-0003 | Admin maintains rooms. | An admin can add or edit a room. | REQ-0003 | Name + capacity. | Medium | ☐ | ☐ | Next phase |
```

## Step 3 · Render

`features.xlsx` is generated into `output/`: `Priority` and `In Scope` as dropdowns, `Ready?` / `Done?` as `☐`/`☑` checkboxes, and the feature-level cells merged across each feature's story rows.

## Recap

- ✅ Every feature cites its `REQ-` codes.
- ✅ User stories kept short — `[User] can [Action]`.
- ✅ `FEAT-` codes sequential.
