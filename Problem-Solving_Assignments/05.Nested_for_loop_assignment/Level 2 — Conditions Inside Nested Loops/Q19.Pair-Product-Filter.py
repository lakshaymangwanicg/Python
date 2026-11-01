number = int(input("Enter a Number: "))
for i in range(1,number+1):
    for j in range(1,number+1):
        if (i*j)%2 == 0:
            print(i, j, i*j)

