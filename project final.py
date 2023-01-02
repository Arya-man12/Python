import time

Library=['britannica', 'harry potter', 'HC Verma']
borrowed=[]

while(True):
         print("*******************")
         print('Welcome to the library.enter your choice to continue')
         print("1.Display books")
         print("2.borrow books")
         print("3.Add books")
         print("4.Return book(s)")
         print("5.enter to see number of books")
         print("6.see users and books borrowed")
         print("*******************")
         user_choice=input("enter choice : ")
         a=int(user_choice)
      
       if (a>6):
        print("Invalid choice, please try again")


       if (a==1):
         print("We have the following books in our AI library:",Library)
            
       if (a==2):
                 while(True):
                 user=input("enter your name")
                 
                 book=input("Enter the name of the book you want to borrow")
                 if book not in Library:
                   print("Book not available ")
                 else:
                  tnow = time.time()   
                  borrowed.append([book, user, tnow])
                  Library.remove(book)
                  print("Book Database has been updated, you can take the book")

                  print("if you are done press d")
                  c=input()
                  if(c=='d'):
                      break
                  
                 
                     

       if (a==3):
                book=input("Enter the name of the book you want to add:")
                Library.append(book)
                print("book has been added")
                
       if (a==4):
                  while(True):
                 book=input("Enter the name of the book you want to return:")
                 found = [item for item in borrowed if item[0] == book]
                 print(found)
                 if (len(found) == 0):
                   print("book not from this library")
                 else:
                   rettime = time.time()
                   time_delta = (rettime - found[0][2])
                   print("Book returned after", time_delta, "seconds")
                   delay_time = time_delta//30
                   if (delay_time > 1):
                     print("You have to pay a fine of ", (delay_time - 1) * 5, "Rupees")
                   Library.append(book)
                
                   borrowed.remove(found[0])
                   print("book has been returned")

                    print("if you are done press d")
                  c=input()
                  if(c=='d'):
                      break

       if(a==5):
                 num=len(Library)
                 print("number of books in library",num)
      
       if(a==6):
                if (len(borrowed)==0):
                  print("no book has been issued")
                for x in range (len(borrowed)):
                 print("borrowed by", borrowed[x])

       print("\n\nPress q to quit or press enter to continue")
       uc=input()
       if uc=='q':
        print("thank you")
        exit()
       continue
