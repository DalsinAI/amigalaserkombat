#!/usr/bin/env python3
"""Every level in assets/levels decodes as little-endian ints to known
blocks and rotations, and read as big-endian (what a 68k would see without
the swap in src/Board.cpp) it does not: the swap is needed and right.
GPL 3, Copyright (c) 2026 AmiCradle Team."""
import struct, sys
from pathlib import Path

COLUMNS, ROWS, BLOCKS = 20, 15, 22   # include/constants.h, include/BlockType.h
N = COLUMNS * ROWS
levels = sorted(Path(sys.argv[1] if len(sys.argv) > 1 else "assets/levels").glob("level*.lvl"))
if not levels:
    sys.exit("no levels found")

def ok(data, order):
    ints = struct.unpack_from(f"{order}{2 + 5 * N}i", data)
    gt, gr, bt, br = (ints[2 + k * N: 2 + (k + 1) * N] for k in range(4))
    return (all(0 <= t < BLOCKS for t in gt + bt)
            and all(0 <= r < 256 for r in gr + br))

bad = []
for p in levels:
    data = p.read_bytes()
    if len(data) < 8 + 5 * N * 4 + 512:
        bad.append(f"{p.name}: {len(data)} bytes, too short")
        continue
    if not ok(data, "<"):
        bad.append(f"{p.name}: does not decode as little-endian")
    if ok(data, ">"):
        bad.append(f"{p.name}: also decodes as big-endian, the swap test proves nothing")
print(f"{len(levels)} levels, {len(bad)} bad")
for b in bad:
    print(" ", b)
sys.exit(1 if bad else 0)
