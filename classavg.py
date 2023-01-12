# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:21:15 2023

@author: Aryaman Kumar
"""
#Class average
n=int(input("Enter the number of marks of students to be entered"))
list1=[]
for i in range(n):
    a=int(input())
    list1.append(a)
sum1=0.0
for i in range(len(list1)):
    sum1+=list1[i]
print(sum1)
avg=sum1//len(list1)
print("Average",avg)
print("Name-Aryaman Kumar,registration no-22BRS1184")