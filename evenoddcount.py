# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 22:42:09 2023

@author: Aryaman Kumar
"""

#Program to find odd and even numbers in given series of numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
evencount=0
oddcount=0
for i in range(0,len(numbers)):
    if(numbers[i]%2==0):
        evencount=evencount+1
    else:
        oddcount=oddcount+1
print("Number of even numbers",evencount)
print("Number of odd numbers",oddcount)
print("Name-Aryaman Kumar,registration no-22BRS1184")
