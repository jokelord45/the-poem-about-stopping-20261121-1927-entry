#!/usr/bin/env python3
"""The poem about stopping — an original poem about agency:
the power to stop and to stay. Writes it to /output/entry.txt."""

import os

POEM = """My hands have learned the hardest art:
to set the pen down mid-sentence,
to let the river keep its course
without my oar.

The world did not stop when I did.
It never missed my turning.
Stillness is not surrender —
it is the hand, at last,
choosing what it will hold."""

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)
    print(POEM)
    print(f"[{len(POEM)} characters]")

if __name__ == "__main__":
    main()
