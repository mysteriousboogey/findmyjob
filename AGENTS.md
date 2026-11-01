# Repository intent

When a user says “set this up”, “install this”, or gives this repository to install Find My Job:

1. Read `SETUP.md`.
2. Inspect existing plugin and MCP state; do not create duplicates.
3. Register this repository as a plugin marketplace when the host supports it, then install or enable `find-my-job`.
4. Run `$setup-find-my-job` and complete every safe setup step automatically.
5. Ask the user only for a permission the host actually requires.
6. Finish by asking for a resume.

Setup means installing the job-search workflow, not administering this repository. Do not ask about repository visibility, branch protection, Actions, deployment, or a website. Do not modify the repository during end-user setup.

Find My Job is desktop-only. Playwright is required for application preparation. Scrapling is recommended for efficient public-page extraction but must remain optional. If either dependency is unavailable, report the exact missing capability and continue with everything that still works.

Never place candidate data, resumes, browser credentials, or application answers in this repository.
