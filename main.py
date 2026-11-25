#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun bounty entry.

Writes exactly one word to the output path (default /output/entry.txt).
"""
import sys
from pathlib import Path

WORD = "unsubscribed"


def main() -> int:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(WORD + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
