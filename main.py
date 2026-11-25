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
    # Self-check the competition gate before writing: exactly two
    # non-empty lines, total at most 400 characters (output unchanged).
    lines = ENTRY.split("\n")
    assert len(lines) == 3 and lines[2] == "", "entry must be exactly two lines"
    assert all(line.strip() for line in lines[:2]), "each line must be non-empty"
    assert len(ENTRY) <= 400, "entry must be at most 400 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
