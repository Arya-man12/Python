# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:09:13 2022

@author: Aryaman Kumar
"""
import math
#Progam to find area of triangle using Herons formula
a=int(input("Enter first side"))
b=int(input("Enter second side"))
c=int(input("Enter third side"))
s=a+b+c/2
d=s*(s-a)*(s-b)*(s-c)
area=math.sqrt(d)
print(area)