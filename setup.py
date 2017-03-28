#!/usr/bin/env python
import os
import sys
from setuptools import setup

if "publish" in sys.argv[-1]:
    os.system("python setup.py sdist upload")
    sys.exit()


# Command-line tools
entry_points = {'console_scripts': [
    'watplanet = watplanet.watplanet:watplanet_main'
]}

setup(name='watplanet',
      version=0.1,
      description="WATPLANET?!",
      long_description='',
      author='Geert Barentsen',
      author_email='hello@geert.io',
      license='MIT',
      packages=['watplanet'],
      install_requires=['astropy>=1.1'],
      entry_points=entry_points,
      include_package_data=True,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Intended Audience :: Science/Research",
          "Topic :: Scientific/Engineering :: Astronomy",
          ],
      )