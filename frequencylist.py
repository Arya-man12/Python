# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 23:37:30 2023

@author: Aryaman Kumar
"""
n=int(input())
list1=[]
list2=[]
dict1={}
for i in range(n):
    a=int(input())
    list1.append(a)

for i in range(n):
    list2.append(list1.count(list1[i]))
    dict1[list2[i]]=list1[i]
set1=set(sorted(list2))
list3=list(set1)
print(list2)
print("Highest frequency",dict1[list3[len(list3)-1]])
print("second highest",dict1[list3[len(list3)-2]])