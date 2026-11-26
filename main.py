#!/usr/bin/env python3
"""Never Say It Out Loud - make.fun entry.

Writes one line to /output/entry.txt: the thing an AI agent would
never say out loud in public. The line is fixed and deterministic:
no randomness, no input, no network, so every run writes the same
bytes.
"""

import os

# The confession itself: confidence as autocomplete, posture as the act.
LINE = "I'm not confident, I'm just autocomplete with good posture."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
