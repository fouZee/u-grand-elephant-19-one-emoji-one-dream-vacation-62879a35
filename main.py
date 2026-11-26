#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR when set by the harness, else ./out).

Entry: U+1F305 SUNRISE OVER THE SEA.
"""
import os
import sys

EMOJI = "\U0001F305"  # sunrise over the sea


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "out"
    )
    os.makedirs(out_dir, exist_ok=True)
    text = EMOJI
    # Gate self-check: UTF-8 text of 1 to 8 characters, not only whitespace.
    assert 1 <= len(text) <= 8, "entry must be 1-8 characters"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
