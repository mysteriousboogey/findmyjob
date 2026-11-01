#!/usr/bin/env python3
"""Check or install optional Scrapling in an isolated local environment."""

import argparse
import importlib.util
import json
import subprocess
import sys
import venv

from platform_paths import data_dir


def isolated_python():
    root = data_dir() / "tools" / "scrapling"
    executable = root / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
    return root, executable


def available():
    if importlib.util.find_spec("scrapling") is not None:
        return True, sys.executable
    _, executable = isolated_python()
    if not executable.exists():
        return False, None
    result = subprocess.run(
        [str(executable), "-c", "import scrapling"],
        capture_output=True,
        timeout=30,
    )
    return result.returncode == 0, str(executable)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--install", action="store_true")
    args = parser.parse_args()

    present, executable = available()
    if present or not args.install:
        print(json.dumps({"available": present, "installed": False, "python": executable}))
        return 0

    root, executable = isolated_python()
    try:
        root.parent.mkdir(parents=True, exist_ok=True)
        venv.EnvBuilder(with_pip=True).create(root)
        subprocess.run(
            [str(executable), "-m", "pip", "install", "scrapling>=0.5"],
            check=True,
            capture_output=True,
            text=True,
            timeout=300,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        print(json.dumps({"available": False, "installed": False, "fallback": "web search and Playwright", "error": str(exc)}))
        return 0

    present, executable = available()
    print(json.dumps({"available": present, "installed": present, "python": executable, "fallback": None if present else "web search and Playwright"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
