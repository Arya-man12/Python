# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 19:46:25 2022

@author: Aryaman Kumar
"""

N=int(input("Enter last term of the series"))
sum=0
for i in range(1,N+1):
    sum=sum+i**(0.5)
print(sum)