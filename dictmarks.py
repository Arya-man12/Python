# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 20:35:23 2023

@author: Aryaman Kumar
"""
dict1={}
n=int(input("Enter number of students"))
for i in range(n):
    names=input()
    marks=int(input())
    dict1[names]=marks
print("Sum of marks",sum(list(dict1.values())))
print("Name-Aryaman Kumar,registration no-22BRS1184")