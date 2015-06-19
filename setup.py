#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    long_description = open("README.rst", "U").read()
except IOError:
    long_description = "See https://github.com/wolever/safesort"

setup(
    name="safesort",
    version="0.2.0",
    url="https://github.com/wolever/safesort",
    author="David Wolever",
    author_email="david@wolever.net",
    description="Safely sort heterogeneous collections.",
    long_description=long_description,
    py_modules=["safesort"],
    install_requires=[],
    license="BSD",
    classifiers=[ x.strip() for x in """
        Development Status :: 3 - Alpha
        Intended Audience :: Developers
        License :: OSI Approved :: BSD License
        Natural Language :: English
        Operating System :: OS Independent
        Programming Language :: Python
        Programming Language :: Python :: 2
        Programming Language :: Python :: 3
        Topic :: Software Development
    """.split("\n") if x.strip() ],
)
