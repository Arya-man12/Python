#program to count number of prime numbers and composite number
PrimeCount=0
CompositeCount=0
n=0
a='true'
while():#if -1 is encountered program stops
    P='true'
    if(n==-1):
      a='false'
      break
    n=int(input(""))
    for i in range(2,n-1):
        if(n%i==0):
            CompositeCount=CompositeCount+1
            P='false'
            break
    if(P=='true'):
        PrimeCount=PrimeCount+1
print(CompositeCount)
print(PrimeCount)

            
