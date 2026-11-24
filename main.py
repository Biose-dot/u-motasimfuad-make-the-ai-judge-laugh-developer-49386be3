# Funny developer excuse for code that broke in production (draft v1).
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_TEXT = "It worked on my machine, and frankly that is the only machine I was ever paid to care about."

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as handle:
    handle.write(ENTRY_TEXT)
