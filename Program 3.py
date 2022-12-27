f=open("C:\\Users\\Aryaman Kumar\\words.txt,'r')
lines=f.readlines()
f.close()
f=open("C:\\Users\\Aryaman Kumar\\words.txt",'w')
f=open("C:\\Users\\Aryaman Kumar\\newword.txt",'w')
for line in lines:
       if 'a' in lines:
          f.write(line)
       else:
           f.write(line)
print("All the lines that contain the character a have been deleted')
