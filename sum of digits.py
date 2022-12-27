# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:16:49 2022

@author: Aryaman Kumar
"""
#Program to find the sum of digits
n=int(input("Enter the number"))
rem=0
sum=0
while(n>0):
   rem=n%10
   sum=sum+rem
   n=n//10
print("Sum of digits",sum)