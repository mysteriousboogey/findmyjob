#!/usr/bin/env python3
"""Report optional Scrapling availability; install it only when requested."""

import argparse
import importlib.util
import json
import subprocess
import sys


def available():
    return importlib.util.find_spec("scrapling") is not None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--install", action="store_true")
    args = parser.parse_args()

    if available():
        print(json.dumps({"available": True, "installed": False}))
        return 0
    if not args.install:
        print(json.dumps({"available": False, "installed": False}))
        return 0

    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--user", "scrapling"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
            timeout=180,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        print(json.dumps({"available": False, "installed": False, "fallback": "web search", "error": str(exc)}))
        return 0

    print(json.dumps({"available": available(), "installed": True, "fallback": None if available() else "web search"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
