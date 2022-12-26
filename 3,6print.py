# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 16:41:13 2022

@author: Aryaman Kumar
"""
#Program to print every number in the given range except 3 and 6
for i in range(0,6):
    if(i==3 or i==6):
        continue
    else:
        print(i)