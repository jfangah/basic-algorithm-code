# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 11:10:48 2017

@author: Administrator
"""

def find_dic(d,a):
    if a in d.keys():
        return 1
    else:
        return 0

d={'1':10,'2':20,'3':30,'4':40,'5':50,'6':60}
m=input()
n=find_dic(d,m)
if n==0:
    print("%s is not present in the dictionary" %m)
else:
    print("%s is present in the dictionary" %m)