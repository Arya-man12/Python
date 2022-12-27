
import re
txt="The rain in Spain"
x2=re.findall("^The.*Spain$",txt)
print(x2)
x=re.findall("ai",txt)
print(x)
x=re.search("\s",txt)
print("First expression",txt)
y=re.search("Portugal",txt)
print(y)
a=re.split("\s",txt)
print(a)
b=re.findall("[a-m]",txt)
print(b)
set1=set(b)
print(set1)
z=re.findall("\d",txt)
print(z)
txt2="helo heoplanet"
x1=re.findall("he.*o",txt2)
y1=re.findall("he.+o",txt2)
print(x1)
print(y1)
z1=re.findall("he.?o",txt2)
print(z1)
z2=re.findall("he.{2}o",txt2)
print(z2)
txt3="When rain falls in spain it stays in the plains"
z3=re.findall("falls|stays",txt3)
if x:
    print(z3)
    print("Match found")
else:
    print("No match")
txt4="8times before 11:45 am"
z4=re.findall("[0-9a-zA-Z]",txt4)
print(z4)

