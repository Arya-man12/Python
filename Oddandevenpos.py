# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 21:27:52 2023

@author: Aryaman Kumar
"""
#Program to replace odd element at odd position with odd and even element at even position with even
n=int(input("Enter size of list"))
list1=[]
odd=0
even=0
evenpositionlist=[]
oddpositionlist=[]
for i in range(n):
    n1=int(input())
    list1.append(n1)
for i in range(len(list1)):
    if(list1[i]%2==0 and (i+1)%2==0):
        list1[i]='even'
        odd+=1
        oddpositionlist.append(i)
    elif(list1[i]%2!=0 and (i+1)%2!=0):
        list1[i]='odd'
        even+=1
        evenpositionlist.append(i)
        
print(list1)
print("odd",odd)
print("even",even)
print("oddpositionlist",oddpositionlist)
print("evenpositionlist",evenpositionlist)
print("Name-Aryaman Kumar,registration no-22BRS1184")