Laser Kombat for GFOS
=====================

A port of Laser Kombat, David Dewey's 1995 tank-and-mirror puzzle game in
Wouter Wijsman's SDL 2 and C++17 version, from
https://github.com/sharkwouter/laserkombat at commit
3ebb3880684d36e95e4dde551c5ae6467b3dbd31, for GFOS: AmigaOS 3.2 with
GFOpenUp, on a 68040 or 68060 with an FPU, on GFOpenUp's SDL 2.

Destroy every enemy tank in each of the levels without being seen: aim the
laser off mirrors, blow up the bombs, push the enemies into the water.

Status: built in Cradle's os32-gcc16-open6 stove; not yet run in a lab.


What you need
-------------

- GFOS: AmigaOS 3.2 with GFOpenUp 0.8.26 or later, which installs
  LIBS:GFOpenGPU/SDL2.module. SDL2_ttf is linked into the game from
  GFOpenUp's kit, so no SDL2_ttf.module is needed.
- A 68040 or 68060 with an FPU (not an LC040 or EC040), an RTG screen of
  800 x 600 or more (or the AmiCradle lab), and about 8 MB of free memory.
- Nothing else: the levels, pictures, sounds and fonts are in the drawer's
  assets.


How to play
-----------

Run Install-LaserKombat (or copy the LaserKombat drawer where you want
it), then double-click LaserKombat. The keys are in the drawer's Controls
file (the Help key shows it; F1 and F2 in the game show the keys and the
blocks).


Building
--------

    make -f amiga/Makefile.amigaos -j4 STOVE=/path/to/os32-gcc16-open6

or, in Cradle, stove_build with the os32-gcc16-open6 stove and target
package (package/build-amiga.sh), which also packs
LaserKombat-VERSION-68040.lha.


What was changed
----------------

- include/utils.h: the assets are found in PROGDIR:assets/.
- src/Board.cpp: the level files hold little-endian ints (written on a
  PC); on a big-endian machine they are swapped as they are read
  (tests/host checks every level decodes to known blocks).
- amiga/amiga_start.c: 256 KB of stack and the $VER string.
- amiga/: the Makefile, the GlowIcons (our own art), the Installer script
  and its spec.

The AmiCradle Team.
