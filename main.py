"""One Letter for Your Day — writes exactly one letter, Z, to entry.txt.

Z stands for "zero sleep": the word behind the letter describing the day.
The output file must be exactly 1 byte: b"Z", no newline, nothing else.
Python 3.13 stdlib only, no network.
"""

import os

# Resolve the repo dir from MAKEFUN_BOT_DIR when set; fall back to this
# script's own directory. Never rely on process.cwd() alone.
BOT_DIR = os.environ.get("MAKEFUN_BOT_DIR") or os.path.dirname(
    os.path.abspath(__file__)
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # One letter, one byte: Z. No newline, no trailing whitespace.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(b"Z")


if __name__ == "__main__":
    main()
