"""
Setup the package.
"""
from setuptools import (
    find_packages,
    setup,
)

DESCRIPTION = 'Next-gen Arrange-Act-Assert to structure test cases and force software engineers to ' \
              'express explicit intentions in BDD style.'

with open('README.md', 'r', encoding='utf-8') as read_me:
    long_description = read_me.read()

with open('.project-version', 'r') as project_version_file:
    project_version = project_version_file.read().strip()

setup(
    version=project_version,
    name='intentions',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dmytrostriletskyi/intentions',
    project_urls={
        'Issue Tracker': 'https://github.com/dmytrostriletskyi/intentions/issues',
        'Source Code': 'https://github.com/dmytrostriletskyi/intentions',
        'Download': 'https://github.com/dmytrostriletskyi/intentions/tags',
    },
    license='MIT',
    author='Dmytro Striletskyi',
    author_email='dmytro.striletskyi@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
