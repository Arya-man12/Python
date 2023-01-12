# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 16:33:06 2022

@author: Aryaman Kumar
"""
#Prime number using recursion
def prime(n,i):
    if(n<=2):  #1 and 2 are prime numbers
        return True
    if(n%i==0): #not a prime number
        return False
    if(i*i>n):#if this is true it means further values of i cannot divide this number,hence it is a prime number
        return True#terminating condition
    else:
        return prime(n,i+1)
num=int(input("Enter number"))
if(prime(num,2)==True):
    print("Prime number")
else:
    print("Not a prime number")
print("Name-Aryaman Kumar,registration no-22BRS1184")