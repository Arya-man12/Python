# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:29:06 2023

@author: Aryaman Kumar
"""

#Program to display pascals triangle up till given row
from math import factorial
n=int(input("Enter the number of rows of Pascals triangle required"))
for i in range(n):
  for j in range(1,n-i+1):
     print(end=" ")
  for j in range(0,i+1):
      print(int(factorial(i)/(factorial(j)*factorial(i-j))),end=" ")
  print("")
print("Name-Aryaman Kumar,registration no-22BRS1184")
