# (C) Copyright IBM 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""ipyhi

ipyhi is a Jupyter notebook notification system.
It is based on the jupyter-notify package.
"""
import os
from setuptools import find_packages, setup

MAJOR = 0
MINOR = 0
MICRO = 11

ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)
FULLVERSION = VERSION

DOCLINES = __doc__.split('\n')
DESCRIPTION = DOCLINES[0]
LONG_DESCRIPTION = "\n".join(DOCLINES[2:])

def git_short_hash():
    try:
        git_str = "+" + os.popen('git log -1 --format="%h"').read().strip()
    except:  # pylint: disable=bare-except
        git_str = ""
    else:
        if git_str == '+': #fixes setuptools PEP issues with versioning
            git_str = ''
    return git_str

if not ISRELEASED:
    FULLVERSION += '.dev'+str(MICRO)+git_short_hash()

def write_version_py(filename='ipyhi/version.py'):
    cnt = """\
# THIS FILE IS GENERATED FROM IPYHI SETUP.PY
# pylint: disable=missing-module-docstring
short_version = '%(version)s'
version = '%(fullversion)s'
release = %(isrelease)s
"""
    a = open(filename, 'w')
    try:
        a.write(cnt % {'version': VERSION, 'fullversion':
                       FULLVERSION, 'isrelease': str(ISRELEASED)})
    finally:
        a.close()

setup(
    name='ipyhi',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Paul Nation',
    author_email='nonhermitian@gmail.com',
    url='https://github.com/nonhermitian/ipyhi',
    license='Apache-2',
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'ipyhi': ['js/*.js']},
    install_requires=[
        'ipython',
        'jupyter',
        'ipywidgets'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
