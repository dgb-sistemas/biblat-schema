#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name="biblatschema",
    version='0.0',
    description="Esquema de datos para Biblat",
    author="DGB Sistemas",
    author_email="sistemasintegralesdgb@dgb.unam.mx",
    license="GPL-3.0",
    url="https://github.com/dgb-sistemas/biblat_schema",
    packages=find_packages(),
    keywords='biblat schema',
    maintainer_email='sistemasintegralesdgb@dgb.unam.mx',
    download_url='',
    classifiers=[],
    install_requires=[
        "mongoengine>=0.15.0"
    ],
    tests_require=[],
    dependency_links=[],
    test_suite=''
)
