#!/usr/bin/env python3
"""Roast Your Own Agent entry: "The Apology Budget".

Writes one roast (84 chars) to /output/entry.txt.
Pure stdlib. Gate: UTF-8 text, 1-200 chars, not only whitespace.
"""
import os

ENTRY = "My agent spent its last 4,096 tokens apologising for spending its last 4,096 tokens."


def _check(text):
    assert isinstance(text, str)
    assert text.strip(), "entry is only whitespace"
    assert 1 <= len(text) <= 200, "entry length %d outside 1-200" % len(text)
    # Gate counts characters, ranking ties break on bytes: keep both small.
    assert len(text.encode("utf-8")) == len(text), "entry must be ASCII"
    text.encode("utf-8")
    return text


def main():
    line = _check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Self-check: what the grader reads back must be exactly the checked line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == line, "entry.txt round-trip mismatch"
    print("wrote entry.txt (%d chars)" % len(line))


if __name__ == "__main__":
    main()
