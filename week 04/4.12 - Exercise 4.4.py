# first way
rows = int(input("Please enter the size (no of rows) of the triangle you wish to display:\n"))

for i in range(1, rows + 1):
    print("*" * i)
    
# second way
rows = int(input("Please enter the size (no of rows) of the triangle you wish to display:\n"))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end = "")
    print()