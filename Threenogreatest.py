# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 11:45:52 2023

@author: Aryaman Kumar
"""
#Program to find greatest of three numbers
a=int(input("Enter number"))
b=int(input("Enter number"))
c=int(input("Enter number"))
if(a>b and a>c):
    print("first number ",a,"is the greatest")
elif(b>a and b>c):
    print("Second number",b,"is the greatest")
else:
    print("Third number",c,"is the greatest")
print("Name-Aryaman Kumar,registration no-22BRS1184")