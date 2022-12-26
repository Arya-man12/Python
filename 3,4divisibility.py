# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 14:11:34 2022

@author: Aryaman Kumar
"""

n=10
while(n<100):
    if(n%3==0):#divisibility by 3 is checked first and then divisibility by 4
        print(n)
        
    elif(n%4==0):
        print(n)
    n=n+1