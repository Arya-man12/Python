# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 22:23:29 2022

@author: Aryaman Kumar
"""
#Function to raise float number to specified power
import math
def power(X,N):
    y=math.pow(X,N)
    return y
X=float(input("Enter number"))
N=int(input("Enter power"))
print(power(X,N))
print("Name-Aryaman Kumar,registration no-22BRS1184")