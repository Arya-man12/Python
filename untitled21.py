# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 22:57:35 2022

@author: Aryaman Kumar
"""

txt = "\110\145\154\154\157"
print(txt)
txt1= "\x60\x65\x6c\x6c\x6f"
print(txt1)
txt2="welcome to the jungle"
bb=len(txt2)

print(txt2.zfill(bb-7))
txt3="banana"
print(txt3.rjust(20,"h"))
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
txt = "banana,,!,,,ssqqqww....."
x = txt.rstrip(",.qsw!")
print(x)
d1={"name":'John',"country":'name'}
myseperator='Test'
x=myseperator.join(d1)
print(x)