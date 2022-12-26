n=int(input("Enter numbers of student"))
for i in range (0,n): 
               student_name=input("Enter names of student")
               student_rollno=int(input("enter roll no of student"))
               mark1=int(input("Enter marks of student out of 100"))
               dict={'name':student_name,'rollno':student_rollno,'mark':mark1}
               if(int(mark1)>75):
                 print(dict['name'],"is having more than 75")
               else:
                 print(dict['name'],"is not having more than 75")
                        
                
                                 
