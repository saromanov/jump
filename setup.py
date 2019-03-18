#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import textwrap

version = "1.0"

if __name__ == "__main__":
    setuptools.setup(
        name="jams",
        version=version,
        description="Consistent hashing algorithm",
        author="Sergey Romanov",
        author_email="xxsmotur@gmail.com",
        long_description=textwrap.dedent("""\
            Implementation of consistent hashing algorithm
           """),
        packages=[
            "jump",
        ],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "License :: MIT",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Topic :: Software Development",
        ],
        test_suite="jump.tests.AllTests",
        python_requires=">=3.0"
    )
