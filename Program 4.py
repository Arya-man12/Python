f=open("C:\\Users\\Aryaman Kumar\\Word.txt",'r')
lines=f.readlines()
f.close()
f=open("C:\\Users\\Aryaman Kumar\\reword.txt",'w')
f1=open("C:\\Users\\Aryaman Kumar\\newword.txt",'w')
for line in lines:
       if 'a' in lines:
          f1.write(line)
       else:
           f.write(line)
print("All the lines that contain the character a have been saved in newword")
f.close()
f1.close()
f=open("C:\\Users\\Aryaman Kumar\\reword.txt",'r')
f1=open("C:\\Users\\Aryaman Kumar\\newword.txt",'r')
lines=f.readlines()
print("new contents of the word txt file are")
for a in lines:
      print(a,end="")
f.close()
lines=f1.read()
print("\n The contents of the text file are:")
for a in lines:
      print(a,end=" ")
f.close()
f1.close

