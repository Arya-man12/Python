n=int(input(""))
sum=0
rev=0
while(n>0):   
    rev=n%10
    n=n//10
    sum=sum*10+rev
    print(sum)
    
