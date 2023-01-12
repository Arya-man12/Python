# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 00:55:51 2023

@author: Aryaman Kumar
"""
def vowels(str1):
  c1=0
  for i in range(len(str1)):
       if(str1[i] in ('a','e','i','o','u','A','E','I','O','U')):
           c1+=1
  return c1
def consonants(s):
    c2=0
    for i in range(len(s)):
        if (s[i]!=" " and s[i].isdigit()==False and ord(s[i])>=65):
            c2+=1
    c3=c2-vowels(s)
    return c3
s1=input()
print("vowels",vowels(s1))
print("consonants",consonants(s1))
print("Name-Aryaman Kumar,registration no-22BRS1184")