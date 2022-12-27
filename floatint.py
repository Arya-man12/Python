# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:52:15 2022

@author: Aryaman Kumar
"""
#Elements of list of float data type are converted to int data type and duplicates are removed
l=int(input("Enter the length of the list"))
l1=[]
for i in range(0,l):
    n=float(input("enter element"))
    l1.append(n)
    print(l1)
for i in range(0,l):
    l1[i]=int(l1[i])
    print(l1)
for i in range(0,l):
    print(i)
    for j in range(0,l):
        print(j)
        if(l1[j]==l1[i] and j!=i):
            l1.remove(l1[j])
        else:
            continue
print(l1)        