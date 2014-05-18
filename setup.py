# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

here = os.path.dirname(__file__)
requires = []
tests_require = [
]


def _read(name):
    try:
        return open(os.path.join(here, name)).read()
    except:
        return ""
readme = _read("README.rst")
license = _read("LICENSE.rst")

setup(
    name='ip2country',
    version='0.0.1',
    test_suite='ip2country',
    author='Kohei YOSHIDA',
    author_email='license@yosida95.com',
    description='OAuth 2.0 library for Python 3.',
    long_description=readme,
    license=license,
    url='https://github.com/yosida95/ip2country',
    packages=['ip2country'],
    install_requires=requires,
    tests_require=tests_require,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)