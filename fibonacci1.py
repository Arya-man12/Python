#program to print fibonacci numbers upto a user defined value n
sum=0
a=0
b=1
n=int(input())
for i in range(0,n):#loop runs till number n
    sum=a+b
    b=a
    a=sum
    print(sum)#next element in series printed
