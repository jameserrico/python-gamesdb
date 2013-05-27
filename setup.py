#!/usr/bin/env python

from distutils.core import setup

setup(name='gamesdb',
      version='0.1.1',
      description='Python client for thegamesdb.net API for retrieving video game data.',
      author='James Errico',
      author_email='james.errico@gmail.com',
      url='https://github.com/jameserrico/python-gamesdb',
      py_modules=['gamesdb.api', 'gamesdb.urlutils.urlencode_no_plus'],
      license='MIT',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
      ],
)