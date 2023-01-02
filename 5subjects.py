# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 18:18:10 2022

@author: Aryaman Kumar
"""
#Program to calculate total marks and average of five subjects
sum1=0
for i in range(5):
    n=int(input("Enter the marks for subject"))
    sum1+=n
print('Total marks',sum1)
avg=sum1//5
print("Average",avg)
print("Name-Aryaman Kumar,registration no-22BRS1184")