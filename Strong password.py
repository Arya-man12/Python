# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:14:42 2022

@author: Aryaman Kumar
"""
import re
#Program to check for strong password
pasw=input("Enter password")
x=re.search("^.{8}",pasw)
if x:
   y=re.findall("[a-z]",pasw)
   if y:
       z=re.findall("[A-Z]",pasw)
       if z:
           a=re.findall("[0-9]",pasw)
        
           if a:
               b=re.findall("[$%^&*@#]",pasw)
               if b:
                   print("Strong password")
               else:
                   print("Weak password")
           else:
              print("Weak password")
       else:
            print("Weak password")
   else:
    print("Weak password")
else:          

    print("Weak password")