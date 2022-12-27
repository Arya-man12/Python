# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 19:41:37 2022

@author: Aryaman Kumar
"""
#To find sum of series 1 + 2/4 + 3/9 + ....+ N/(N*N)

N=int(input("Enter the last term of the series"))
sum=0
for i in range(1,N+1):
    sum=sum+i/(i*i)
print(sum)