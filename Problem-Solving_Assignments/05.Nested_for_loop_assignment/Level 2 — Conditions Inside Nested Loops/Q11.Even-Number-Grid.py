row = int(input("Enter row number: "))
col = int(input("Enter column number: "))
for i in range(1,4):
    for j in range(1,4):
        if i == 1 and j ==1 or i ==2 and j == 1 or i ==3 and j==1: 
            print("2", end=" ")
        elif i ==1 and j==2 or i ==2 and j== 2 or i ==3 and j==2:
            print("4", end=" ")
        elif i == 1 and j ==3 or i ==2 and j == 3 or i ==3 and j==3:
            print("6", end=" ")
    print()


row = int(input("Enter row number: "))
col = int(input("Enter column number: "))
for i in range(1,row+1):
    for j in range(2,col+1,2):
        print(j,end=" ")
    print()
