#!/usr/bin/env python
# coding=utf-8
# :bc: Not importing unicode_literals because in Python 2 distutils,
# some values are expected to be byte strings.
from __future__ import absolute_import, division, print_function

from codecs import StreamReader, open
from distutils.version import LooseVersion

import setuptools

##
# Because of the way PyOTA declares its dependencies, it requires a
# more recent version of setuptools.
# https://www.python.org/dev/peps/pep-0508/#environment-markers
if LooseVersion(setuptools.__version__) < LooseVersion('20.5'):
    import sys

    sys.exit('Installation failed: Upgrade setuptools to version 20.5 or later')

##
# Load long description for PyPI.
with open('README.rst', 'r', 'utf-8') as f:  # type: StreamReader
    long_description = f.read()

##
# Declare test dependencies separately, so that they can be installed
# either automatically (``python setup.py test``) or manually
# (``pip install -e .[test-runner]``).
tests_require = [
    'mock; python_version < "3.0"',
    'nose',
]

##
# Off we go!
# noinspection SpellCheckingInspection
setuptools.setup(
    name='PyOTA',
    description='IOTA API library for Python',
    url='https://github.com/iotaledger/iota.lib.py',
    version='2.0.8',

    long_description=long_description,

    packages=setuptools.find_packages('.', exclude=(
        'examples', 'examples.*',
        'test', 'test.*',
    )),

    include_package_data=True,

    # http://python-packaging.readthedocs.io/en/latest/command-line-scripts.html#the-console-scripts-entry-point
    entry_points={
        'console_scripts': [
            'pyota-cli=iota.bin.repl:main',
        ],
    },
    
    # Class Registry dependancy of filters module overwriten to support Python 3.7
    # This module is no longer maintained so used a forked version. 

    install_requires=[
        'filters',
        'class-registry @ git+https://github.com/todofixthis/class-registry@2.1.3#egg=class-registry'
        'pysha3',

        # ``security`` extra wasn't introduced until 2.4.1
        # http://docs.python-requests.org/en/latest/community/updates/#id35
        'requests[security] >= 2.4.1',

        'six',
        'typing; python_version < "3.0"',
    ],

    extras_require={
        'ccurl': ['pyota-ccurl'],
        'docs-builder': ['sphinx', 'sphinx_rtd_theme'],
        'test-runner': ['detox'] + tests_require,
    },

    test_suite='test',
    test_loader='nose.loader:TestLoader',
    tests_require=tests_require,

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    keywords=(
        'iota,tangle,iot,internet of things,api,library,cryptocurrency,'
        'balanced ternary'
    ),

    author='Phoenix Zerin',
    author_email='phx@phx.ph',
)
