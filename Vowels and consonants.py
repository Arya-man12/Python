str=input("Enter the string")
vc=cc=0
str=str.lower()
for i in range(0,len(str)):
    if str[i] in('a','l','i'):
        vc=vc+1
    elif(str[i]>='a' and str[i]<='z'):
        cc=cc+1

print("Number of vowels are:",vc)
print("Number of consonants are :",cc)
