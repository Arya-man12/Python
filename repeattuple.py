# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 20:57:22 2023

@author: Aryaman Kumar
"""
t1=eval(input())
dict1={}
for i in range(len(t1)):
    if(t1.count(t1[i])>1):
       dict1[t1[i]]=t1.count(t1[i])
print(list(dict1.keys()))
print("Name-Aryaman Kumar,registration no-22BRS1184")
