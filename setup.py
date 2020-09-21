# -*- coding:utf-8 -*-
# Author: https://github.com/Hopetree
# Date: 2020/7/11
from setuptools import find_packages, setup

VERSION = '1.0.1'

with open('README.md', 'r', encoding='utf-8') as fp:
    long_description = fp.read()

setup(
    name='py2curl',
    version=VERSION,
    py_modules=[
        'py2curl',
    ],
    author='Hopetree',
    author_email='zlwork2014@163.com',
    description='A tool render requests object to curl',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Hopetree/py2curl',
    keywords='python requests curl',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
)
