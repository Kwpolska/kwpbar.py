#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# KwPBar for Python — test suite
# Copyright © 2015, Chris Warrick.
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


@pytest.mark.xfail(raises=ValueError)
def test_fail1():
    kwpbar.pbar(1, 0)


@pytest.mark.xfail(raises=ValueError)
def test_fail2():
    kwpbar.pbar(2, 1)


@pytest.mark.xfail(raises=ValueError)
def test_fail3():
    kwpbar.pbar(-2, 1)
