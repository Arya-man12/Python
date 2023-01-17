# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 21:39:41 2023

@author: Aryaman Kumar
"""

n=int(input())
dict1={}
list1=[]
if(n>0 and n<=10):
    for i in range(1,n+1):
        for j in range(1,i+1):
            list1.append(j)
        dict1[i]=list1
        list1=[]
print(dict1)
print("Name-Aryaman Kumar,registration no-22BRS1184")