# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 20:34:20 2023

@author: Aryaman Kumar
"""
#Program to display only the Initials and lastname of a given name
str1=input()
list1=str1.split(" ")
str2=""
for i in range(0,len(list1)-1):
    str2=str2+list1[i][0]+"."
str2=str2+list1[len(list1)-1]
print(str2)
print("Name-Aryaman Kumar,registration no-22BRS1184")