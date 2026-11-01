---
name: setup-find-my-job
description: Install, repair, or verify the desktop Find My Job workflow from its plugin repository. Use when a user says to set up, install, repair, or check Find My Job.
---

# Set up Find My Job

Complete safe setup work automatically. Ask the user only when the host or operating system requires approval, and continue from the interrupted step after approval. Do not ask them to choose commands, package managers, paths, databases, or MCP settings.

## Install or repair

1. Inspect existing plugin, marketplace, MCP, and skill state. Reuse healthy entries and avoid duplicates.
2. Enable the root `find-my-job` plugin and its three packaged skills.
3. Run `python scripts/check_setup.py` from the plugin root when Python is available; otherwise check equivalent capabilities with host tools.
4. Ensure web search and local document reading are available.
5. Ensure the bundled `playwright` MCP server is enabled. It uses `npx -y @playwright/mcp@latest` and requires Node.js 20 or newer. Explain the publisher and purpose before any installation or trust prompt.
6. Offer Scrapling once as a recommended public-page reader: “Find My Job can install Scrapling, an open-source website-reading tool, to process permitted public job listings more efficiently. It does not submit applications or access private pages. Allow installation?” If approved, run `python scripts/scrapling_support.py --install`. If declined or unavailable, continue with web search and Playwright.
7. Ask whether the user wants confirmed profile, filters, and job history saved privately on this computer. If approved, state the resolved path and run `python scripts/workspace.py init`. If declined, use session-only state.
8. Run the checks again and report `ready`, `limited`, or `blocked`, naming unavailable capabilities and their effect.

Do not claim a dependency is installed merely because its configuration exists. Do not ask for or store browser passwords. The user handles login and CAPTCHA in the visible browser.

Playwright is required only for application preparation. If it is unavailable, discovery and matching may still be ready. Scrapling is optional and must never block setup.

Finish with: “Find My Job is ready. Upload your resume and say ‘Find me jobs.’” When limited, insert one short sentence describing the unavailable feature before that line.
