# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 12:12:15 2023

@author: Aryaman Kumar
"""

def factors(num,i):
    if(num%i==0):
        print("Factor",i)
    if(i>=num):
        return""
    else:
        return factors(num,i+1)
n=int(input())
print(factors(n,1))