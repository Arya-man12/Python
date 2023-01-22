# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:40:11 2023

@author: Aryaman Kumar
"""

def palindrome(str1):
    str1=str1.lower()
    if(str1==str1[::-1]):
        return True
    else:
        return False
str1=input()
print(len(str1))
if((palindrome(str1)==True)):
    print("Palindrome")
else:
    print("not  palindrome")
print("Name-Aryaman Kumar,registration no-22BRS1184")
