# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 19:36:36 2022

@author: Aryaman Kumar
"""

def is_anagram(s1,s2):
    if s1.split()in s2 or s2.split() in s1:
        return True
    else:
        return False
str1=input("Enter string 1")
str2=input("Enter string 2")
if(is_anagram(str1,str2)==True):
    print("anagram")
else:
    print("Not anagram")