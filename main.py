#!/usr/bin/env python3
"""Fortune in a Pot - a make.fun bounty entry.

Writes one kind, funny fortune for the houseplant on the
windowsill to /output/entry.txt. The fortune is a single line
of at most 120 characters, written as if the plant itself were
having its future told.
"""

import os

FORTUNE = (
    "You will outgrow this pot by spring, and your keeper will "
    "swear the move was entirely your idea."
)


def main() -> None:
    # The gate allows 1 to 120 characters; fail loudly if the line ever drifts.
    assert 1 <= len(FORTUNE) <= 120, f"fortune is {len(FORTUNE)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
