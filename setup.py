# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup

dependencies = open('requirements.txt','r').readlines()


version="0.0.0"

setup(
    name = "jwt-generator",
    packages = ["generator"],
    entry_points = {
        "console_scripts": ['jwt-generator = generator.jwt_generator:main']
        },
    version = version,
    description = "a simple JWT generator.",
    long_description='todo',
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['jwt', 'click'],
    author = "Mark van Holsteijn",
    author_email = "markvanholsteijn@binx.io",
    url = "https://github.com/mvanholsteijn/jwt-generator",
    )
