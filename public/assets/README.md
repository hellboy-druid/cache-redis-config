"""
cache-redis-config

A Python package to configure and manage Redis cache.

Usage
-----

To use this package, simply install it via pip:

    pip install cache-redis-config

Features
--------

* Supports Redis configuration for multiple environments
* Provides a simple API to configure and get Redis settings
* Includes support for Redis Sentinel and Cluster modes

Installation
------------

To install the package, use pip:

    pip install git+https://github.com/[username]/cache-redis-config.git

Contributing
------------

Contributions are welcome and encouraged. To contribute, fork the repository and submit a pull request.

License
-------

This package is licensed under the MIT License.

"""

from setuptools import setup, find_packages

setup(
    name='cache-redis-config',
    version='1.0.0',
    author='[Your Name]',
    author_email='[your_email@example.com](mailto:[your_email@example.com])',
    description='Redis cache configuration package',
    long_description=__doc__,
    packages=find_packages(),
    install_requires=[
        'redis'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)