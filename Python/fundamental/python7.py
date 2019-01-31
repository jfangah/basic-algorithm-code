# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 11:10:26 2017

@author: Administrator
"""

class IOString:
    def get_String(self):
        self.string=input()
    def print_String(self):
        self.string=(self.string).upper()
        print(self.string)
