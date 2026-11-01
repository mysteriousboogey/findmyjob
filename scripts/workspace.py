#!/usr/bin/env python3
"""Create or inspect Find My Job's private local SQLite workspace."""

import argparse
import json
import os
import sqlite3

from platform_paths import data_dir


SCHEMA = """
CREATE TABLE IF NOT EXISTS metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS jobs (
    canonical_key TEXT PRIMARY KEY,
    company TEXT NOT NULL,
    title TEXT NOT NULL,
    location TEXT NOT NULL,
    source_url TEXT NOT NULL,
    apply_url TEXT NOT NULL,
    status TEXT NOT NULL,
    verified_at TEXT NOT NULL,
    evidence_json TEXT NOT NULL DEFAULT '{}'
);
CREATE TABLE IF NOT EXISTS applications (
    canonical_key TEXT PRIMARY KEY REFERENCES jobs(canonical_key),
    status TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    notes TEXT NOT NULL DEFAULT ''
);
CREATE TABLE IF NOT EXISTS reported_jobs (
    canonical_key TEXT PRIMARY KEY,
    reported_at TEXT NOT NULL
);
"""


def initialize():
    root = data_dir()
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    if os.name != "nt":
        root.chmod(0o700)
    database = root / "find-my-job.sqlite3"
    with sqlite3.connect(database) as connection:
        connection.executescript(SCHEMA)
        connection.execute("INSERT OR REPLACE INTO metadata VALUES (?, ?)", ("schema_version", "1"))
    if os.name != "nt":
        database.chmod(0o600)
    return root, database


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("path", "status", "init"))
    args = parser.parse_args()
    root = data_dir()
    database = root / "find-my-job.sqlite3"

    if args.command == "init":
        root, database = initialize()

    tables = []
    if args.command == "status" and database.exists():
        with sqlite3.connect(database) as connection:
            tables = [row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]

    print(json.dumps({"path": str(root), "database": str(database), "initialized": database.exists(), "tables": tables}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
