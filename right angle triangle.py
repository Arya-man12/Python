# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 14:45:11 2022

@author: Aryaman Kumar
"""
import math
a=int(input("Enter length of first side"))
b=int(input("Enter length of second side"))
c=int(input("Enter length of third side"))
if(c>a and c>b):
    if(c^2==a^2+b^2):#We apply pythagoras theorem to see if the square of the largest side
      #is equal to the sum of squares of the other two sides
        print("Right angle triangle")
if(b>a and b>c):
    if(b^2==a^2+c^2):
        print("Right angle triangle")
if(a>b and a>c):
    if(a^2==b^2+c^2):
        print("Right angle triangle")