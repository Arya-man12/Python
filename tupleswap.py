# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:17:10 2022

@author: Aryaman Kumar
"""

#Program to swap the values of numbers using tuple assignement
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
print("Before swap",a,b)
t=a,b
b,a=t
print("After swap",a,b)