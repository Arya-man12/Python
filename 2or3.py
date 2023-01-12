# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 21:11:52 2023

@author: Aryaman Kumar
"""
#Program to find if number is divisible by 2 or 3
c1=0
c2=0
while(True):
    n=int(input(""))
    if(n==-100):
        break#Terminating condition
       
    if(n%2==0 or n%3==0):
        c1+=1
    else:
       c2+=1
print("Divisible count is",c1)
print("Non divisible count is",c2)
print("Name-Aryaman Kumar,registration no-22BRS1184")