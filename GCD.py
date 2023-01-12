#Program to find HCF of a number using euclidean algorithm and common factor method
a=int(input("Enter first number"))
b=int(input("Enter second number"))
x=a
y=b
c=1
i=1
fact=0
#using euclidean algorithm
while(b>0):
    c=a%b
    a=b
    b=c
print(a,"is HCF by Euclidean method")
#Using common factor method
while((x//i)>0 and (y//i)>0):
  if(x%i==0 and y%i==0):
     fact=i
     i=i+1
  else:
      i=i+1
print(fact,"is HCF by common factor method")
print("Name-Aryaman Kumar,registration no-22BRS1184")
