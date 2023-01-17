# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 20:47:06 2023

@author: Aryaman Kumar
"""
#Program to print shortest name in list
list1=[]
N=int(input())
for i in range(N):
    a=input()
    list1.append(a)
list1.sort(key=len)
print(list1[0])
for i in list1:
    if len(i)==len(list1[0]) and i!=list1[0]:
        print(i)
print("Name-Aryaman Kumar,registration no-22BRS1184")