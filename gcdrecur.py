# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 23:10:12 2023

@author: Aryaman Kumar
"""

def GCD(a,b):
    if(b==0):
        return a
    else:
        return a//b*GCD(b,a%b)
a=int(input())
b=int(input())
print(GCD(a,b))