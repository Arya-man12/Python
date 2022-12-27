# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:16:06 2022

@author: Aryaman Kumar
"""
temp=0
s=[]
l=[86,86,85,85,83,23,45,84,1,2,0]
for i in range(0,len(l)-1):
    for i in range(0,len(l)-1):#sorting list in ascending order
        if(l[i]>=l[i+1]):
            temp=l[i+1]
            l[i+1]=l[i]
            l[i]=temp
            s.extend(l)
print("highest marks",s[len(s)-1])#last element of sorted list is highest marks
for i in range(0,len(s)):#ensuring duplicate element is not considered as second highest marks
    if(s[-i]!=s[len(s)-1]):
        print("second highest marks",s[-i])
        break