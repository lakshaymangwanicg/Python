number = int(input("Enter a number: "))
for i in range(1,number+1):
    for j in range(1,number+1):
        if i%j == 0:
            print("X",end=" ")
        else:
            print("-", end=" ")
    print()