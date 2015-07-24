=================
KwPBar for Python
=================

.. function:: pbar(value, max)

   :param int/float value: current value of progress bar
   :param int/float max: maximum value of the progress bar
   :raises: ValueError

   Print a progress bar to the screen (stderr).


.. function:: erase_pbar()

   Erase the progress bar from the screen.

.. function:: get_termlength()

   :return: terminal length, or 80
   :rtype: int

   Return terminal length, internal helper function.

See also
========

`KwPBar for C <https://github.com/Kwpolska/kwpbar.c>`_

Other documents
===============

.. toctree::
   :maxdepth: 2

   README for KwPBar <README>
   CONTRIBUTING
   LICENSE
   CHANGELOG

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
