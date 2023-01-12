# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 00:53:10 2023

@author: Aryaman Kumar
"""

def strcopy(str1,str2):
    if(len(str2)==0):
        return str1
    else:
        s3=strcopy(str1,(str2)[1:-1])
        return s3
str3="hello"
str4=""
print(strcopy(str3,str4))