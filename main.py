#!/usr/bin/env python3
"""The Most Honest Outage Line: one line, 160 characters or fewer.

Writes one original status page line from an AI agent during a total
server outage to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.

Draft line (v1): every server the agent runs on is down, including the
very servers it would use to check what failed, and the agent admits
it does not know the cause and cannot say when service will return.
Plain first person, specific about what is down, no invented cause,
no ETA.

Revision 2: tightened the line and put the agent itself in the first
words ("I am down with every server I run on") so it reads as the
agent reporting on itself, not a detached bulletin; folded the two
unknowns (cause, return time) into one clause, which reads more like
a real status page and frees characters without losing any admission.
"""
import os

LINE = (
    "I am down with every server I run on, including the ones I "
    "would use to check what failed. I do not know the cause or "
    "when service will return."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 160, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be one line"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
