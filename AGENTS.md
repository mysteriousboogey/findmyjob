# Repository intent

When a user says “set this up”, “install this”, or equivalent, they mean:

1. Read `SETUP.md` and register this repository as the `find-my-job` plugin marketplace when supported and not already registered.
2. Install or enable the `find-my-job` plugin for their ChatGPT account.
3. Confirm it can be selected in a new ChatGPT conversation, including on mobile when the account supports synced plugins.
4. Start Find My Job onboarding only after installation is confirmed, unless the user asks to start immediately.

Do not interpret setup as repository administration. Do not ask about repository visibility, branch protection, GitHub Actions, deployment, or building a website. Do not change the repository. Inspect existing plugin state first and avoid duplicate marketplace or plugin entries.

If permanent plugin installation is unavailable because of the account, workspace policy, or client capability, state the exact limitation and continue using the skill instructions in the current conversation. Do not stop halfway.
