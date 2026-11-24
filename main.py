"""Last Text at One Percent — make.fun entry.

Writes the last text message a dying phone sends at one percent battery
to /output/entry.txt. Deterministic: the same line on every run.
No network, no input files, no secrets, nothing read from outside
this repository.
"""

import os

LINE = (
    "i have 1% left and i'm spending it texting you instead of "
    "calling 911. that's how much i love you. "
    "also delete my search history."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
