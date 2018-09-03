#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# KwPBar for Python — test suite
# Copyright © 2015-2018, Chris Warrick.
# See /LICENSE for licensing information.

import pytest
import kwpbar
import kwpbar.demo


def test_printing():
    """Test progressbar printing."""
    kwpbar.pbar(0, 2)
    kwpbar.pbar(1, 2)
    kwpbar.pbar(2, 2)


def test_erasing():
    """Test progressbar erasing."""
    kwpbar.pbar(2, 3)
    kwpbar.erase_pbar()


def test_termwidth_positive():
    assert kwpbar.get_termwidth() >= 0


def test_fail1():
    with pytest.raises(ValueError):
        kwpbar.pbar(1, 0)


def test_fail2():
    with pytest.raises(ValueError):
        kwpbar.pbar(2, 1)


def test_fail3():
    with pytest.raises(ValueError):
        kwpbar.pbar(-2, 1)
