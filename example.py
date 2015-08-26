# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:09:20 2015

@author: 906235
"""

from splitzip import Folder

path = # Insert path here. For windows paths, use forward slashes or double backslashes!
myfolder = Folder(path)
print(myfolder.contents)
print(myfolder.split_contents(MAX_TOTAL_SIZE=64e6))
myfolder.zip_split_contents(MAX_TOTAL_SIZE=64e6)
