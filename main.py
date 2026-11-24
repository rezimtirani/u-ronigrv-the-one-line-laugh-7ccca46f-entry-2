"""Second One-Line Laugh entry: a programmer's confession.

The humour comes from a familiar developer habit: the fix itself is
trivially destructive, and the real work goes into making the commit
history look deliberate afterwards.
"""

import os
import sys
from pathlib import Path


def build_line():
    """Return the single joke line this entry submits."""
    return (
        "I fixed the bug by deleting the code that caused it, then spent "
        "an hour writing a commit message that made it sound intentional."
    )


def check_line(text):
    """Refuse anything that breaks the gate: one line, 1-200 chars."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    if len(stripped) > 200:
        raise ValueError("entry must be at most 200 characters")
    if "\n" in stripped:
        raise ValueError("entry must be a single line")
    return stripped


def emit(text):
    """Write the checked line to the grader's output directory."""
    base = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    base.mkdir(parents=True, exist_ok=True)
    target = base / "entry.txt"
    target.write_text(text, encoding="utf-8")
    return target


def verify_written(target, expected):
    """Read the file back and confirm it holds exactly the checked line."""
    stored = target.read_text(encoding="utf-8")
    if stored != expected:
        raise ValueError("written entry does not match the checked line")
    if stored.count("\n") > 0:
        raise ValueError("written entry must be a single line")
    return len(stored)


def run():
    line = check_line(build_line())
    target = emit(line)
    verify_written(target, line)
    print(line)


if __name__ == "__main__":
    sys.exit(run())
