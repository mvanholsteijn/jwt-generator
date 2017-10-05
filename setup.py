# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))
dependencies = open(path.join(here, 'requirements.txt'),'r').readlines()
with open(path.join(here, 'README.md'), 'r') as f:
    long_description = f.read()

version="1.0"

setup(
    name = "jwt-generator",
    packages = ["generator"],
    entry_points = {
        "console_scripts": ['jwt-generator = generator.jwt_generator:main']
        },
    version = version,
    description = "a simple JWT generator.",
    long_description=long_description,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['jwt', 'click'],
    author = "Mark van Holsteijn",
    author_email = "markvanholsteijn@binx.io",
    url = "https://github.com/mvanholsteijn/jwt-generator",
    )
