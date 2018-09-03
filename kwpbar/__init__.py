# -*- encoding: utf-8 -*-
# KwPBar for Python v0.2.0
# Copyright © 2015-2018, Chris Warrick.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions, and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions, and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the author of this software nor the names of
#    contributors to this software may be used to endorse or promote
#    products derived from this software without specific prior written
#    consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
A progress bar for Python.

:Copyright: © 2015-2018, Chris Warrick.
:License: BSD (see /LICENSE).
"""

import shutil
import subprocess  # used only on Python 2
import sys

__title__ = 'KwPBar for Python'
__version__ = '0.2.0'
__author__ = 'Chris Warrick'
__license__ = '3-clause BSD'
__docformat__ = 'restructuredtext en'

__all__ = ('pbar', 'erase_pbar')


def get_termwidth(default=80):
    """Get the width of this terminal."""
    try:  # pragma: no cover
        return shutil.get_terminal_size((default, default)).columns
    except AttributeError:
        # Python 2
        try:
            size = subprocess.check_output(['stty', 'size'])
            return int(size.split()[1]) or 80
        except (IndexError, subprocess.CalledProcessError):
            return 80


def pbar(value, max):
    """Print the progressbar."""
    fullwidth = get_termwidth()
    pbarwidth = fullwidth - 9
    try:
        progress = float(value) / float(max)
    except ZeroDivisionError:
        raise ValueError("invalid progressbar maximum (0)")
    perc = progress * 100
    now = int(round(progress * pbarwidth))
    bar = ''
    if progress == 1:
        bar = '=' * now
    elif progress < 0 or progress > 1:
        raise ValueError("invalid progressbar value (not in range [0, 1])")
    elif now > 0:
        bar = '=' * (now - 1)
        bar += '>'
    final = "\r[{0:" + str(pbarwidth) + "}]{1:5.1f}%"
    sys.stderr.write(final.format(bar, perc))
    sys.stderr.flush()


def erase_pbar():
    """Erase the progressbar."""
    fullwidth = get_termwidth()
    bar = ' ' * fullwidth
    sys.stderr.write("\r" + bar + "\r")
    sys.stderr.flush()
