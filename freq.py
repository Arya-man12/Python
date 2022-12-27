

lst=eval(input("enter list:"))
length=len(lst)
ele=int(input("enter element:"))
count=0
for i in range (0,length):
   if ele==lst[i]:
    count=count+1
    if count==0:
     print(ele,"not found in given list")


    else:
     print(ele,"has frequency as", count ,"in given list")
 
