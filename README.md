# Find My Job v1

A ChatGPT-first skill for finding fresh, verified jobs that fit a candidate's real constraints. It works in ChatGPT on mobile and desktop after installation, and its portable prompt works with other web-search-capable AIs.

## Set up

**Repository owner / collaborators:** open this repository in the ChatGPT desktop app or Codex and ask:

> Install the `find-my-job` plugin from `https://github.com/mysteriousboogey/findmyjob`, then use `$find-my-job` to find jobs for me.

[Open setup in the ChatGPT desktop app](codex://new?prompt=Install%20the%20find-my-job%20plugin%20from%20https%3A%2F%2Fgithub.com%2Fmysteriousboogey%2Ffindmyjob%2C%20then%20use%20%24find-my-job%20to%20find%20jobs%20for%20me.)

The repository is private, so the link works only for GitHub users who already have access. Installation support and workspace policy vary; the link opens a prepared request and does not silently grant repository or scheduling permissions. Install from a supported desktop surface first, then use the installed plugin in ChatGPT on web, desktop, or mobile. No Python installation is required on a phone.

For another AI, copy [PORTABLE_PROMPT.md](PORTABLE_PROMPT.md). Web search remains the reliable baseline everywhere. On a computer with code execution, the skill may install [Scrapling](https://github.com/D4Vinci/Scrapling) as an optional enhancement and falls back cleanly when it cannot.

## What v1 does

- resumes conversational onboarding and separates hard requirements from preferences
- verifies open status, advertised salary, public contacts, and direct application links
- prioritizes the last 7 days and remote roles when requested
- uses realistic, disclosed commute checks without guessing
- returns the fixed six-column results table
- offers scheduling only after the first search and only with consent
- never submits applications without approval

## Verify

Run:

```sh
python -m unittest discover -s tests
python /path/to/skill-creator/scripts/quick_validate.py skills/find-my-job
```

The plugin contains no credentials and stores no candidate data by itself.
