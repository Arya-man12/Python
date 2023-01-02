# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 18:36:05 2022

@author: Aryaman Kumar
"""
#Program to swap using temporary variable and multiple assignment
a=int(input("Enter number1"))
b=int(input("Enter number2"))
c=a
a=b
b=c#Temporary variable
print(a,b,"after swapping")
a,b=b,a#Multiple assignment
print(a,b,"after swapping again")
print("Name-Aryaman Kumar,registration no-22BRS1184")
