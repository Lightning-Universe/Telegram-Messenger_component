#!/usr/bin/env python
import os

from pkg_resources import parse_requirements
from setuptools import find_packages, setup

_PATH_ROOT = os.path.dirname(__file__)

with open("README.md") as fp:
    long_description = fp.read()


def _load_requirements(path_dir: str = _PATH_ROOT, file_name: str = "requirements.txt") -> list:
    reqs = parse_requirements(open(os.path.join(path_dir, file_name)).readlines())
    return list(map(str, reqs))


setup(
    name="lit_telegram",
    version="0.1.0",
    description="Messaging notifications for telegram.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Krishna Kalyan",
    author_email="krishna@grid.ai",
    url="https://github.com/PyTorchLightning/LAI-telegram-messenger",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=_load_requirements(),
    python_requires=">=3.8",
)