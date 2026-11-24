#!/usr/bin/env python3
"""Two Lines to Your Past Self.

Writes exactly two lines to /output/entry.txt:
  line 1 - a warning to my past self about one specific moment
           (2 a.m., outside the Blue Note, taking Marcus's keys);
  line 2 - one sentence on why that moment mattered and what
           changed because of it.
Gate: UTF-8 text, 1-280 characters, not only whitespace.
Pure standard library, no input, no network, no secrets.
"""

import os

ENTRY = (
    "Don't take the keys from Marcus at 2 a.m. outside the Blue Note "
    "when he says you're fine to drive.\n"
    "That one ride cost you your leg, your scholarship, and ten years "
    "of mornings spent learning to walk again."
)


def main() -> None:
    text = ENTRY
    lines = text.split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() for line in lines), "no blank lines"
    # Each line must be a single sentence: it ends with one full stop
    # and contains no sentence break (". " followed by a capital).
    # Note "2 a.m." carries periods, but none of them ends a sentence,
    # so a plain period count would wrongly reject line 1.
    import re

    for line in lines:
        assert line.endswith("."), "each line ends with a full stop"
        assert re.search(r"\.\s+[A-Z]", line) is None, \
            "each line must be a single sentence"
    assert 1 <= len(text) <= 280, "entry must be 1-280 characters"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
