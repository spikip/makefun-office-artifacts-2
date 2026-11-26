#!/usr/bin/env python3
"""Museum placard for a stapler, an office artifact.

The bounty asks for a one-line museum placard for an ordinary
office object, written as if it were an ancient artifact. This
placard gives the stapler everything a real museum label carries:
a catalogue date (c. 2019), a material (steel and plastic), and
a donor (the Department of Lost Paperclips). The framing does the
joking — office workers become scribes, stapling becomes a binding
ritual — and the donor's name lands a second joke, because the
department never got its paperclips back, a small office tragedy
everyone recognises. The bounty allows one line of 1 to 180
characters, so the line is checked against that cap before it is
written to /output/entry.txt.
"""

import os

ENTRY = (
    # Two jokes in one line: the ritual framing first, then the
    # donor's lost paperclips as the kicker a curator would keep dry.
    "Stapler, c. 2019. Steel and plastic. Used in binding rituals "
    "by office scribes; donated by the Department of Lost "
    "Paperclips, who never got them back."
)

MAX_CHARS = 180
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry must not be empty")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    print(text)


if __name__ == "__main__":
    main()
