# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 18:27:58 2022

@author: Aryaman Kumar
"""
#Program to calculate net pay
BP=int(input("Enter basic pay"))
DA=88/100*BP
HRA=8/100*BP
CCA=1000
insurance=2000
PF=PF=10/100*BP
Dd=insurance+PF
GP=BP+DA+HRA+CCA
Net=GP-Dd
print(Net)
print("Name-Aryaman Kumar,registration no-22BRS1184")