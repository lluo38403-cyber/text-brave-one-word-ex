"""One Word From Your Ex — make.fun entry.

Writes exactly one word to /output/entry.txt: the word an ex
would use to describe the entrant, and nothing else. The word is
"Next" — the funniest, most painfully honest verdict there is:
the ex has already moved on, and the whole relationship is now
just someone waiting in line behind them.
"""

import os

ENTRY = "Next"

MAX_CHARS = 24


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    assert len(text.split()) == 1, "entry must be exactly one word"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
