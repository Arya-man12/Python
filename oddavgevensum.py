# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:34:55 2022

@author: Aryaman Kumar
"""
OddAverage=0
EvenSum=0
count=0
l=int(input("Enter the size of the list"))
list1=[]
for i in range(0,l):
    n=int(input("Enter element"))
    list1.append(n)
for i in range(0,l):
     if(i%2==0):
         OddAverage=OddAverage+list1[i]
         count=count+1
     else:
         EvenSum=EvenSum+list1[i]
print(OddAverage)
OddAverage=OddAverage/count
print(OddAverage)
print(EvenSum)