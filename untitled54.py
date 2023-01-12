# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 20:58:32 2023

@author: Aryaman Kumar
"""

def reverse(str1):
    if(len(str1)==1):
        return str1
    else:
       str2=str1[-1]+reverse(str1[1:len(str1)-2])
       return str2
s=input()
print(reverse(s))