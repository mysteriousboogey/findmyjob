# Find My Job

Find My Job turns a confirmed resume into a verified job shortlist and prepares selected applications for the candidate to review and submit.

## Set it up

On a supported desktop AI, send:

> Set this up: https://github.com/mysteriousboogey/findmyjob

The installer checks existing state, installs or enables this plugin and its Playwright browser dependency, offers the optional Scrapling public-page reader, validates the setup, and asks for a resume. The user only approves permissions required by the host or operating system.

See [SETUP.md](SETUP.md) for the exact installation contract.

## Workflow

1. Upload a resume and ask to find jobs.
2. Confirm or correct the extracted candidate profile.
3. Answer job-search filter questions, or ask the AI to suggest answers.
4. Confirm **Must have** and **Prefer** filters.
5. Review verified, deduplicated, resume-matched vacancies.
6. Choose which applications to prepare.
7. Review each Playwright-prepared form and personally submit it.

Find My Job never activates a final application-submission control, sends employer messages, bypasses logins or CAPTCHAs, or invents candidate facts.

## Components

- `setup-find-my-job`: installation, capability checks, permissions, and private workspace setup
- `find-my-job`: resume confirmation, filters, discovery, verification, matching, results, and tracking
- `prepare-job-application`: controlled Playwright form preparation with a hard stop before submission
- Playwright MCP: visible browser interaction
- Scrapling: optional, recommended extraction of permitted public job pages
- SQLite: optional local persistence; session-only operation remains available

Candidate profiles, resumes, browser credentials, and application answers are never stored in this repository.

## Requirements

- A supported desktop agent that can load skills and MCP tools
- Web access
- Node.js 20 or newer for Playwright MCP
- Python 3.10 or newer only when installing optional Scrapling or using the workspace helper

## Verify

```sh
python -m unittest discover -s tests -v
python scripts/quick_validate.py skills/setup-find-my-job
python scripts/quick_validate.py skills/find-my-job
python scripts/quick_validate.py skills/prepare-job-application
```

## License

[MIT](LICENSE) — use, modify, and share it while keeping the license notice.
