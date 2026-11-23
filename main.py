#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes exactly one original dad joke to entry.txt: a deadpan,
tell-it-out-loud joke with a single clean pun at the end.
Deterministic: the same run always writes the same bytes.
Standard library only, no network, no dependencies.
"""

import os

# The pun turns on "hinge": the door part, and "hinge on" (depend on).
# Setup first, punchline last, told deadpan at the dinner table.
JOKE = (
    "My kids asked me to fix the squeaky door. "
    "I said I would \u2014 but first, let me hinge on it for a bit."
)

# The gate allows 1-200 characters; keep the joke well inside it.
assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"

ENTRY_NAME = "entry.txt"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_NAME)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
