# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 15:28:55 2022

@author: Aryaman Kumar
"""

#Program to calculate grade of student based on marks
marks=int(input("Enter the marks of the student"))
if(marks>=90):
    print("A")
elif(marks>=70 and marks<90):
    print("B")
elif(marks>=50 and marks<70):
    print("C")
elif(marks>=35 and marks<50):
    print("D")
else:
    print("E")
print("Name-Aryaman Kumar,registration no-22BRS1184")