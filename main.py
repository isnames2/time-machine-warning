"""Funniest time machine warning label, for make.fun.

Writes one warning label (111 characters, under the 120-character gate)
to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
from pathlib import Path

LINE = (
    # 111 characters, under the 120-character gate.
    # The grandfather paradox, phrased as a straight-faced safety notice:
    # the surprise lands in the last few words.
    "WARNING: Never meet your own grandfather. If you already have, "
    "please return this machine before you were born."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
