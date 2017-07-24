#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 14:52:32 2017

@author: ofir
"""

from distutils.core import setup
#from setuptools import setup
from glob import glob

setup(
    name = "demopack",
    version = "1.2",
    author = "Ofir",
    author_email = "ofiras@gmail.com",
    #py_modules = ['chelpers,numhelpers'],
    packages = ['demopack'],
    scripts = ['testpack1.py'],
    data_files = [
        ('images',glob('images/*')),
        ('.', ['664.jpg'])],
    )

