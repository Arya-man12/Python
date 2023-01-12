# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 23:51:57 2023

@author: Aryaman Kumar
"""

def tiles(A,i):
    print(A)
    if(2^(i+1)>=A//2):
        return 1
    else:
       print(i)
       s=(2**i)+tiles(A,i+1)
       return s
N=int(input())
M=int(input())
print(tiles(N*M,0))