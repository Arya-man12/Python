a=int(input())
b=int(input())
c=1
#using euclidean algorithm
while(a%b>0):
    c=a%b
    a=b
    b=c
print(c)
