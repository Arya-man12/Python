# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 12:20:08 2023

@author: Aryaman Kumar
"""

def recaman(a,n,lim):
      if(n==0):
          return(recaman(0,1,lim))
      if(a>lim):
          return ""
      if(a-n>0):
          print(a-n)
          return recaman(a-n,n+1,lim)
      else:
          print(a+n)
          return recaman(a+n,n+1,lim)
lim=int(input())

print(recaman(1,0,lim))