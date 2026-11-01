number = int(input("Enter a number: "))
for i in range(number):
    for j in range(number):
        if i == j:
            print("Same", end=" ")
        else:
            print("Different", end=" ")
    print()