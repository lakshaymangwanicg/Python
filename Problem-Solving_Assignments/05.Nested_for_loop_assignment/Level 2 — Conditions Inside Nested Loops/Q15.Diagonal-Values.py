number = int(input("Enter a number: "))
for i in range(number):
    for j in range(number):
        if i == j:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()