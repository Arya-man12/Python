# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 23:53:37 2023

@author: Aryaman Kumar
"""
list1=[]
list2=[]
list3=[]
n=int(input())
for i in range(n):
  n1=int(input())
  list1.append(n1)
if(n%2==0):
    list2=list1[0:n//2]
    list3=list1[n//2:n]
print(list2)
print(list3)
print("Name-Aryaman Kumar,registration no-22BRS1184")