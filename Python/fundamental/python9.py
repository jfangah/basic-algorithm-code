# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 11:11:08 2017

@author: Administrator
"""

def is_prime(number):
    if number>1:
        for i in range(2,number):
            if number%i==0:
                return -1
        return 1
    else:
        return -1
    
a=int(input())
b=is_prime(a)
if b==1:
    print('%d is a prime number' %a)
else:
    print("%d isn't a prime number" %a)
            