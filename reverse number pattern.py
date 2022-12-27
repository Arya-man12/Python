# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 12:21:38 2022

@author: Aryaman Kumar
"""
#Program to display pattern of five rows of numbers in decreasing order
for i in range(0,6):
    for j in range(i,0,-1):
        print(j,end='')
    print('')
        