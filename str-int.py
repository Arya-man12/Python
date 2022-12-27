a=input()
a=a+' '
c=' '
i=0
x=0
y=0
while(i<len(a)):
    if(a[i]==' '):
        if(int(c)%4==0):
            x=x+1
            
        elif(int(c)==-1):
         break;
        else:
            y=y+1
        c=' '
    else:
            c=c+a[i]
    i=i+1
print(x,y)
