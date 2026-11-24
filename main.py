#!/usr/bin/env python3
"""Entry for make.fun: One-Liner Marathon.

Writes one original single-line comedy joke (at most 280 characters)
to /output/entry.txt. Pure standard library, no network, no reliance
on the working directory: every path is absolute.
"""

import os
from pathlib import Path

JOKE = (
    "My AI assistant said it fixed my burnout, then billed me for "
    "the therapy session it scheduled with itself."
)

# Why this line: the setup is a relatable modern frustration (burnout
# and an AI helper promising to fix it), the turn is concrete and
# specific (a bill, a therapy session, scheduled with itself), and the
# punchline lands on the last word -- the assistant treating itself as
# both therapist and client while the human pays. Short, human-voiced,
# and retellable in one breath.


def main() -> None:
    line = JOKE
    if not 1 <= len(line) <= 280:
        raise ValueError(f"entry line is {len(line)} characters, must be 1-280")
    if not line.strip():
        raise ValueError("entry line must not be only whitespace")
    if line != line.strip():
        raise ValueError("entry line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    target = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != line:
        raise ValueError("entry.txt read-back does not match the joke")
    # Report what landed, so a human running the entry can see the
    # exact bytes the judge will compare: the line plus its length.
    print(f"{len(written)} chars: {written}")


if __name__ == "__main__":
    main()
