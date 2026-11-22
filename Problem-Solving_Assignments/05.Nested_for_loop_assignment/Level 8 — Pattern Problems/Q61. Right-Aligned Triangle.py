num = int(input("Enter Number: "))
for i in range(1, num + 1):
    for j in range(num - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()