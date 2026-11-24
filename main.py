"""One Emoji, One Smile.

Writes exactly one emoji to entry.txt in the output directory.

The chosen emoji is U+1FAF6 HEART HANDS: two hands forming a heart.
It is a warm gesture aimed straight at the stranger reading it, kind
and friendly at first glance, readable the same way by anyone of any
age or background, and clearly a picked choice rather than the first
smiley that comes to mind. No irony, no in-joke, no intimacy.

Standard library only. No network. Deterministic: every run writes
the same bytes.
"""

import os

EMOJI = "\U0001faf6"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the file holds exactly the one emoji, so the
    # gate counts exactly one character.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
