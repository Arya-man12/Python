import csv
fh=open("Employee.csv","w")
ewriter=csv.writer(fh)
empdata=[
            ['empno','name','designation','salary'],
            [1000,'tirupti','manager',50000],
            [1002,'ramesh','hod',50000],
            [1003,'suresh','gm',60000]
            ]
ewriter.writerows(empdata)
print("file successfully created")
fh.close()
            
