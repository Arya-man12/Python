# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 10:34:27 2022

@author: Aryaman Kumar
"""
#program to compute exponentiation without** operator

n=int(input("Enter the number"))
i=int(input("Enter power of number"))
count=0
expo=1
while(count<i):
    #number is multiplied by itself for the number of times 
    expo =expo*n    #specified by the user
    count=count+1
print(expo)
