# Find My Job v1

A ChatGPT-first skill for finding fresh, verified jobs that fit a candidate's real constraints. It works directly in a phone conversation with no computer, Python, or plugin installation required. Desktop installation is optional.

## Start on a phone — no computer required

In the ChatGPT mobile app, send this repository link with the message:

> Load the Find My Job instructions from https://github.com/mysteriousboogey/findmyjob and start my job-search setup now. Use ordinary web search; do not require desktop installation.

If ChatGPT confirms that the instructions are loaded, the setup is complete for that conversation. It must begin onboarding immediately—not stop to discuss permanent installation. Keep that conversation for future searches.

For a reusable mobile home, create a Dot named **Find My Job** in the ChatGPT mobile app when Dots are available on the account, then send it the same message. A Dot can be created and used entirely on a phone. If Dots are unavailable, the original conversation still works. See [MOBILE_SETUP.md](MOBILE_SETUP.md).

Because this repository is private, the phone's ChatGPT account must be able to access it. Anyone without repository access can instead copy [PORTABLE_PROMPT.md](PORTABLE_PROMPT.md); that works in ChatGPT or another web-search-capable AI without installing anything.

## Optional desktop installation

Desktop users may register the private marketplace so Find My Job appears across new supported conversations:

> Add `mysteriousboogey/findmyjob` as a plugin marketplace, install `find-my-job`, then use `$find-my-job` to find jobs for me.

[Open one-link setup in the ChatGPT desktop app](codex://new?prompt=Add%20mysteriousboogey%2Ffindmyjob%20as%20a%20plugin%20marketplace%2C%20install%20find-my-job%2C%20then%20use%20%24find-my-job%20to%20find%20jobs%20for%20me.)

This desktop step is optional and must never block phone use. Installation support and workspace policy vary; the link does not silently grant repository or scheduling permissions. The plugin is a small set of readable instructions and helper files—not an application that can silently control the computer.

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

## License

[MIT](LICENSE) — use, modify, and share it while keeping the license notice.
