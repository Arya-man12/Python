import pickle
emp={}
empfile=open('Emp1.dat','rb')
empfile.seek(9)
print(empfile.tell())
try:
    while True :
        emp=pickle.load(empfile)
        print(emp)



except EOFError:
    empfile.seek(9,1)
    empfile.tell()
    empfile.close()

