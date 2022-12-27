lst=[]
num=int(input("How many numbers"))
for n in range(num):
  number=int(input("Enter number"))
  lst.append(number)
  for i in range(len(lst)):
      temp=lst[i]
      sum=0
      while(temp>0):
       digit=temp%10
       sum+=digit**3
       temp//=10
  if(lst[i]==sum):
   print(lst[i]==sum)
   print(lst[i],"is equal to the sum of digit")

  else:
    print(lst[i],"is not equal to the sum of cubes of the digit")

print("The smallest number in given list is ",min(lst))
print("The largest number in given list is ",max(lst))
