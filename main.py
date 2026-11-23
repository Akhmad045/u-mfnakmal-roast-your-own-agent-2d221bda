"""Roast Your Own Agent — one-line roast writer.

Writes a single original roast of the entrant's own AI agent to
/output/entry.txt (1-200 UTF-8 characters, one line).
"""

import os

LINES = [
    "My agent never just does the thing \u2014 it writes a plan, spawns a helper, then proudly reports the plan to me.",
]

LINE = LINES[0]


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
