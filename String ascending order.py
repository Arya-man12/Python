# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 19:04:27 2023

@author: Aryaman Kumar
"""
list1=[]
def sorted(list1):
    for i in range(len(list1)-1):
        if(list1[i]>list1[i+1]):
           list1[i],list1[i+1]=list1[i+1],list1[i]
    return list1
n=int(input("Enter number of elements in list"))
for i in range(n):
    n1=input("Enter element")
    list1.append(n1)
print("Sorted list",sorted(list1))
print("Name-Aryaman Kumar,registration no-22BRS1184")
