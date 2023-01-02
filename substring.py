# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 13:07:20 2022

@author: Aryaman Kumar
"""
#Program to find number of times a substring appears in a string and first index of appearance of the string
str1=input("Enter string")
str2=input("Enter substring")
def check(s1,s2):
    b=str1.count(str2,0,len(str1)-1)
    return b
def check2(s1,s2):
    b=str1.find(str2)
    return b
print(check(str1,str2))
print("First instance at index ",check2(str1,str2))
print("Name-Aryaman Kumar,registration no-22BRS1184")