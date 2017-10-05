# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup
from git_release_tag import GitReleaseTagger

dependencies = open('requirements.txt','r').readlines()


tagger = GitReleaseTagger()
tagger.set_directory('.')
tagger.get_current_release()

version=tagger.current_release

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
