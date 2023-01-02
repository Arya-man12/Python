# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 16:42:02 2022

@author: Aryaman Kumar
"""
#Finding gcd using recursion
def gcd(a,b):
    if a==b:
      return a
    elif(a<b):
        return gcd(b,a)
    else:
        return gcd(b,a-b)
a=int(input("Enter number"))
b=int(input("Enter number"))
print(gcd(a,b))
print("Name-Aryaman Kumar,registration no-22BRS1184")