word=input("Enter the string")
uc=lc=0
for a in word:
 if a.islower():
    lc=lc+1
 elif a.isupper():
        uc=uc+1
print("Number of uppercase letters are",uc)
print("number of lowercase letters are" ,lc)
