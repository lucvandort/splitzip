# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:56:07 2015

@author: 906235
"""

import os, stat
import pandas as pd


class Folder:
    def __init__(self, path):
        self.path = path
        self.contents = pd.DataFrame(columns=['name', 'size'])
        self.update_contents()
    
    def update_contents(self):
        for filename in os.listdir(path=self.path):
            if filename == '.':
                continue
            
            filepath = os.path.join(self.path, filename)
            filestat = os.lstat(filepath)            
            
            if stat.S_ISDIR(filestat.st_mode):
#                print('folder: ' + filepath)
                continue
            elif stat.S_ISREG(filestat.st_mode):
#                print('file: ' + filepath)
                self.contents.loc[len(self.contents)] = (filename, filestat.st_size)


