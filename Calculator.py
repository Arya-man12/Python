# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:58:01 2022

@author: Aryaman Kumar
"""

#Program to make a simple calculator that can add,subtract,multiply and divide two numbers
a=int(input("Enter first number"))
b=int(input("Enter second number"))
ch=int(input("Enter your choice 1.Addition,2.Subtraction,3.Multiplication,4 division"))
if(ch==1):
    c=a+b
    print("Result",c)
if(ch==2):
    c=a-b
    print("Result",c)
if(ch==3):
    c=a*b
    print("Result",c)
if(ch==4):
    c=a/b
    print("Result",c)