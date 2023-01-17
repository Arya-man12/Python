# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 00:02:23 2023

@author: Aryaman Kumar
"""
#Program to print average of list with two zeroes
n=int(input())
list1=[]
for i in range(n):
    a=int(input())
    list1.append(a)
avg=float(sum(list1)/len(list1))
print("%.2f" % avg)
print("Name-Aryaman Kumar,registration no-22BRS1184")