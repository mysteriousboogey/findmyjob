# Find My Job v1

A ChatGPT-first skill for finding fresh, verified jobs that fit a candidate's real constraints. It works in ChatGPT on mobile and desktop after installation, and its portable prompt works with other web-search-capable AIs.

## Set up

**Repository owner / collaborators:** open this one-link setup request in the ChatGPT desktop app or Codex. It asks the agent to register this repository as a private marketplace, install the plugin, and start onboarding:

> Add `mysteriousboogey/findmyjob` as a plugin marketplace, install `find-my-job`, then use `$find-my-job` to find jobs for me.

[Open one-link setup in the ChatGPT desktop app](codex://new?prompt=Add%20mysteriousboogey%2Ffindmyjob%20as%20a%20plugin%20marketplace%2C%20install%20find-my-job%2C%20then%20use%20%24find-my-job%20to%20find%20jobs%20for%20me.)

The repository is private, so setup works only for GitHub users who already have access and whose desktop Git credentials can read it. Installation support and workspace policy vary; the link opens a prepared request and does not silently grant repository or scheduling permissions. The Find My Job plugin is a small set of readable instructions and helper files from this repository—not an application that can silently control your computer. Install from a supported desktop surface first, then use it in ChatGPT on web, desktop, or mobile. No Python installation is required on a phone.

For another AI, copy [PORTABLE_PROMPT.md](PORTABLE_PROMPT.md). Web search remains the reliable baseline everywhere.

### Optional Scrapling installation

On a computer with code execution, Find My Job may offer to install [Scrapling](https://github.com/D4Vinci/Scrapling), an open-source Python tool that helps read public job pages efficiently. Before anything is installed, the AI must explain what it is and ask permission. The normal Python package installer fetches the public `scrapling` package; users can inspect the linked source and should never bypass a security warning merely because the skill requested it.

Saying **No** is completely fine. Search may be slower and some difficult pages may not be verified, but setup and job searching continue using ordinary web search. Find My Job must not stop halfway, keep asking, or disable core features because Scrapling was declined or failed to install.

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
python scripts/quick_validate.py skills/find-my-job
```

The plugin contains no credentials and stores no candidate data by itself.
