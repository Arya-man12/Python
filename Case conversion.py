# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 12:25:43 2022

@author: Aryaman Kumar
"""
#Program to convert uppercase to lowercase and vice versa
a=input("Enter text")
if(a.islower()==True):
    cc=a.upper()#Converting lowercase to uppercase
    print(cc)
    print("Converted to uppercase")
else:
    cc=a.lower()#Converting uppercase to lowercase
    print(cc)
    print("Converted to lowercase")