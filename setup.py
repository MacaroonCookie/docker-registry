#!/usr/bin/env python

from setuptools import setup

__version__ = '0.0.1-alpha.2'
__license__ = ''

setup(
        name='Docker Registry CLI',
        version = __version__,
        description = 'A CLI tool to interact with private Docker Registires',
        long_description = '',
        author = 'Seth Cook',
        author_email = 'cooker52@gmail.com',
        url = '',
        packages = [ 'docker_registry' ],
        license = __license__,
        classifiers  = [ 'Programming Language :: Python :: 2.7',
                         'Operating System :: Unix',
                         'Development Status :: 3 - Alpha' ],
        install_requires = [
            'argparse>=1.4.0',
            'requests>=2.11.0',
            'tabulate>=0.7.5'
        ],
        entry_points = { 'console_scripts': [ 'docker-registry=docker_registry.__main__:main' ] }
)
