# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 17:50:39 2022

@author: Aryaman Kumar
"""
#Print fizz for all multiples of 3 , buzz for all multiples of 5 and fizzbuzz for multiples of 3 and 5
for i in range(1,50):
    if(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    elif(i%3==0 and i%5==0):
        print("FizzBuzz")
    else:
        print(i)
print("Name-Aryaman Kumar,registration no-22BRS1184")