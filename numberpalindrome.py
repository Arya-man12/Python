# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 23:03:04 2023

@author: Aryaman Kumar
"""

def palindrome(n):
    if(n<0):
        return 
    else:
        return n%10+10*palindrome(n//10)
n1=int(input())
print(palindrome(n1))