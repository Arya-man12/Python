# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 21:25:27 2023

@author: Aryaman Kumar
"""

states=[]
n=int(input("Enter number of states"))
for i in range(n):
    a=input("Enter name of state")
    n1=int(input("Enter number of districts"))
    states[a]=n1
list1=list(states.values())
list2=list(states.keys())
list3=[]
dict2={}
for i in range(len(states)-1):
 for j in range(len(states)-1):
  if(list1[i]==list1[j]):
        list3.append(list2[i])
        list3.append(list1[j])
        dict2[states[list2[i]]]=list3
print()
print(len(list3))
print(dict2)