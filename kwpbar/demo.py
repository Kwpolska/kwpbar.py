# -*- encoding: utf-8 -*-
# KwPBar for Python 0.1.0
# A progress bar for Python.
# Copyright © 2015-2018, Chris Warrick.
# See /LICENSE for licensing information.

"""
Demo module.

:Copyright: © 2015-2018, Chris Warrick.
:License: BSD (see /LICENSE).
"""

import sys
import kwpbar
import time

__all__ = ('demo')


def demo():  # pragma: no cover
    """Run the demo."""
    if len(sys.argv) == 1:
        runs = 5
    else:
        runs = int(sys.argv[1])

    for i in range(0, runs + 1):
        kwpbar.pbar(i, runs)
        time.sleep(1)

    kwpbar.erase_pbar()


if __name__ == '__main__':  # pragma: no cover
    demo()
