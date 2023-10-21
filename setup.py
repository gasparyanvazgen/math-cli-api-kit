"""This module configures the setup details for the Math CLI API Kit
package.

For more information about this package and its usage, please refer to
the README.md file or the official GitHub repository:
https://github.com/gasparyanvazgen/math-cli-api-kit
"""

from typing import Literal

from setuptools import setup, find_packages

from math_cli_api_kit.config import APIConfig, GITHUB_REPO_URL

__version__: Literal["Module version"]
__author__: Literal["Author full name"]

api_config = APIConfig()

__version__ = api_config.API_VERSION
__author__ = api_config.API_CONTACT_NAME

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="math-cli-api-kit",
    version=__version__,
    description=api_config.API_DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    author_email=api_config.API_CONTACT_EMAIL,
    url=GITHUB_REPO_URL,
    license=api_config.API_LICENSE_NAME,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
        "Topic :: Utilities",
        "Framework :: Sanic",
        "Framework :: Sanic-OpenAPI",
        "Natural Language :: English",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click==8.1.2",
        "sanic==21.12.0",
        "sanic-openapi==21.12.0",
        "websockets==10.0",
    ],
    zip_safe=False
)
