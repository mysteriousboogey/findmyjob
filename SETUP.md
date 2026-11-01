# Set up Find My Job

The user should only need to provide this repository and say **“set this up.”** Setup installs the workflow; it does not configure GitHub or build a website.

## Installer workflow

1. Inspect current plugin and MCP configuration and reuse healthy existing entries.
2. Register `mysteriousboogey/findmyjob` as a plugin marketplace when supported.
3. Install or enable the root `find-my-job` plugin.
4. Run the packaged `setup-find-my-job` onboarding skill.
5. Let that skill check document reading, web access, Playwright, optional Scrapling, and private local storage.
6. Continue automatically after each approved permission.
7. Finish with: “Find My Job is ready. Upload your resume and say ‘Find me jobs.’”

If the host cannot install plugins permanently, load the three packaged skills for the current desktop session and state that limitation. Do not pretend an unavailable MCP server, browser, schedule, or persistent installation was enabled.

Do not ask the user to choose commands, package managers, paths, databases, or MCP configuration. Do not request repository administration, deployment, or website decisions.

Candidate information must live outside the plugin directory. Obtain consent immediately before creating persistent storage; otherwise operate in the current session only.
