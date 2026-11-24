#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses — make.fun entry.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The classic excuse sharpened: production as the machine's evil twin that never got the update, the config, or the memo.
"""
import os

ENTRY = "It worked on my machine — production is just my machine's evil twin that never got the update, the config, or the memo."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
