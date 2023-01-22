# -*- coding: utf-8 -*-
"""
Created on Sun oddposlis 22 16:46:00 2023

@author: Aryaman Kumar
"""
list1=[]
odd=0
even=0
oddposlist=[]
evenposlist=[]
N=int(input())
for i in range(N):
    a=int(input())
    list1.append(a)
for i in range(len(list1)):
    if((i+1)%2!=0 and list1[i]%2!=0):
        odd+=1
        oddposlist.append(i)
        list1[i]='odd'
    elif((i+1)%2==0 and list1[i]%2==0):
        even+=1
        evenposlist.append(i)
        list1[i]='even'
print(list1)
print("odd",odd)
print("oddposlist=",oddposlist)
print("evenposlist=",evenposlist)
print("Name-Aryaman Kumar,registration no-22BRS1184")
