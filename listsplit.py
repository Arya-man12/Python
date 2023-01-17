# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 20:54:39 2023

@author: Aryaman Kumar
"""
#Program to split a list
N=int(input())
if(N%2==0):
 list1=[]
 for i in range(N):
    n=int(input())
    list1.append(n)
 list2=list1[0:N//2]
 list3=list1[N//2:len(list1)]
 print("list1:")
 for i in list2:
    print(i)
 print("list2:")
 for i in list3:
    print(i)
else:
    print("Even number of elements required")
print("Name-Aryaman Kumar,registration no-22BRS1184")