import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "baneks",
    version = "1.0.0",
    author = "Leonid Startsev",
    author_email = "sandwwraith@gmail.com",
    description = ("Print banek to standard output"),
    license = "WTFPL",
    url = "https://github.com/sandwwraith/baneks",
    packages=['baneks'],
    long_description=read('README.md'),
    requires=['requests','lxml'],
    install_requires=['requests','lxml'],
    entry_points={
        "console_scripts": [
            "banek=baneks.baneks:main"
        ]
    }
)
