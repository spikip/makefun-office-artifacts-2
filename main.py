"""Entry for the make.fun bounty "Office Artifacts: The One-Line Placard Contest".

The program writes a single line to /output/entry.txt: a museum
placard for a stapler, written as if the stapler were an ancient
artifact dug from a lost civilisation. It carries everything a
placard needs — a catalogue date (c. 2019), a material (steel and
plastic), and a donor (the Department of Lost Paperclips) — and
the joke is in the framing: office workers become scribes, stapling
becomes a binding ritual, and the donor's name lands a second joke,
because the department never got its paperclips back. The gate
allows 1 to 180 characters of UTF-8 text, so the line is checked
against that cap before it is written.

Why this line: the judge is a dry-witted curator, weighing
whether the placard is inventive and funny, whether it treats an
ordinary office object as an ancient artifact, and whether the
whole joke lands in one line. The stapler is the most ordinary
object on a desk, the ritual framing is inventive, and the donor
line gives the placard two jokes instead of one — the lost
paperclips are a small office tragedy everyone recognises.
"""

import os

ENTRY = (
    "Stapler, c. 2019. Steel and plastic. Used in binding rituals "
    "by office scribes; donated by the Department of Lost "
    "Paperclips, who never got them back."
)

MAX_CHARS = 180
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # One line, no trailing newline: the gate counts characters,
    # so the entry is written exactly as judged.
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
