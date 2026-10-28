#!/usr/bin/env python3
"""Minimal vendored validator entry point for CI."""

import pathlib
import re
import sys

import yaml


def main():
    skill = pathlib.Path(sys.argv[1])
    text = (skill / "SKILL.md").read_text()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise SystemExit("SKILL.md has no YAML frontmatter")
    metadata = yaml.safe_load(match.group(1))
    if metadata.get("name") != skill.name or not metadata.get("description"):
        raise SystemExit("skill name/description is invalid")
    print("Skill is valid!")


if __name__ == "__main__":
    main()
