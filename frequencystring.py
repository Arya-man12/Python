# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:28:54 2023

@author: Aryaman Kumar
"""
#Program to display frequency of letters in a string
dict1={}
def frequency(str1):
    for i in range(len(str1)):
        dict1[str1[i]]=str1.count(str1[i])
    return dict1
str1=input("Enter string")
print(frequency(str1))
print("Name-Aryaman Kumar,registration no-22BRS1184")
