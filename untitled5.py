# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 21:10:12 2023

@author: Aryaman Kumar
"""

str1=input()
dict1={}
list1=[]
print(str1)
for i in range(len(str1)):
    dict1[str1[i]]=str1[i].count(str1[i])
    list1.append(str1[i].count(str1[i]))
list1.sort(reverse=True)
