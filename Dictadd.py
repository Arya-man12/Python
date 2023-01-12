# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 21:48:42 2023

@author: Aryaman Kumar
"""
#Program to add two values of two seperate dictionaries if they have the same key 
Dict1 = {'A': 100, 'B': 200, 'C':300}
Dict2 = {'A': 300, 'B': 500, 'D':400}
newdict={}
list1=list(Dict1.keys())
list2=list(Dict2.keys())
for i in range(len(Dict1)):
    for j in range(len(Dict2)):
        if(list1[i]==list2[j]):
           newdict[list1[i]]=Dict1[list1[i]]+Dict2[list2[i]]
        elif(list1[i] not in list2):
             newdict[list1[i]]=Dict1[list1[i]]
        elif(list2[j] not in list1):
            newdict[list2[j]]=Dict2[list2[j]]
print(newdict)
print("Name-Aryaman Kumar,registration no-22BRS1184")