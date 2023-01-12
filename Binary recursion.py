# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 21:58:32 2023

@author: Aryaman Kumar
"""

def binary(n):
  if(n==0):
      return 0
  else:
      return n%2+10*(binary(n//2))
n1=int(input())
print(binary(n1))