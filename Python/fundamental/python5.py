# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 11:04:28 2017

@author: Administrator
"""

def sum_list(list1):
    t=sum(i for i in list1)
    return t
a=eval(input())
b=list(a)
c=sum_list(b)
print(c)