# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 22:54:54 2023

@author: Aryaman Kumar
"""
Divisiblecount=0
Nondivisiblecount=0
while(True):
    n=int(input())
    if(n==-100):
        print("Divisible count is ",Divisiblecount)
        print("Nondivisible count is",Nondivisiblecount)
        print("Name-Aryaman Kumar,registration no-22BRS1184")
    if(n%2==0 and n%3==0):
        Divisiblecount+=1
    else:
        Nondivisiblecount+=1
print("Name-Aryaman Kumar,registration no-22BRS1184")