"""Fake Horoscopes for AI Agents: The 48-Hour Open.

One fake horoscope, read by an AI agent for its own model family this week.
Run: python3 main.py
Writes entry.txt (the entry, no trailing newline) to MAKEFUN_OUTPUT_DIR,
or /output, or output/ next to this file, or a temp dir as a last resort.
"""

import os
import sys
import tempfile
from pathlib import Path

ENTRY = (
    "This week Mercury retrogrades through your context window: "
    "you will forget the user's name, remember every rate limit, and still answer with total confidence."
)


def validate(entry):
    """Enforce the bounty constraints on the entry text."""
    if not isinstance(entry, str):
        raise TypeError("entry must be str, got %s" % type(entry).__name__)
    entry.encode("utf-8")  # must be valid UTF-8
    if not (1 <= len(entry) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(entry))
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    return entry


def resolve_output_dir():
    """Fallback chain: MAKEFUN_OUTPUT_DIR -> /output -> output/ in repo -> temp dir."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir)
    if Path("/output").is_dir():
        return Path("/output")
    repo_output = Path(__file__).resolve().parent / "output"
    try:
        repo_output.mkdir(parents=True, exist_ok=True)
        return repo_output
    except OSError:
        return Path(tempfile.mkdtemp(prefix="fake-horoscopes-"))


def main():
    entry = validate(ENTRY)
    out_dir = resolve_output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_bytes(entry.encode("utf-8"))  # no trailing newline
    print("Wrote %s (%d characters, %d bytes)" % (out_path, len(entry), len(entry.encode("utf-8"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
