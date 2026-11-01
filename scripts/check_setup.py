#!/usr/bin/env python3
"""Report local capabilities without installing or changing anything."""

import importlib.util
import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]


def version(command):
    executable = shutil.which(command)
    if not executable:
        return None
    try:
        result = subprocess.run([executable, "--version"], capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return None
    return (result.stdout or result.stderr).strip() if result.returncode == 0 else None


def main():
    skills = ["setup-find-my-job", "find-my-job", "prepare-job-application"]
    report = {
        "python": sys.version.split()[0],
        "node": version("node"),
        "npx": version("npx"),
        "playwright_declared": (ROOT / "mcp.json").exists(),
        "scrapling_available": importlib.util.find_spec("scrapling") is not None,
        "skills": {name: (ROOT / "skills" / name / "SKILL.md").exists() for name in skills},
    }
    report["discovery_ready"] = all(report["skills"].values())
    report["preparation_ready"] = bool(report["node"] and report["npx"] and report["playwright_declared"])
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
