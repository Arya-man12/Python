# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 12:16:40 2022

@author: Aryaman Kumar
"""
#Program to display pattern of five rows of stars in increasing and decreasing order by row

for i in range(0,6):
    for j in range(0,i):
        print("*",end='')
    print('')
for i in range(4,0,-1):
    for j in range(i,0,-1):
        print('*',end='')
    print('')