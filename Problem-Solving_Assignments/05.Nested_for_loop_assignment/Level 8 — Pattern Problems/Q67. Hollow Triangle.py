num = int(input("Enter a Number: "))
for i in range(num):
    for j in range(num):
        if j == 0 or i == j or i == num-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()