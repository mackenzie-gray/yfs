#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='yfs',
    version='0.0.1',
    description='Wrapper for the Yahoo Fantasy Sports API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
    url='https://github.com/maxhumber/yfs',
    author='Max Humber',
    author_email='max.humber@gmail.com',
    license='MIT',
    packages=['yfs'],
    zip_safe=False,
    install_requires=['requests'],
    python_requires='>=3.6',
    setup_requires=['setuptools>=38.6.0']
)
