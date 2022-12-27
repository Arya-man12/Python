# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:24:53 2022

@author: Aryaman Kumar
"""
#Program to find out the greatest number among three numbers
n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
n3=int(input("Enter third number"))
if(n1>n2 and n1>n3):
    print(n1,"n1 is greatest")
elif(n2>n1 and n2>n3):
    print(n2,"n2 is greatest")
else:
    print(n3,"n3 is greatest")