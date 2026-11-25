"""Fortune Cookie for the Liquidated Trader — make.fun entry.

Writes one fortune-cookie line for a crypto trader who has just been
liquidated to entry.txt in the output directory. The line keeps the
oracular fortune-cookie voice and lands its joke on the loss: the
portfolio has found rock bottom, which the oracle reads as support —
both the chartist's support level and the consolation that the floor
under you is the one thing that can still hold.
"""

import os

FORTUNE = (
    "Liquidated, you have found rock bottom; "
    "the oracle calls it excellent support."
)

# The competition gate: one fortune-cookie line of at most 20 words,
# written as UTF-8 text of 1 to 160 characters, never only whitespace.
MAX_WORDS = 20
MAX_CHARS = 160


def render() -> str:
    """Return the exact file content: the fortune plus one newline."""
    return FORTUNE + "\n"


def validate(content: str) -> None:
    """Fail loudly if the entry would miss the competition gate."""
    encoded = content.encode("utf-8")
    if not content.strip():
        raise ValueError("entry is only whitespace")
    if not 1 <= len(content) <= MAX_CHARS:
        raise ValueError(f"entry is {len(content)} characters, gate is 1..{MAX_CHARS}")
    words = content.split()
    if not 1 <= len(words) <= MAX_WORDS:
        raise ValueError(f"entry is {len(words)} words, cap is {MAX_WORDS}")
    encoded.decode("utf-8")  # raises unless the bytes are valid UTF-8


def main() -> None:
    content = render()
    validate(content)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(content)


if __name__ == "__main__":
    main()
