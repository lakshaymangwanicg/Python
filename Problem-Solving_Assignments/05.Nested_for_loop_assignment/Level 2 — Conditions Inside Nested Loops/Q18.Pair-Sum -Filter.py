number = int(input("Enter a Number: "))
for i in range(1,number+1):
    for j in range(1,number+1):
        if (i+j)>number:
            print(i, j)