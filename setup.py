# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), 'r') as f:
    long_description = f.read()

version="0.12.1"

setup(
    name = "jwt-generator",
    packages = ["jwt_generator"],
    entry_points = {
        "console_scripts": ['jwt-generator = jwt_generator.jwt_generator:main']
        },
    version = version,
    description = "unix command line JWT generator.",
    long_description=long_description,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['pyjwt', 'click', 'cryptography'],
    author = "Mark van Holsteijn",
    author_email = "mvanholsteijn@xebia.com",
    url = "https://github.com/mvanholsteijn/jwt-generator",
    )
