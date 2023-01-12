# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 22:59:50 2023

@author: Aryaman Kumar
"""

def SOD(n):
    if(n<=0):
        return 0
    else:
        return n%10+SOD(n//10)
n=int(input())
print(SOD(n))