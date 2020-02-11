#!/usr/bin/env python
# encoding: utf-8

"""Convenience methods that help with debugging.

They should never be used in production code.

"""

import sys

DUMP_FILENAME = (
    "/tmp/file.txt"
    if not sys.platform.lower().startswith("win")
    else "C:/windows/temp/copywriting.txt"
)


def debug(msg):
    """Dumb 'msg' into the debug file."""
    with open(DUMP_FILENAME, "ab") as dump_file:
        dump_file.write((msg + "\n").encode("utf-8"))
