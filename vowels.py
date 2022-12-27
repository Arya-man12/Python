# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:09:44 2022

@author: Aryaman Kumar
"""
import re
#Program to remove all vowels from a string
r=input("Enter string")
x=re.sub("[aeiouAEIOU]","",r)
print(x)