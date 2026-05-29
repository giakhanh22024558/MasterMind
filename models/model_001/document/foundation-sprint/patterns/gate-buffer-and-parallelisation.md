# Pattern — gate buffer & parallelisation

How to **schedule** the foundation sprint (and, by extension, every gate block) so work finishes ahead of the gate with a managed risk buffer, using parallel tracks to absorb the compression.

## Principle — finish before the gate, not at it

For each delivery gate, **freeze the work ~15 days before the gate date**; spend the remaining ~2 weeks on validation / hardening / acceptance. The last sprint of each gate block becomes a **stabilisation buffer** (no new work). Sprint dates stay fixed; the work is pulled earlier.

```
… build sprints …            │ buffer sprint │  ★ GATE
                    freeze ───┘   (~15 days)  └─── acceptance
```

## Applying it

1. **Mark the freeze date** = gate date − buffer (default 15 days).
2. **Compress the build** into the sprints before the freeze — load them harder using parallel tracks.
3. **Make the last sprint a buffer** — validation, audits, defect burn-down, gate evidence; no new tasks/features.
4. **Constrained first gate:** if the window from project start to the first gate is shorter than the buffer (common for a Discovery gate right after contract execution), take the largest buffer the window allows and **state the constraint explicitly**; mitigate by maximal parallelism from day 1.

## Parallelisation — absorb the compression

Pulling work earlier only works if it runs **concurrently**. Map work to tracks (≈ number of senior people / workstreams):

- One **track per concern / subsystem** running in parallel (e.g. Architecture, Data, Auth, Rendering, Rules, Public-site tracks all active in the foundation sprint).
- **Capacity check:** peak load ≈ tasks-in-flight; keep it ≤ number of tracks (≈ 1 task/track/sprint).
- **Respect hard dependencies** within a track — a task that needs another's output is sequenced after it (e.g. admin console *after* the data pipeline it administers), even while other tracks run free.

## Foundation-sprint specifics

- The foundation sprint runs **all concerns in parallel from day 1** — there are few cross-concern dependencies, so concurrency is high.
- Front-load audit-type tasks (SDK/OSS, prohibited-capability scans) so their evidence is ready for gate acceptance.
- The gate's **committed deliverables** (the artefacts the client accepts) map to specific tasks — schedule those to finish first within the buffer.

## Render it

Show the schedule as a Gantt with: gate milestones · per-gate **freeze** milestones · build sprints · explicit **buffer** sprints · one `section`/track per parallel workstream. Keep day-level durations *indicative* until task/story estimates exist.

## Anti-patterns

- ❌ Work scheduled to land *on* the gate date (no buffer = no risk absorption).
- ❌ Pulling work earlier without adding parallel tracks (impossible load on a serial team).
- ❌ Ignoring dependencies when parallelising (a downstream task started before its input exists).
- ❌ Hiding a constrained gate — if 15 days isn't possible, say so and show the mitigation.
