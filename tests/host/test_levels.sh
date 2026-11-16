#!/bin/sh
# The level files are little-endian (tests/host/check_levels.py).
set -eu
cd "$(dirname "$0")/../.."
python3 tests/host/check_levels.py assets/levels
