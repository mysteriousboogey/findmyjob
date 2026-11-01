import json
import os
import pathlib
import sqlite3
import subprocess
import sys
import tempfile
import unittest


ROOT = pathlib.Path(__file__).parents[1]


class PackageTests(unittest.TestCase):
    def test_portable_plugin_declares_onboarding_and_playwright(self):
        plugin = json.loads((ROOT / "plugin.json").read_text())
        mcp = json.loads((ROOT / "mcp.json").read_text())
        self.assertEqual(plugin["extensions"]["com.openai"]["onboardingSkill"], "./skills/setup-find-my-job/SKILL.md")
        self.assertEqual(mcp["mcpServers"]["playwright"]["command"], "npx")
        self.assertIn("@playwright/mcp@latest", mcp["mcpServers"]["playwright"]["args"])
        self.assertIn("--no-webmcp", mcp["mcpServers"]["playwright"]["args"])

    def test_all_three_skills_exist(self):
        for name in ("setup-find-my-job", "find-my-job", "prepare-job-application"):
            text = (ROOT / "skills" / name / "SKILL.md").read_text()
            self.assertTrue(text.startswith("---\n"))
            self.assertIn(f"name: {name}", text)

    def test_application_skill_has_absolute_submission_boundary(self):
        text = (ROOT / "skills" / "prepare-job-application" / "SKILL.md").read_text()
        self.assertIn("Never click or activate the final submission control", text)
        self.assertIn("personally submits every form", text)
        self.assertIn("only when they confirm it", text)
        self.assertIn("CAPTCHA", text)

    def test_resume_and_filter_confirmation_are_gates(self):
        text = (ROOT / "skills" / "find-my-job" / "SKILL.md").read_text()
        self.assertIn("Do not search", text)
        self.assertIn("Ask the user to confirm both lists before searching", text)
        self.assertIn("Suggest for me", text)

    def test_workspace_initializes_private_database(self):
        with tempfile.TemporaryDirectory() as temporary:
            environment = {**os.environ, "FIND_MY_JOB_DATA_DIR": temporary}
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "workspace.py"), "init"],
                check=True,
                capture_output=True,
                text=True,
                env=environment,
            )
            database = pathlib.Path(json.loads(result.stdout)["database"])
            with sqlite3.connect(database) as connection:
                tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            self.assertTrue({"metadata", "jobs", "applications", "reported_jobs"}.issubset(tables))
            if os.name != "nt":
                self.assertEqual(database.stat().st_mode & 0o777, 0o600)

    def test_checks_are_read_only_and_report_capabilities(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check_setup.py")],
            check=True,
            capture_output=True,
            text=True,
        )
        report = json.loads(result.stdout)
        self.assertTrue(report["discovery_ready"])
        self.assertTrue(report["playwright_declared"])

    def test_scrapling_check_never_installs_without_flag(self):
        with tempfile.TemporaryDirectory() as temporary:
            environment = {**os.environ, "FIND_MY_JOB_DATA_DIR": temporary}
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "scrapling_support.py")],
                check=True,
                capture_output=True,
                text=True,
                env=environment,
            )
            self.assertIn("available", json.loads(result.stdout))
            self.assertFalse(any(pathlib.Path(temporary).iterdir()))


if __name__ == "__main__":
    unittest.main()
