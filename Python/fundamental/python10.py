# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 11:11:30 2017

@author: Administrator
"""

a=eval(input())
b=list(a)
l=len(b)
for m in range(0,l-1):
    for n in range(0,l-1-m):
        if b[n]>b[n+1]:
            b[n],b[n+1]=b[n+1],b[n]
print(b)