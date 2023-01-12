# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 13:58:28 2022

@author: Aryaman Kumar
"""
#Program to check whether year is leap year or not
n=int(input("Enter the year"))
if(n%100==0):
 if(n%400==0):#If a leap year is also divisible by 100 then it has to 
              #be divisible by 400 to be a leap year
     print("It is leap year")
 else:
     print("It is not a leap year")
elif(n%4==0):#If a year not divisible by 100 is divisible by 4 it is a 
             #leap year
    print("It is leap year")
else:
    print("It is not a leap year")
print("Name-Aryaman Kumar,registration no-22BRS1184")