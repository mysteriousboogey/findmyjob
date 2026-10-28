# Scheduling

Use the host's real scheduled-task capability when available. If it is unavailable, explain the gap and provide a reusable search prompt; never pretend a schedule was created.

## Wizard

Confirm:

- saved search/profile to reuse
- schedule, default weekdays at 08:00
- timezone, default `Asia/Kuala_Lumpur`
- notifications, default on

Explain that scheduled searches report only newly discovered confirmed matches, reducing repeated review. Obtain explicit consent immediately before creating the task.

## Registry and duplicate prevention

Before creating a task, inspect existing tasks for the same candidate/search. Reuse or update the existing task instead of creating a duplicate. Keep a small registry containing task ID, profile/search identifier, schedule, timezone, notification state, last successful run, and already-reported canonical listing keys.

On each run, search using saved hard criteria, verify results, and notify only listings not already reported. Do not notify when nothing new and actionable was found unless the host requires a run-status message.

Support update, pause, resume, and delete when the host supports them. Confirm the resulting state. If a task ID is stale, reconcile it once against the host's task list before offering to recreate it.
