myfile=open("C:\\Users\\Aryaman Kumar\\data.txt",'r')
content=myfile.readlines()
def data():
     for line in content:
           words=line.split()
           for word in words:
               print(word+"a#",end=' ')
           print()
data()
