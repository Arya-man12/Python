
       
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    
    print("\n")
rows2 = 5
for i in range(1, rows2 + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
