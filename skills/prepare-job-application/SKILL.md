---
name: prepare-job-application
description: Prepare a user-selected, verified job application in a visible browser using confirmed candidate facts. Use only after the user chooses a job; never perform the final submission action.
---

# Prepare a Job Application

Prepare one selected application at a time with Playwright. The candidate reviews and personally submits every form.

## Preconditions

Require a user-selected job, a recently verified canonical application URL, and a confirmed candidate profile. Re-verify that the vacancy is open immediately before preparation. Ask before disclosing the candidate's data to a new employer when the user's selection did not already make that intent clear.

Read [references/form-fields.md](references/form-fields.md) before filling. Use a visible browser. Let the user complete login, CAPTCHA, account creation, and any authentication challenge; never request or store their password.

## Prepare

1. Inspect the whole application flow and identify its steps and final submission control.
2. Fill confirmed factual fields only.
3. Ask the user for missing, ambiguous, sensitive, or legal declarations.
4. Draft narrative answers from confirmed evidence, label them as drafts, and obtain review before using them.
5. Upload only the resume and documents the user approved for this job.
6. Validate required fields and summarize everything entered.
7. Stop on the final review page before any action that could submit, send, finish, complete, or confirm the application.

Never click or activate the final submission control, even after a general approval to prepare applications. Never send an employer message. Never invent experience, achievements, dates, qualifications, salary, authorization, availability, or legal answers.

If a button's effect is ambiguous, do not activate it until it is proven non-submitting. If the site auto-submits on the last field, file upload, or navigation action, stop before that action and hand control to the user.

Give the user a final review summary covering the employer and role, attached documents, filled sections, drafted answers, user-supplied sensitive declarations, unresolved items, and the exact control they must use to submit.

After the user returns, ask whether they submitted successfully. Update tracking to `user_confirmed_submitted` only when they confirm it.
