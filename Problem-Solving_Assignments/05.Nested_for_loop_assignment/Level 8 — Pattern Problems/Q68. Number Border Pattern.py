num = int(input("Enter a Number: "))
for i in range(num):
    for j in range(num):
        if i == 0 or i == num-1 or j == 0 or j == num-1:
            print("1",end="")
        else:
            print("0",end="")
    print()