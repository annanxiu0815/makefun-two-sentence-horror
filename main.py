"""Two-sentence horror story entry for the make.fun bounty.

Writes exactly two sentences (187 characters) to /output/entry.txt
as UTF-8 text. No network, no dependencies, deterministic.
"""

import os

STORY = (
    "The wind chimes on the roof rang at sunset, "
    "even though there was no wind at all. "
    "When I climbed up to look, every chime was a small white tooth, "
    "and the one in the middle was still warm."
)


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(STORY)
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = "output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(STORY)


if __name__ == "__main__":
    main()
