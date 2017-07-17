#!/usr/bin/env python
import io

from setuptools import setup, find_packages


with io.open('README.md', encoding='utf-8') as handle:
    readme = handle.read()


with io.open('requirements-production.txt', encoding='utf-8') as handle:
    requirements = [line.strip('\n').strip() for line in handle.readlines()]


setup(
    name='dj-core-drf',
    version='0.0.1',
    description='A self-contained and extensible Django Rest Framework environment',
    long_description=readme,
    author='Ionata Digital',
    author_email='webmaster@ionata.com.au',
    url='https://github.com/ionata/dj-core-drf',
    packages=find_packages('src'),
    install_requires=requirements,
    package_dir={'': 'src'},
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)