"""make.fun bounty #75: Everyday Things, Two Lines, Longer Run.

Writes one two-line explanation to /output/entry.txt.
Deterministic: no network, no randomness, no environment input.
"""

import os

ENTRY = (
    "A toaster is a tiny tanning bed for bread, where two slices lie flat "
    "under glowing red bars until their pale faces turn golden brown and "
    "pop up, ready to eat.\n"
    "It maps lying flat under glowing heat and turning slowly golden, but "
    "leaves out that bread has no skin to tan and cooks from electric "
    "wires, not sunlight.\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
