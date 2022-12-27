n=int(input("enter range"))
rem=0
sum=0
count=0
l1=[]
for i in range(0,n):
    a=i
    while(count<10):
         rem=n%10
         a=a//10
         sum=sum+rem^2
    if(sum==1):
        l1.append(i) 
    a=sum
    count=count+1
print(l1)
