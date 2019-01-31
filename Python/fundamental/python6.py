# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 11:07:05 2017

@author: Administrator
"""

class Circle:
    def __init__(self,r):
        self.r=r
    def LandS(self):
        s=3.14*self.r*self.r
        l=2*3.24*self.r
        print("面积是%.2f，周长是%.2f" %(s,l))
circle1=Circle(3)
circle1.LandS()