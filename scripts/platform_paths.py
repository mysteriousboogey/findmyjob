"""Resolve Find My Job's private data directory without third-party packages."""

import os
import platform
from pathlib import Path


def data_dir() -> Path:
    override = os.environ.get("FIND_MY_JOB_DATA_DIR")
    if override:
        return Path(override).expanduser()

    system = platform.system()
    if system == "Windows":
        base = os.environ.get("LOCALAPPDATA") or os.environ.get("APPDATA")
        return Path(base) / "Find My Job" if base else Path.home() / "Find My Job"
    if system == "Darwin":
        return Path.home() / "Library" / "Application Support" / "Find My Job"
    return Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share")) / "find-my-job"
