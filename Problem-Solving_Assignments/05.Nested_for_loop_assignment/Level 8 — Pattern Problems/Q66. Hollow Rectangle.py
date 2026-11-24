row = int(input("Enter rows Number: "))
column = int(input("Ener columns Number: "))
for i in range(row):
    for j in range(column):
        if i == 0 or j == 0 or i == row-1 or j==column-1:
            print("#",end="")
        else:
            print(" ",end="")
    print()
