# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 12:37:45 2022

@author: Aryaman Kumar
"""
#Program to find sum of series 1 + 1/2 + 1/3 + ….. + 1/N
N=int(input("Enter last term of series"))
sum=0
for i in range(1,N+1):
    sum=sum+1/i
print("Sum is",sum)