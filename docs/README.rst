=================
KwPBar for Python
=================
:Info: This is the README file for KwPBar.
:Author: Chris Warrick <chris@chriswarrick.com>
:Copyright: © 2015-2018, Chris Warrick.
:Date: 2018-09-03
:Version: 0.2.1

.. index: README
.. image:: https://travis-ci.org/Kwpolska/kwpbar.py.svg?branch=master
   :target: https://travis-ci.org/Kwpolska/kwpbar.py

A simple progress bar for Python programs.

INSTALLATION
------------

::

    pip install kwpbar

USAGE
-----

``import kwpbar`` in your program.

The following functions are available:

* `get_termlength()` → return terminal length (columns); helper function
* `pbar(value, max)` → print a progress bar to the screen (stderr).  Can raise ValueError.
* `erase_pbar()` → erase the progress bar from the screen

DEMO
----

::

    python -m kwpbar.demo

SEE ALSO
--------

`KwPBar for C <https://github.com/Kwpolska/kwpbar.c>`_

COPYRIGHT
---------
Copyright © 2015-2018, Chris Warrick.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions, and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions, and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

3. Neither the name of the author of this software nor the names of
   contributors to this software may be used to endorse or promote
   products derived from this software without specific prior written
   consent.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
