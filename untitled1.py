# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 00:38:48 2023

@author: Aryaman Kumar
"""

myfile=open("C:\\Users\\Aryaman Kumar\\Desktop\\programs\\text1.txt","r+")
user=input("Enter string")

myfile.write(user)
str1=myfile.read()
print(str1)
str2=""
for i in range(len(str1)):
    if(len(str1[i])>len(str1[i+1])):
        str2=str1[i]
    else:
        str2=str1[i+1]
print("longest word is",str2)