"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
"""

from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pydatadctesting',
    version='0.1',
    description='Companion code to PyData DC 2018 presentation on testing for Data Science',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/drwaterman/pydatadctesting',
    author='David Waterman',
    packages=['pydatadctesting']
)
