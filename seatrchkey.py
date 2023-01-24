# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 16:58:17 2023

@author: Aryaman Kumar
"""
dict1={}
n=int(input())
for i in range(n):
    k=int(input())
    v=int(input())
    dict1[k]=v
s=int(input())
if s in dict1:
    print("Key existing")
else:
    print("Key not existing")
print("Name-Aryaman Kumar,registration no-22BRS1184")
