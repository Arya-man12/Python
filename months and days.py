# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:29:36 2022

@author: Aryaman Kumar
"""

l1=['Jan','Feb','March','April','May','June','July','August','September','October ','November','December']
l2=[31,28,31,30,31,30,31,31,30,31,30,31]
month=input("Enter month")
for i in range(0,len(l1)):
    if(month==l1[i]):
      print(l2[i])
    