#Program to check whether a given number is palindrome number
a=int(input("Enter the number"))
dig=0
sum=0
temp=a
while(a>0):
    dig=a%10
    a=a//10
    sum=sum*10+dig

if (temp==sum):
     print("Palindrome number")
else:
     print("Not a palindrome number")
