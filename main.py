#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, best laugh wins.

Writes a single-line roast of a smart fridge to /output/entry.txt.
Deterministic, no network, standard library only.
"""

import os

ROAST = (
    "My smart fridge beeps like a tiny landlord every time I open "
    "the door, charging me rent in cold air for the crime of "
    "standing there deciding."
)


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    line = ROAST.strip()
    assert "\n" not in line, "roast must be a single line"
    assert 1 <= len(line) <= 160, f"roast must be 1-160 chars, got {len(line)}"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what was actually written: one line, 1-160 chars, no newline.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "written content differs from roast"
    assert "\n" not in written and 1 <= len(written) <= 160
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
