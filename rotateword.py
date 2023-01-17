# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 12:54:05 2022

@author: Aryaman Kumar
"""
#Program to encrypt a string by adding specified number to ASCII value
def rotate_word(str1,n):
    rt=""
    b=0
    for i in range(len(str1)):
        b=ord(str1[i])+n
        rt+=chr(b)
    return rt
a=input()
n1=int(input())
c=rotate_word(a,n1)
print(c)
if c[0] in ('a','e','i','o','u','A','E','I','O','U') and c[len(c)-1] in('a','e','i','o','u','A','E','I','O','U'):
    print("Happy cool string") #To check if first and last letter are vowels
else:
    print("Happy hot string")
print("Name-Aryaman Kumar,registration no-22BRS1184")