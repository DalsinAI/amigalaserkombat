/* The Amiga port's start: the stack and the version string.
 * Copyright (c) 2026 AmiCradle Team. GPL 3, like Laser Kombat. */

/* A Shell gives 4 KB of stack; SDL 2 and the C++ runtime want more.
 * libnix's startup sets this much up. */
unsigned long __stack = 256 * 1024;
static const char version[] __attribute__((used)) =
    "$VER: LaserKombat 1.0 (16.11.2026)";
