l=[32,43,56,31,1,2]
c=0
n=1
for i in range(0,len(l)-1):
  for i in range(0,len(l)-1):
      if(l[i]>l[i+1]):
               c=l[i+1]
               l[i+1]=l[i]
               l[i]=c
  
      
               
print(l)
print(l[len(l)-2])
