#!/usr/bin/env python3
"""Last Text at One Percent.

Writes the dying phone's final text message to /output/entry.txt.
The text is fixed: one message, under 200 characters, in the voice
of a phone at one percent battery.
"""

import os

ENTRY = "i have 1% left and i'm spending it texting you instead of calling 911. that's how much i love you. also delete my search history."


def main():
    # Gate: the entry must be 1-200 characters of non-whitespace text.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
