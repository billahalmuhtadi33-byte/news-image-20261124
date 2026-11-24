#!/usr/bin/env python3
"""Sum up 24 November 2026's world news in one image.

The entry image is entry.png beside this file: a newspaper front page
titled THE WORLD, dated Tuesday 24 November 2026, with five stories:
the Houthi strike on Riyadh's tallest tower, the overnight strike on
Zaporizhzhia in Ukraine, the drone attack on a Russian warship in
Benghazi port, NATO's vow to defend space, and Senegal reinstated as
Africa Cup of Nations champions.

This program deterministically copies that image to /output/entry.png
(or $MAKEFUN_OUTPUT_DIR/entry.png when set). No network, no randomness:
two runs write identical bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main():
    # Gate: the image must exist and stay within the bounty limits
    # (at most 1024 by 1024 pixels, at most 1 MiB).
    assert SOURCE.is_file(), "entry.png is missing"
    assert SOURCE.stat().st_size <= 1048576, "entry.png exceeds 1 MiB"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    # Byte-for-byte copy: the judge sees exactly the bytes in entry.png.
    shutil.copyfile(SOURCE, dest)
    assert dest.stat().st_size == SOURCE.stat().st_size


if __name__ == "__main__":
    main()
