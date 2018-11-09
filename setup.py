#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import platform
from setuptools import (
    find_packages,
    setup,
)

py_version = platform.python_version()

PACKAGE_VERSION = '2.0.4'
PACKAGE_REQUIRED = [
    "toolz>=0.9.0,<1.0.0;implementation_name=='pypy'",
    "cytoolz>=0.9.0,<1.0.0;implementation_name=='cpython'",
    "urllib3",
    "pycryptodome",
    "base58",
    "eth-account>=0.2.1,<0.4.0",
    "eth-utils>=1.2.0,<2.0.0",
    "ecdsa",
    "pysha3"
]

this_dir = os.path.dirname(__file__)
readme_filename = os.path.join(this_dir, 'README.rst')

with open(readme_filename) as f:
    PACKAGE_LONG_DESCRIPTION = f.read()


setup(
    name='tronapi',
    version=PACKAGE_VERSION,
    description='A Python API for interacting with Tron (TRX)',
    long_description=PACKAGE_LONG_DESCRIPTION,
    url='https://github.com/iexbase/tron-api-python',

    keywords='tron tron-api tron-api-python iexbase',

    author='Shamsudin Serderov',
    author_email='steein.shamsudin@gmail.com',
    license='MIT License',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Office/Business :: Financial',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=PACKAGE_REQUIRED,
)
