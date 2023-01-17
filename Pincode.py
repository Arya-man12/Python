# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 23:19:37 2023

@author: Aryaman Kumar
"""
#Program to check if pincode is valid or not
import re
pin=input()
x=re.search("^[1-9].{4}[0-9]$",pin)
if x:
    print("Valid pin")
else:
    print("Not valid pin")
print("Name-Aryaman Kumar,registration no-22BRS1184")