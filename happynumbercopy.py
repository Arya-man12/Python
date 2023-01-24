# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 23:28:43 2023

@author: Aryaman Kumar
"""

def Happy_num(n):
  past = set()
  while n != 1:
     for j in str(n):
        n=sum(int(j)**2)
        n=str(n)
        if n in past:
           return False
        past.add(n)
  return True
n=int(input())
for i in range(n):
    if(Happy_num(i)==True):
        print(i)
    