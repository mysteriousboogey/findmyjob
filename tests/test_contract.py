import pathlib
import subprocess
import sys
import unittest


ROOT = pathlib.Path(__file__).parents[1]
SKILL = ROOT / "skills/find-my-job/SKILL.md"


class ContractTests(unittest.TestCase):
    def test_required_output_header_is_exactly_six_columns(self):
        text = SKILL.read_text()
        self.assertIn("| # | Job title / Company | Salary | Work arrangement | Contact | Apply |", text)
        self.assertIn("must have", text)
        self.assertIn("wait for permission", text)
        self.assertIn("May I install the optional Scrapling package", text)
        self.assertIn("continue the entire setup and search", text)
        self.assertIn("Do not say desktop installation is required", text)
        self.assertIn("immediately ask the first useful onboarding question", text)
        self.assertIn("Start every new user with an empty candidate profile", text)
        self.assertIn("Never derive candidate details", text)
        self.assertIn("state its source", text)

    def test_scrapling_check_falls_back_without_failure(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "skills/find-my-job/scripts/scrapling_support.py")],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn('"available"', result.stdout)

    def test_repository_setup_intent_is_unambiguous(self):
        instructions = (ROOT / "AGENTS.md").read_text()
        setup = (ROOT / "SETUP.md").read_text()
        self.assertIn("Do not interpret setup as repository administration", instructions)
        self.assertIn("Install or enable the `find-my-job` plugin", instructions)
        self.assertIn("including on mobile", instructions)
        self.assertIn("not to configure this GitHub repository", setup)
        self.assertIn("Do not ask about GitHub visibility", setup)


if __name__ == "__main__":
    unittest.main()
