#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — round-2 resubmit entry for make.fun.

Running this script writes the one-line sick-day excuse to
/output/entry.txt. The output is fully deterministic: the exact
same line is produced on every run.

Round 2 line (127 characters): a sneeze count from the morning
standup, escalated by HR into a weather event. Two beats, twist
in the final clause, specific numbers (34 times, 8:15), named
character (Sarah from HR) — the structure the finalized one-liner
winners share (see variants.md).
"""

import os
import sys


def validate_line(line: str) -> None:
    """Check that the entry is one non-blank line of 1-200 characters.

    Exits with a non-zero status and a loud error message if the
    line is empty, spans multiple lines, or is over the limit,
    so a bad line can never ship unnoticed.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)


# The entry itself: one fixed line, 127 characters, no trailing newline.
# Structure: two beats (sneeze count, then the 8:15 standup) with the
# reveal in the final clause — HR reclassifies the sneezer as a weather event.
# Judge criteria from RULES.txt: the setup stays half-believable (a real
# standup, a real sneeze count) while the twist near the end is the bigger laugh.
LINE = "Can't come in — I sneezed 34 times during the 8:15 standup and Sarah from HR has officially reclassified me as a weather event."


def main() -> None:
    # Validate first, then write the line to entry.txt.
    # The output must stay byte-exact (129 bytes, no trailing newline):
    # any change to LINE or to this write step changes the entry itself.
    # Entry constraints enforced by validate_line above: exactly one line,
    # 1-200 characters, and deterministic output — the same bytes on every run.
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
