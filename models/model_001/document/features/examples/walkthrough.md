# Example · feature backlog walkthrough

A short worked example — deriving an Epic → Feature → User Story backlog from a requirements table. Generic "RoomBooking" scenario.

## Input — the requirements table

| Req code | Topic | Criteria |
|---|---|---|
| REQ-0001 | Booking | Create a booking |
| REQ-0002 | Booking | Cancel a booking |
| REQ-0003 | Rooms | Room catalogue |

## Step 1 · Group into epics

Both `Booking` and `Rooms` topics serve one capability area → epic `EPIC-0001` "Booking".

## Step 2 · Define features under the epic

- `REQ-0001` + `REQ-0002` → `FEAT-0001` "Booking management".
- `REQ-0003` → `FEAT-0002` "Room catalogue".

## Step 3 · Write user stories under each feature

Each story gets a `US-xxxx` code and cites its `REQ-xxxx`.

## Step 4 · Write the feature list

One row per user story; epic-level and feature-level cells filled on the first row.

```markdown
| Epic ID | Epic Name | Feature ID | Feature Name | Ref. Req (Feature) | Description (Feature) | Story ID | User Story | Ref. Req (Story) | Description (Story) | Priority | Ready? | Done? | In Scope |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EPIC-0001 | Booking | FEAT-0001 | Booking management | REQ-0001, REQ-0002 | Members create and cancel bookings. | US-0001 | A member can book an available room. | REQ-0001 | Pick a room + slot. | High | ☑ | ☐ | In scope |
| | | | | | | US-0002 | A member can cancel their booking. | REQ-0002 | Before start time only. | Medium | | | |
| | | FEAT-0002 | Room catalogue | REQ-0003 | Admin maintains the room list. | US-0003 | An admin can add or edit a room. | REQ-0003 | Name + capacity. | Medium | ☐ | ☐ | Next phase |
```

## Step 5 · Render

`features.xlsx` is generated into `output/`: `Priority` / `In Scope` dropdowns, `Ready?` / `Done?` checkboxes, epic-level and feature-level cells merged across their rows.

## Recap

- ✅ Three-level hierarchy — `EPIC-0001` → two features → three stories.
- ✅ Every level coded; every feature/story cites its `REQ-` codes.
- ✅ User stories kept short — `[User] can [Action]`.
