# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:56:07 2015

@author: 906235
"""

import os, stat
import pandas as pd
import zipfile


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

    def split_contents(self, MAX_TOTAL_SIZE = 100e6):
        file_sets = {'000': list()}
        i = 0;
        total_size = 0;
        for ind in self.contents.index:
            if self.contents.loc[ind]['size'] > MAX_TOTAL_SIZE:
                continue
            else:
                total_size += self.contents.loc[ind]['size']
                
            if total_size > MAX_TOTAL_SIZE:
                i += 1
                file_sets[str(i).zfill(3)] = list()
                total_size = self.contents.loc[ind]['size']
                            
            file_sets[str(i).zfill(3)].append(self.contents.loc[ind]['name'])
                
        return file_sets
            
