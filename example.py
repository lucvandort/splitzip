# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:09:20 2015

@author: 906235
"""

from splitzip import Folder

path = # Insert path here. Use forward slashes, also in Windows!
testfolder = Folder(path)
print(testfolder.contents)
print(testfolder.split_contents(MAX_TOTAL_SIZE=10e6))
testfolder.zip_split_contents(MAX_TOTAL_SIZE=10e6)