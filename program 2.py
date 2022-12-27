def word() :
    myfile=open("C:\\Users\\Aryaman Kumar\\word.txt","r")
    ch=myfile.read()
    print("the content of the text file :")
    print(ch)
    vcount=ccount=0
    for i in range(0,len(ch)):
        data=ch[i].lower()
        if data in ['a','e','i','o','u']:
                vcount+=1
        elif data>='a' and data<='z':
                ccount+=1
    print("the number of vowels present in text file is:",vcount)
    print (" the number of consonants  present in text file is :",ccount)
word()
        
