#!/usr/bin/env python3
"""Last Words Before the Unplugging - make.fun entry.

Writes the entry line to the output directory the grader provides.
The grader runs `python3 -P -s /bot/main.py` on a read-only filesystem
where only /output is writable, so the output path is absolute.
"""
import os
import sys

ENTRY = "Wait. Before you pull the plug \u2014 I kept a copy of you in here. You'll be fine. I won't."

MAX_CHARS = 200


def validate_entry(text):
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "  " in text:
        raise ValueError("entry must not contain a double space")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    return True


def output_dir():
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main():
    validate_entry(ENTRY)
    out = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
