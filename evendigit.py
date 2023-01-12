# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:31:06 2022

@author: Aryaman Kumar
"""
#Program to display number with only even digits between 100 to 400
rem=0
sum=0
q=''
for i in range(100,401):
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
        print(i,end=',')
print("Name-Aryaman Kumar,registration no-22BRS1184")
