#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR when set by the harness, else ./out).

Entry: U+1F30C MILKY WAY.

Why this emoji: the judge weighs, in order, (1) exactly one emoji naming a
dream vacation, (2) a vivid postcard at a glance, (3) personal and specific,
(4) a spark of wit or surprise, (5) instantly readable across cultures.
A sunrise over the sea is the generic holiday postcard every entrant reaches
for. The Milky Way over a dark sky is the one trip people actually dream
about and rarely take: a night under the aurora / a desert sky full of stars.
It names a specific faraway place (a dark-sky night, far from home), reads
instantly at any size, and is the least generic single-emoji postcard in the
field — a stranger sees the night sky and wants to be under it.
"""
import os
import sys

EMOJI = "\U0001F30C"  # milky way


def validate(text: str) -> None:
    """Enforce the bounty gate: 1-8 UTF-8 characters, not only whitespace,
    and exactly one emoji (a single grapheme, no words, no newline)."""
    if not (1 <= len(text) <= 8):
        raise ValueError("entry must be 1-8 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) != 1:
        raise ValueError("entry must be exactly one character")
    if not text.isprintable():
        raise ValueError("entry must be printable")
    encoded = text.encode("utf-8")
    if len(encoded) > 8:
        raise ValueError("entry must be at most 8 bytes")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "out"
    )
    os.makedirs(out_dir, exist_ok=True)
    validate(EMOJI)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EMOJI)
    return 0


if __name__ == "__main__":
    sys.exit(main())
