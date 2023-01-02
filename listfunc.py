# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 23:05:42 2023

@author: Aryaman Kumar
"""
#Program to perform operations using inbuilt list functions
list1=[]
n=int(input("Enter number of students"))
for i in range(n):
    s=input("Enter names")
    list1.append(s)
print(list1)
print("Count of students",len(list1))
s2=input("Enter name which you want to replace")
s3=input("Enter name which you want to enter instead")
list1[list1.index(s2)]=s3
print(list1)
list1.sort()
print(list1)
s4=input("Enter name which you wish to insert")
a=int(input("Enter position at which name is to be inserted"))
list1.insert(a,s4)
print(list1)
s5=input('Enter students name to be searched for')
print(s5,"at index",list1.index(s5))
s6=input("Enter students name to be removed")
list1.remove(s6)
print(list1)
print("Name-Aryaman Kumar,registration no-22BRS1184")