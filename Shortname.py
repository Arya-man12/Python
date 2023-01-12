# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 14:11:22 2023

@author: Aryaman Kumar
"""

name=input()
n2=name.split(" ")
n3=" "
for i in range(len(n2)-1):
  n3=n3+n2[i][0]+"."
n4=n3+n2[len(n2)-1]
print(n4)
print("Name-Aryaman Kumar,registration no-22BRS1184")