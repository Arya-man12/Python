# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 19:11:43 2023

@author: Aryaman Kumar
"""

def Palindrome(str1):
    if(str1[::-1]==str1):
        return True
    else:
        return False
str1=input("Enter string")
if(Palindrome(str1)==True):
    print("Palindrome")
else:
    print("Not a palindrome")
print("Name-Aryaman Kumar,registration no-22BRS1184")