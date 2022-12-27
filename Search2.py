lst=eval(input("enter list:"))
length=len(lst)
ele=int(input("enter element to be searched for:"))
for i in range (0,length):
    if ele==lst[i]:
         print(ele,"found at index",i)

         break
     else :
          print(ele,"not found in given list")
  
