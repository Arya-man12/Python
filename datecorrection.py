# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 22:52:56 2023

@author: Aryaman Kumar
"""
import re
dict1={1:'JAN',2:'FEB',3:'MAR',4:'APR',5:'MAY',6:'JUN',7:'JUL',8:'AUG',9:'SEP',10:'OCT',11:'NOV',12:'DEC'}
str1=input()
x=re.findall("^[0-9].{3}[-][A-Z].{3}",str1)
if x:
   print("Valid Date")
y=re.findall("^[0-9].{1}[-][0-9].{1}",str1)
if(y):
     list2=re.findall("[0-9].{3}$",str1)
     str2=list2[0]
     list1=re.findall("^.{^3}[0-9].{1}",str1)
     str3=str(dict1[int(list1[0])])
     list3=re.findall("^[0-9].{1}",str1)
     str4=list3[0]
     str5=str2 +"-"+str3 +"-"+str4
     print(str5)
     print("Format corrected")
print("Name-Aryaman Kumar,registration no-22BRS1184")