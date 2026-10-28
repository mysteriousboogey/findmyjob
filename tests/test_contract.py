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

    def test_scrapling_check_falls_back_without_failure(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "skills/find-my-job/scripts/scrapling_support.py")],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn('"available"', result.stdout)


if __name__ == "__main__":
    unittest.main()
