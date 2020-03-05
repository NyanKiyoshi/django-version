#!/usr/bin/env python
import os.path

from setuptools import setup

HERE = os.path.dirname(__file__)


def read(filename):
    with open(os.path.join(HERE, filename)) as f:
        return f.read()


setup(
    name="django-version",
    version="1.0.rc1",
    packages=["django_version"],
    author="NyanKiyoshi",
    author_email="hello@vanille.bid",
    license="MIT",
    description=(
        "A middleware retrieving a project version from settings "
        "and returning it in the response headers."
    ),
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    url="https://github.com/NyanKiyoshi/django-version",
    classifiers=[
        "License :: Public Domain",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    data_files=[("", ["README.md", "LICENSE"])],
    install_requires=["django"],
)
