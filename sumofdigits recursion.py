# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 15:53:00 2022

@author: Aryaman Kumar
"""
#Sum of digits of a number using recursion
def sod(n1):
 if(n1<=0):
    return 0
 else:
    return(n1%10+sod(n1//10))
num=int(input("Enter number"))
sum1=sod(num)
print("Sum",sum1)
print("Name-Aryaman Kumar,registration no-22BRS1184")