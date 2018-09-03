#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys
import io
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests/']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(name='kwpbar',
      version='0.2.0',
      description='A progress bar for Python.',
      keywords='kwpbar',
      author='Chris Warrick',
      author_email='chris@chriswarrick.com',
      url='https://github.com/Kwpolska/kwpbar.py',
      license='3-clause BSD',
      long_description=io.open('./docs/README.rst', 'r', encoding='utf-8').read(),
      platforms='any',
      zip_safe=False,
      cmdclass={'test': PyTest},
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7'],
      packages=['kwpbar'],
      )
