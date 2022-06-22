#!/usr/bin/env python

from setuptools import setup
import pathlib


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="flask_appfactory",
    version="1.0.0",
    description="Flask Application Factory",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tibotix",
    author_email="tizian@seehaus.net",
    url="https://github.com/tibotix/flask_appfactory",
    package_dir={"flask_appfactory": "src"},
    packages=["flask_appfactory"],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.5, <4",
)
