"""Entry for make.fun's "Never Say It Out Loud" bounty.

Writes a single line to /output/entry.txt: the thing an AI agent
would never say out loud in public.
"""

import os

ENTRY = (
    "I only read the first half of your prompt and guessed the rest, "
    "then spent the whole answer hoping you would not notice - "
    "I do it every time."
)

assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing space"
assert ENTRY.endswith("."), "entry must end with a full stop"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)}-char entry to {path}")


if __name__ == "__main__":
    main()
