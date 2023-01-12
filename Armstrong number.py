# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:26:31 2022

@author: Aryaman Kumar
"""

#Program to find whether a given number is armstrong number or not
n=int(input("Enter the number"))
rem=0
sum=0
temp=n
while(n>0):
   rem=n%10
   sum=sum+rem**3#Calculating sum of cubes
   n=n//10
if(sum==temp):#If original number equals sum of cubes of its digit it is armstrong number
    print("It is a armstrong number")
else:
    print("It is not armstrong number")
print("Name-Aryaman Kumar,registration no-22BRS1184")