# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 22:27:56 2022

@author: Aryaman Kumar
"""
#Program to calculate total marks,average ,grade and print name and ID of N students
sum1=0
def student(name,id1):
    
    for i in range(5):
        print("Enter marks of subject",+(i+1))
        marks=int(input())
        total(marks)
    print("Name",name)
    print("ID",id1)
    print("total marks",sum1)
    print("Average",avg(sum1))
    grade(sum1)
    
def total(n1):
    global sum1
    sum1+=n1
    print(sum1)
    return sum1
def avg(sum2):
    avg=sum2//5
    return avg
def grade(n1):#Assuming 500 as total marks
    if(sum1>=450):
        print("A grade")
    elif(sum1>=400):
        print("Bgrade")
    elif(sum1>=300):
        print("C grade")
    elif(sum1>=200):
        print("D grade")
    elif(sum1>=150):
        print("Egrade")
    else:
        print("Fail")
N=int(input("Enter number of students"))
for i in range(N):
    name=input("Enter name")
    ID=input("Enter ID")
    student(name,ID)
    sum1=0
print("Name-Aryaman Kumar,registration no-22BRS1184")