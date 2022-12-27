# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 17:43:54 2022

@author: Aryaman Kumar
"""

#Program to display number with only even digits between 100 to 400
rem=0
sum=0
l=[]
q=''
for i in range(1,401):
    n=i
    while(n>0):#loop to check if digits are even
        rem=n%10
        if(rem%2!=0):#If digit is odd loop is broken
            q=False
            break
        else:
            q=True
           
        n=n//10
    if(q==True):
        l.append(i)#number is stored in list
for i in range(0,len(l)):
    print(l[i])