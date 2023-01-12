# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 17:07:19 2022

@author: Aryaman Kumar
"""
#Ackermann function
def A(m,n):
    if(m==0):
        return n+1
    if (m>0 and n==0):
        return A(m-1,1)
    if(m>0 and n>0):
        return A(m-1,A(m,n-1))
m=int(input("Enter m value"))
n=int(input("Enter n value"))
c=A(m,n)
print(c)
print("Name-Aryaman Kumar,registration no-22BRS1184")