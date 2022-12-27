# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:16:39 2022

@author: Aryaman Kumar
"""
#Program to find the roots of a quadratic equation
import math
a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter c value"))
D=b**2-4*a*c#Calculating discirimnant
if(D<0):
    print("Imaginary roots")
else:
   x1=(-b+math.sqrt(D))/2*a#Calculating the two roots
   x2=(-b-math.sqrt(D))/2*a
   print("roots",x1,x2)
