"""Setup script for CadQuery."""

from setuptools import setup, find_packages
import re
from pathlib import Path

# Read version from cadquery/__init__.py
def get_version():
    init_path = Path("cadquery/__init__.py")
    if init_path.exists():
        content = init_path.read_text()
        match = re.search(r'^__version__\s*=\s*["\']([^"\']+)["\']', content, re.M)
        if match:
            return match.group(1)
    return "0.0.0"


# Read long description from README
def get_long_description():
    readme = Path("README.md")
    if readme.exists():
        return readme.read_text(encoding="utf-8")
    return ""


setup(
    name="cadquery",
    version=get_version(),
    description="A parametric 3D CAD scripting framework built on top of OCCT",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="CadQuery Contributors",
    url="https://github.com/CadQuery/cadquery",
    license="Apache License 2.0",
    packages=find_packages(exclude=["tests", "tests.*", "doc", "doc.*"]),
    python_requires=">=3.8",
    install_requires=[
        "OCP",          # Python bindings for OpenCASCADE
        "typish",
        "nptyping",
        "pyparsing",
        "pytest",       # included for plugin testing utilities
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "mypy",
            "black",
            "flake8",
        ],
        "docs": [
            "sphinx",
            "sphinx-rtd-theme",
            "sphinxcadquery",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    ="CA OCCT, OpenCASCADE,  parametric, modeling, scripting",
    projectreadthedocs.io",
        "Source": "https://github.com/CadQuery/cadquery",
        "Tracker": "https://github.com/CadQuery/cadquery/issues",
    },
)
