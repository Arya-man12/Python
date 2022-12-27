# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 11:58:28 2022

@author: Aryaman Kumar
"""
#Program to find whether input character is uppercase,lowercase or digit
a=input("Enter character")
if(a.islower()==True):
    print("Character is lowercase")
elif(a.isupper()==True):
    print("Character is Uppercase")
elif(a.isdigit()==True):
    print("Character is a digit")