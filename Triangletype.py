# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 11:54:43 2023

@author: Aryaman Kumar
"""
#Program to determine type of triangle based on lengths of three sides
a=int(input("Enter length of first side of triangle"))
b=int(input("Enter length of second side of triangle"))
c=int(input("Enter length of third side of triangle"))
if(a==b and a==c):
    print("Equilateral triangle")
elif(a==b or a==c or b==c):
    print("Isoceles triangle")
else:
    print("Scalene triangle")
print("Name-Aryaman Kumar,registration no-22BRS1184")
