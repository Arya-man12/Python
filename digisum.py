n=int(input())
sum=0 
dig1=0
dig2=0
temp=n
count=0
while(n>0):
    for i in range(0,n):
        temp=temp//10^i
        count=count+1
        if(n<0):
            break
    if(n>10^count):
        dig1=n%10
        
    if(n<10):
         dig2=n
    n=n//10
sum=dig1+dig2
print(sum)
