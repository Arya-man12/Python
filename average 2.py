# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 15:38:44 2022

@author: Aryaman Kumar
"""
#Program to find the average and product of numbers entered by the user
inp='true'
avg=0
sum=0
prod=1
count=1
while(inp=='true'):
    n=int(input("Enter number"))
    sum=sum+n
    avg=sum/count
    prod=prod*n
    count=count+1
    e=input("If you wish to continue,press any key ,if you wish to exit press q")
    if(e=='q'):
        inp='false'
print("Average",avg)
print("Product",prod)
print("Name-Aryaman Kumar,registration no-22BRS1184")