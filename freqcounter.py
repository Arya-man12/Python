# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 20:13:22 2023

@author: Aryaman Kumar
"""
#Program to store number of uppercase,lowercase and special characters in a string
dict1={}
def freqcounter(str1):
    Uc=Uppercase(str1)
    lc=lowercase(str1)
    dig=digit(str1)
    dict1["Uppercase"]=Uc
    dict1["lowercase"]=lc
    dict1["Special character"]=len(str1)-(dig+Uc+lc)
    return dict1
def Uppercase(str1):
    c1=0
    for i in range(len(str1)):
        if(str1[i].isupper()==True):
            c1+=1
    return c1
def lowercase(str1):
    c2=0
    for i in range(len(str1)):
        if(str1[i].islower()==True):
            c2+=1
    return c2
def digit(str1):
    c3=0
    for i in range(len(str1)):
        if(str1[i].isdigit()==True):
            c3+=1
    return c3
str1=input()
print("Name-Aryaman Kumar,registration no-22BRS1184")
print(freqcounter(str1))
