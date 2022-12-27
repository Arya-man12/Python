# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:23:33 2022

@author: Aryaman Kumar
"""
#Program to calculate net pay of the user
bp=int(input("Enter basic pay"))
hra=int(input("Enter HRA amount"))
da=int(input("Enter DA amount"))
de=int(input("Enter amount of deductions"))
net=bp-(hra+da+de)
print("Net pay",net)