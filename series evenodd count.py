# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:30:07 2022

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