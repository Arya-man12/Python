# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 22:39:23 2023

@author: Aryaman Kumar
"""

#Division without using /,// or %
a=int(input("Enter number"))
b=int(input("Enter divisor"))
q=0
sub=a
while(sub>0):
    sub=sub-b
    q=q+1#quotient is number of times the loop runs until divisor can no more be subtracted from original number
rem=a-b*(q)
if(rem<0):#To ensure remainder is not negative and product of quotient and divisor doesnt exceed number
    rem=rem+b
    q=q-1
print("Quotient",q)
print("Remainder",rem)
print("Name-Aryaman Kumar,registration no-22BRS1184")
