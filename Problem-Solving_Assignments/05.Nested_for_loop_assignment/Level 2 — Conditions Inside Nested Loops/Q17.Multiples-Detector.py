number = int(input("Enter a number: "))
for i in range(1,number+1):
    for j in range(1,number+1):
        if j%i == 0:
            print(j,end=" ")
        else:
            print("", end="")
    print()