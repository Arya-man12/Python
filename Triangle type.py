# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:34:12 2022

@author: Aryaman Kumar
"""
#Program to determine the type of triangle from given three sides
a=int(input("Enter length of first side"))
b=int(input("Enter length of second side"))
c=int(input("Enter length of third side"))
if(a==b and b==c):
    print("Equilateral triangle")
elif(a==b or b==c or c==a):
    print("Isoceles triangle")
else:
    print("Scalene triangle")