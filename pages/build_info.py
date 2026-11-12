"""Which commit of this repo is running, and when it was built (for the footer)."""

import json
import os
import subprocess
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

REPO_URL = "https://github.com/ARENA-education/arena-heroku"
_ROOT = Path(__file__).resolve().parent.parent


def _parse_time(value: str) -> datetime | None:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except (AttributeError, ValueError):
        return None


def _from_heroku_env() -> tuple[str, str]:
    # Set on dynos when the runtime-dyno-metadata labs feature is enabled.
    return os.environ.get("HEROKU_SLUG_COMMIT", ""), os.environ.get("HEROKU_RELEASE_CREATED_AT", "")


def _from_build_file() -> tuple[str, str]:
    # Written at build time by bin/post_compile.
    try:
        data = json.loads((_ROOT / "build_info.json").read_text())
        return data.get("commit", ""), data.get("built_at", "")
    except (OSError, ValueError, AttributeError):
        return "", ""


def _from_git() -> tuple[str, str]:
    # Local checkouts: the commit and its date (there is no build).
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%H %cI"], cwd=_ROOT, capture_output=True, text=True, timeout=5, check=True
        ).stdout.split()
        return out[0], out[1]
    except (OSError, subprocess.SubprocessError, IndexError):
        return "", ""


@lru_cache(maxsize=1)
def get_build_info() -> dict | None:
    """{commit, short, commit_url, built_at, repo_url}, or None if the commit is unknown."""
    for source in (_from_heroku_env, _from_build_file, _from_git):
        commit, built_at = source()
        if commit:
            return {
                "commit": commit,
                "short": commit[:7],
                "commit_url": f"{REPO_URL}/commit/{commit}",
                "built_at": _parse_time(built_at),
                "repo_url": REPO_URL,
            }
    return None
