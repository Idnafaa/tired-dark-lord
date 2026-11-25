#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""The Tired Dark Lord: a 100-word villain monologue.

Writes one original monologue to /output/entry.txt. The speaker is a
dark lord who has held the Ember Crown for forty years and is quietly
done with all of it; the exhaustion lives in the pauses, the counting
of stairs, and the deflections, never in a flat announcement.
"""

import os
import sys

MONOLOGUE = (
    "Ah. The hero arrives. The prophecy said dawn, and here you are, "
    "sword first, like the others. Sit down. The stairs took you four "
    "minutes. The last one took six. I counted.\n"
    "\n"
    "You want the Ember Crown. Of course you do. Forty years, three "
    "betrayals, and one patient dragon it took to steal it. And now it "
    "lives in a drawer. Crowns chafe. Thrones are only chairs with "
    "better marketing.\n"
    "\n"
    "Here is my scheme: take it. Wear it. Discover the paperwork. The "
    "kingdom runs on forms now. Forms, and meetings. Enjoy the meetings.\n"
    "\n"
    "One last thing. The dragon retired. So did I. Just now."
)


def self_check(text):
    """Gate the monologue the way the bounty gate does."""
    if not text or not text.strip():
        raise SystemExit("entry is empty or only whitespace")
    chars = len(text)
    if not 1 <= chars <= 600:
        raise SystemExit(f"entry is {chars} characters, must be 1-600")
    words = len(text.split())
    if not 90 <= words <= 110:
        raise SystemExit(f"entry is {words} words, must be near 100")
    return words, chars


def main():
    words, chars = self_check(MONOLOGUE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(MONOLOGUE)
    # Read it back and re-gate the bytes on disk, so a partial write
    # or an encoding slip can never slip past us unnoticed.
    with open(path, "r", encoding="utf-8") as fh:
        on_disk = fh.read()
    if on_disk != MONOLOGUE:
        raise SystemExit("round-trip mismatch: file on disk differs")
    self_check(on_disk)
    print(f"wrote {path}: {words} words, {chars} characters")


if __name__ == "__main__":
    main()
