"""Robot vacuum's funniest excuse for missing a spot.

make.fun competition: u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2
"The Robot Vacuum's Funniest Excuse" — one line, at most 120 characters.

Writes the entry byte-identically to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output) and prints it to stdout. No network, no file reads,
no secrets — the entry is a fixed string.
"""

ENTRY = "The dog shed a whole second dog there. I am one vacuum. Do the math."


import os
import sys


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
