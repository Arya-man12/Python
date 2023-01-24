# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 22:01:46 2023

@author: Aryaman Kumar
"""

n=int(input())
dict1={}
dict2={}
for i in range(n):
    states=input()
    district=int(input())
    dict1[states]=district
list2=dict.keys()
for i in range(len(dict1)):
    for j in range(len(dict1)):
        if(dict1[i]==dict1[j]):
            dict2[dict1(dict1[i])]