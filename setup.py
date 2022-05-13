"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages


setup(
    name="blind-charging-demo",  # Required
    version="1.0.1",  # Required
    packages=find_packages(where="src"),  # Required
    python_requires=">=3.9, <4",
    install_requires=["click"],  # Optional
)
