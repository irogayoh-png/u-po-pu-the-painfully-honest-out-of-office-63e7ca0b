"""The Painfully Honest Out-of-Office.

Writes one painfully honest but still polite out-of-office email
auto-reply to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when that variable is set, for local testing).

The reply is a single sentence of 159 characters. It admits, in
private, something a real employee would only say privately --
that they kept promising quick replies they could not keep --
and answers it with a warm, professional promise: one honest,
careful reply instead of a rushed one. No list of complaints,
no rudeness, no cheerfulness for its own sake.
"""

import os

REPLY = (
    "Out of office until Monday: I kept promising quick replies "
    "I could not keep, so I am resting now to give you one honest, "
    "careful reply instead of a rushed one."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
