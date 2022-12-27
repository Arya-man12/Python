# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 12:44:18 2022

@author: Aryaman Kumar
"""
#Program to find sum of series 1 + x^2/2 + x^3/3 + … x^n/n
N=int(input("Enter last term of series"))
x=int(input("Enter the value of x"))
sum=0
for i in range(1,N+1):
    sum=sum+int(x^i//i)
print("Sum is",sum)