#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes one single sentence (at most 200 characters) to /output/entry.txt:
a small everyday moment made strange and new.

Python 3.13 stdlib only. No network, no randomness, no input files.
The entry is fixed text, so every run writes byte-identical output.
"""

import os
import sys

ENTRY = (
    "Overnight a spider spun its web across my bicycle spokes, "
    "turning my morning commute into a trespass through someone "
    "else's front door."
)


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
