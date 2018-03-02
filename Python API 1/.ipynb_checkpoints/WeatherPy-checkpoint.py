# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 11:06:44 2018

@author: chander
"""

import gzip
with gzip.open('citipy-0.0.5.tar.gz', 'rb') as f:
    file_content = f.read()