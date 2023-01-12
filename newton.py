# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:07:34 2023

@author: Aryaman Kumar
"""

n=int(input("Enter the number"))
x=n
a=True
while(a==True):#root=x+n/x where x is the assumed value of the root and n is the number
    root=0.5*(x+n/x)
    if((root-x)<0):
        root2=(root-x)*-1
    if(root2<1):
        a=False
    x=root
print("Square root",int(root))
print("Name-Aryaman Kumar,registration no-22BRS1184")
