# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 12:58:07 2022

@author: Aryaman Kumar
"""
#Program to find whether a number is prime number or composite number
q=False
n=int(input("Enter the number"))
if(n==1):
    print("Number is a unique number")
for i in range(2,n):
    if(n%i==0):
        print("Number is a composite number")
        break
    else:
        q=True
if(q==True):
    print("Number is a prime number")
        