#!/usr/bin/env python3
"""Two Lines to Your Past Self -- make.fun entry.

Writes exactly two lines to /output/entry.txt:
  line 1 warns the past self about one specific moment, in one sentence;
  line 2 says in one sentence why that moment mattered and what changed.
Pure standard library only.
"""

import os
import sys

LINE_1 = "Don't leave question twelve blank on the morning of the final — write anything, even a guess."
LINE_2 = "Those three missing marks cost you the scholarship, and the job you took instead kept you unhappy for four years."

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    lines = text.strip().split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert 1 <= len(text) <= 280, "entry must be 1-280 characters"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
