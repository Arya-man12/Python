n=int(input())
div=0
count=0
for i in range(2,n-1):
    if(n%i==0):
        while(div>0):
            div=n%i
            count=count+1
    
print(count)
