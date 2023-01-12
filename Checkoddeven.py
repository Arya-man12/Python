# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 17:55:18 2022

@author: Aryaman Kumar
"""
#Function to add odd and even numbers seperately in a given list of numbers
def CheckOddEven(n):
    flag=0
    if(n%2==0):
        flag=1
        return flag
    else:
        return flag

N=int(input("Enter number of numbers"))
sum1=0
sum2=0
list1=[]
for i in range(N):
    num=int(input("Enter number"))
    list1.append(num)
for i in range(len(list1)):
 a=CheckOddEven(i)
 if(a==1):
        sum1+=list1[i]
 else:
        sum2+=list1[i]
print("Even number sum",sum1)
print("Odd number sum",sum2)
print("Name-Aryaman Kumar,registration no-22BRS1184")