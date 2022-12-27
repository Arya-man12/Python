a=input()
l=[]
l=a.split()
x=0
y=0
for i in range(len(l)):
    c=int(l[i].strip())
    if(c%4==0):
        x=x+1
    else:
        y=y+1
print(x,y)
