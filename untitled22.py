# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 22:39:57 2022

@author: Aryaman Kumar
"""
import re
a=input()
b=input()
list1=a.split("")
list2=b.split("")
str1=list1[0]+list2[0]
print(str1)
if (len(list1)>=len(list2)):
    for i in range(1,len(list1)):
      if(i==1):
        str1=list1[1]+ list2[1]
      elif(i%2==0):
          str1+=str1+list1[i]
print(str1)
        